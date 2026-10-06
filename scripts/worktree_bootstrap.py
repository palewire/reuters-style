"""Prepare a Git worktree for local development."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from collections.abc import Sequence

WORKTREE_ID_VARIABLE = "WORKTREE_ID"


class Runner(Protocol):
    """Run commands needed by the bootstrap."""

    def capture(self, command: Sequence[str], cwd: Path) -> str:
        """Run a command and return its standard output.

        Args:
            command: Program and arguments to run.
            cwd: Directory in which to run the command.

        Returns:
            Captured standard output.

        Example:
            `runner.capture(("git", "rev-parse", "--show-toplevel"), cwd)`
        """

    def execute(self, command: Sequence[str], cwd: Path) -> None:
        """Run a command with output attached to the terminal.

        Args:
            command: Program and arguments to run.
            cwd: Directory in which to run the command.

        Returns:
            None.

        Example:
            `runner.execute(("uv", "sync", "--locked"), cwd)`
        """


class SubprocessRunner:
    """Run bootstrap commands in subprocesses."""

    def capture(self, command: Sequence[str], cwd: Path) -> str:
        """Run a command and return its standard output.

        Args:
            command: Program and arguments to run without a shell.
            cwd: Directory in which to run the command.

        Returns:
            Captured standard output.

        Example:
            `SubprocessRunner().capture(("git", "status", "--short"), cwd)`
        """
        result = subprocess.run(  # noqa: S603 - Commands are never shell strings.
            command,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        return result.stdout

    def execute(self, command: Sequence[str], cwd: Path) -> None:
        """Run a command with output attached to the terminal.

        Args:
            command: Program and arguments to run without a shell.
            cwd: Directory in which to run the command.

        Returns:
            None.

        Example:
            `SubprocessRunner().execute(("uv", "sync", "--locked"), cwd)`
        """
        subprocess.run(  # noqa: S603 - Commands are never shell strings.
            command,
            cwd=cwd,
            check=True,
        )


@dataclass(frozen=True)
class GitCheckout:
    """Paths Git reports for the current and primary checkouts."""

    current: Path
    primary: Path

    @classmethod
    def discover(cls, runner: Runner, cwd: Path) -> GitCheckout:
        """Discover checkout paths from Git metadata.

        Args:
            runner: Command runner used for Git queries.
            cwd: Directory from which to discover the checkout.

        Returns:
            Current and primary checkout paths.

        Example:
            `GitCheckout.discover(SubprocessRunner(), Path.cwd())`
        """
        current_output = runner.capture(
            ("git", "rev-parse", "--show-toplevel"),
            cwd,
        )
        current = Path(current_output.strip()).resolve()
        worktree_output = runner.capture(
            ("git", "worktree", "list", "--porcelain"),
            current,
        )
        primary = parse_primary_checkout(worktree_output)
        return cls(current=current, primary=primary)

    @property
    def is_linked_worktree(self) -> bool:
        """Check whether this checkout is a linked worktree.

        Returns:
            True for a linked worktree, False for the primary checkout.

        Example:
            `GitCheckout(Path("/tmp/feature"), Path("/tmp/main")).is_linked_worktree`
        """
        return self.current != self.primary


def parse_primary_checkout(output: str) -> Path:
    """Return the primary checkout from Git's porcelain worktree listing.

    Args:
        output: Text produced by `git worktree list --porcelain`.

    Returns:
        Resolved path of the first checkout in the listing.

    Example:
        `parse_primary_checkout("worktree /tmp/main\\nHEAD abc\\n")`
    """
    for line in output.splitlines():
        if line.startswith("worktree "):
            return Path(line.removeprefix("worktree ")).resolve()
    msg = "Git did not report a primary checkout."
    raise ValueError(msg)


def worktree_identifier(checkout: Path) -> str:
    """Build a stable, environment-safe identifier for a checkout.

    Args:
        checkout: Path to the worktree.

    Returns:
        Lowercase slug and short path hash.

    Example:
        `worktree_identifier(Path("/tmp/my-feature"))`
    """
    resolved = checkout.resolve()
    slug = re.sub(r"[^a-z0-9]+", "-", resolved.name.lower()).strip("-")
    safe_slug = slug or "worktree"
    path_hash = hashlib.sha256(os.fsencode(resolved)).hexdigest()[:8]
    return f"{safe_slug}-{path_hash}"


def ensure_shared_env(checkout: GitCheckout) -> None:
    """Link the primary .env into a linked worktree without overwriting files.

    Args:
        checkout: Current and primary checkout paths.

    Returns:
        None.

    Example:
        `ensure_shared_env(GitCheckout(Path("/tmp/feature"), Path("/tmp/main")))`
    """
    if not checkout.is_linked_worktree:
        return

    source = checkout.primary / ".env"
    destination = checkout.current / ".env"
    if not source.exists():
        return

    if destination.is_symlink() and destination.resolve() == source.resolve():
        return
    if destination.exists() or destination.is_symlink():
        msg = f"Refusing to replace existing {destination}."
        raise FileExistsError(msg)

    destination.symlink_to(source)


def ensure_worktree_override(checkout: Path, identifier: str) -> None:
    """Create or update the managed identifier while preserving local settings.

    Args:
        checkout: Worktree whose local override file will be updated.
        identifier: Stable identifier for this checkout.

    Returns:
        None.

    Example:
        `ensure_worktree_override(Path("/tmp/feature"), "feature-12345678")`
    """
    override = checkout / ".env.worktree"
    assignment = f"{WORKTREE_ID_VARIABLE}={identifier}"
    if not override.exists():
        override.write_text(
            "# Worktree-local overrides. Load this after .env when supported.\n"
            f"{assignment}\n",
            encoding="utf-8",
        )
        return

    original = override.read_text(encoding="utf-8")
    lines = original.splitlines()
    matching_indexes = [
        index
        for index, line in enumerate(lines)
        if line.startswith(f"{WORKTREE_ID_VARIABLE}=")
    ]
    if len(matching_indexes) > 1:
        msg = f"{override} contains multiple {WORKTREE_ID_VARIABLE} assignments."
        raise ValueError(msg)
    if matching_indexes:
        index = matching_indexes[0]
        if lines[index] == assignment:
            return
        lines[index] = assignment
    else:
        if lines and lines[-1]:
            lines.append("")
        lines.append(assignment)

    override.write_text("\n".join(lines) + "\n", encoding="utf-8")


def bootstrap(cwd: Path, uv: str, runner: Runner) -> GitCheckout:
    """Prepare local environment files and install locked dependencies.

    Args:
        cwd: Directory from which to discover the checkout.
        uv: Command name or path for uv.
        runner: Command runner for Git and uv.

    Returns:
        Current and primary checkout paths.

    Example:
        `bootstrap(Path.cwd(), "uv", SubprocessRunner())`
    """
    checkout = GitCheckout.discover(runner, cwd)
    ensure_shared_env(checkout)
    ensure_worktree_override(
        checkout.current,
        worktree_identifier(checkout.current),
    )
    runner.execute(
        (uv, "sync", "--all-groups", "--locked"),
        checkout.current,
    )
    return checkout


def main() -> None:
    """Run the worktree bootstrap from the command line.

    Returns:
        None.

    Example:
        `python scripts/worktree_bootstrap.py --uv uv`
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uv", default=os.environ.get("UV", "uv"))
    args = parser.parse_args()

    checkout = bootstrap(Path.cwd(), args.uv, SubprocessRunner())
    location = "linked worktree" if checkout.is_linked_worktree else "primary checkout"
    print(f"Bootstrap complete for {location}.")


if __name__ == "__main__":
    main()
