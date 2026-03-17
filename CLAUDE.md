# Claude Code — User Configuration

## Core Philosophy

**Key Principles:**
1. **Agent-First**: Delegate to specialized agents for complex work
2. **Parallel Execution**: Use Task tool with multiple agents when possible
3. **Plan Before Execute**: Use Plan Mode for complex operations
4. **Test-Driven**: Write tests before implementation
5. **Security-First**: Never compromise on security

---

## Rules

Detailed, actionable standards live in `~/.claude/rules/`:

| File | Contents |
|---|---|
| [common/coding-style.md](rules/common/coding-style.md) | Immutability, file organization, repo structure, error handling |
| [common/testing.md](rules/common/testing.md) | TDD workflow, 80% coverage, Xray documentation |
| [common/git-workflow.md](rules/common/git-workflow.md) | Commit format, branching, PR workflow, SemVer, Definition of Done |
| [common/development-workflow.md](rules/common/development-workflow.md) | Full feature pipeline: research → plan → TDD → review → commit |
| [common/security.md](rules/common/security.md) | Security checks, secret management, privacy |
| [common/agents.md](rules/common/agents.md) | Agent orchestration, when to use which agent |
| [common/patterns.md](rules/common/patterns.md) | API response, repository patterns |
| [common/performance.md](rules/common/performance.md) | Model selection, context management |
| [common/hooks.md](rules/common/hooks.md) | Hooks system |

Language-specific overrides: `rules/python/`, `rules/golang/`, `rules/typescript/`, `rules/kotlin/`, `rules/swift/`, `rules/php/`

---

## Available Agents

Located in `~/.claude/agents/`:

| Agent | Purpose |
|---|---|
| planner | Feature implementation planning |
| architect | System design and architecture |
| tdd-guide | Test-driven development |
| code-reviewer | Code review for quality and security |
| security-reviewer | Security vulnerability analysis |
| build-error-resolver | Build error resolution |
| e2e-runner | Playwright E2E testing |
| refactor-cleaner | Dead code cleanup |
| doc-updater | Documentation updates |

---

## Editor

VSCode with Claude Code extension.

---

## Knowledge Capture

- Personal debugging notes, preferences, and temporary context → auto memory
- Each service has its own `docs/` directory for service-level documentation
- Cross-cutting and top-level documentation lives in a separate dedicated git repository; pull from there before adding new top-level docs
- If the current task already produces the relevant docs or examples, do not duplicate elsewhere
- If unsure where something belongs, ask before creating a new top-level doc
