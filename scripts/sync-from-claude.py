#!/usr/bin/env python3
"""
Sync files from ~/.claude into the AOK-Systems branch of this repo.

Usage:
    python3 scripts/sync-from-claude.py           # copy + show diff
    python3 scripts/sync-from-claude.py --commit  # copy + commit
"""

import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALL_STATE = os.path.expanduser("~/.claude/ecc/install-state.json")


def main():
    commit = "--commit" in sys.argv

    with open(INSTALL_STATE) as f:
        state = json.load(f)

    updated = []
    for op in state.get("operations", []):
        src_rel = op.get("sourceRelativePath", "")
        dest = op.get("destinationPath", "")
        if not src_rel or not dest:
            continue

        repo_path = os.path.join(REPO, src_rel)
        if not os.path.exists(dest):
            continue
        if not os.path.exists(repo_path):
            continue

        # compare content
        with open(dest, "rb") as f:
            claude_content = f.read()
        with open(repo_path, "rb") as f:
            repo_content = f.read()

        if claude_content != repo_content:
            shutil.copy2(dest, repo_path)
            updated.append(src_rel)

    if not updated:
        print("Already in sync — no changes.")
        return

    print(f"Updated {len(updated)} file(s):")
    for f in updated:
        print(f"  {f}")

    if commit:
        subprocess.run(["git", "add"] + updated, cwd=REPO, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"chore: sync {len(updated)} file(s) from ~/.claude"],
            cwd=REPO,
            check=True,
        )
        subprocess.run(["git", "push", "fork", "AOK-Systems"], cwd=REPO, check=True)
        print("Committed and pushed.")
    else:
        print("\nRun with --commit to commit and push.")


if __name__ == "__main__":
    main()
