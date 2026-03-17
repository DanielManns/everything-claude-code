# Git Workflow

## Commit Message Format
```
<type>: <description>

<optional body>
```

Types: feat, fix, refactor, docs, test, chore, perf, ci

Note: Attribution disabled globally via ~/.claude/settings.json.

## Branching

- **Git Flow** for image/release repositories: `main`, `develop`, feature branches, release branches, hotfixes
- Always test locally before committing

## Pull Request Workflow

When creating PRs:
1. Analyze full commit history (not just latest commit)
2. Use `git diff [base-branch]...HEAD` to see all changes
3. Draft comprehensive PR summary
4. Include test plan with TODOs
5. Push with `-u` flag if new branch
6. Small, focused PRs — easy to review
7. Rebase/squash PRs with many commits before merging
8. Only merge when build and SonarQube are green

> For the full development process (planning, TDD, code review) before git operations,
> see [development-workflow.md](./development-workflow.md).

## Versioning

SemVer: `MAJOR.MINOR.PATCH`
- MAJOR — breaking changes
- MINOR — new features (backwards compatible)
- PATCH — bug fixes and chores

## Definition of Done

Before marking a ticket Done:
- [ ] Pre-commit hooks passed
- [ ] Unit tests written
- [ ] Changelog updated (if needed)
- [ ] README updated (if needed)
- [ ] Docs updated (if needed)
- [ ] After merge: verify service runs correctly on cluster
