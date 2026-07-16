## Context

The project has an OpenCode agentic setup consisting of:
- **Skills** (`.opencode/skills/`): 7 skills — 1 Django domain skill (`django-expert`) and 6 OpenSpec workflow skills
- **AGENTS.md**: Project-level instructions for the agent
- **opencode.json**: OpenCode configuration (was empty)
- **openspec/config.yaml**: OpenSpec planning rules (was unpopulated)
- **.gitignore**: File exclusion rules (was missing Django-specific entries)
- **`.agents/skills/`**: A broken directory with 5 empty subdirectories using `.md` suffix names — not a valid OpenCode skill format

The `django-expert` skill referenced non-existent `references/*.md` files and phantom related skills. `opencode.json` was empty. `openspec/config.yaml` had no project context or rules. `AGENTS.md` was missing lint, format, and uv commands.

## Goals / Non-Goals

**Goals:**
- Remove all broken/non-functional agent artifacts
- Ensure the `django-expert` skill is self-contained and accurate
- Configure `opencode.json` with formatter and permission settings
- Populate `openspec/config.yaml` with project context and per-artifact rules
- Make `AGENTS.md` a complete reference for agent commands and conventions
- Add Django-specific entries to `.gitignore`

**Non-Goals:**
- Defining the Django project's domain features
- Creating new Django apps or models
- Modifying OpenSpec workflow skills (openspec-*)
- Adding new skills beyond what exists

## Decisions

### 1. Remove `.agents/skills/` entirely instead of migrating

**Decision**: Delete the entire `.agents/` directory.

**Rationale**: The `.agents/skills/` directory contained 5 entries that were empty directories named with `.md` suffixes (e.g., `django-expert.md/`). These are not valid OpenCode skill format (which requires `<name>/SKILL.md`). The same `django-expert` content already exists in `.opencode/skills/django-expert/SKILL.md`. The other 4 entries (`code-review-expert`, `django-patterns`, `receiving-code-review`, `refactor`) had no content and no corresponding `.opencode/skills/` equivalents — they were phantom entries.

**Alternatives considered**:
- Migrate to `.opencode/skills/` format — rejected because the directories were empty, there was nothing to migrate.
- Keep as documentation stubs — rejected because broken artifacts cause confusion.

### 2. Make `django-expert` skill self-contained

**Decision**: Remove all references to external `references/*.md` files and non-existent related skills. Bump version to 2.0.0.

**Rationale**: The skill referenced `references/models-orm.md`, `references/drf-serializers.md`, etc., but these files never existed. The `related-skills` field listed `fullstack-guardian`, `fastapi-expert`, `test-master` — none of which exist. A self-contained skill with inline examples is more reliable than one with broken external references.

**Alternatives considered**:
- Create the missing reference files — rejected because the skill's inline example and constraints already cover the essential guidance. Reference files can be added later if the skill grows.

### 3. Use ruff as the sole formatter in opencode.json

**Decision**: Set `"formatter": { "python": "ruff" }` in `opencode.json`.

**Rationale**: The project's `pyproject.toml` already configures both `[tool.black]` and `[tool.ruff]`. Ruff can replace Black as a formatter (`ruff format`), so using a single tool reduces complexity. The AGENTS.md already instructs the agent to use `ruff format`.

**Alternatives considered**:
- Keep Black as formatter, Ruff as linter — rejected because it's redundant when Ruff handles both.
- No formatter config — rejected because the agent needs to know which tool to run.

### 4. Populate openspec/config.yaml with Django-specific rules

**Decision**: Add project context and per-artifact rules for proposal, design, tasks, and specs.

**Rationale**: The config was empty, meaning OpenSpec would generate artifacts without any project-specific guidance. Adding context ensures proposals know the tech stack, designs consider Django patterns, and tasks are scoped appropriately.

### File Structure After Changes

```
MyWebEngineeringProject/
├── .opencode/
│   ├── skills/
│   │   ├── django-expert/
│   │   │   └── SKILL.md          ← refined (v2.0.0, self-contained)
│   │   ├── openspec-apply-change/
│   │   ├── openspec-archive-change/
│   │   ├── openspec-explore/
│   │   ├── openspec-propose/
│   │   ├── openspec-sync-specs/
│   │   └── openspec-update-change/
│   └── commands/
│       └── opsx-*.md             ← unchanged
├── openspec/
│   ├── config.yaml               ← populated with context + rules
│   ├── changes/
│   └── specs/
├── AGENTS.md                     ← enhanced with full command reference
├── opencode.json                 ← configured (formatter, permissions)
├── .gitignore                    ← Django-specific entries added
└── pyproject.toml                ← unchanged
```

No model relationships, API endpoints, or database indexes are involved — this change is purely agent infrastructure.

## Risks / Trade-offs

- **[Risk] Future skills may need reference files** → Mitigation: The `django-expert` skill can be extended with `references/` files later when the content justifies splitting. The inline example covers current needs.
- **[Risk] Removing `.agents/` may break compatibility with other tools** → Mitigation: The directory contained only empty directories. No other tool was using it.
- **[Risk] Ruff-only formatting may differ from Black output** → Mitigation: `ruff format` is designed to be a Black-compatible formatter. Differences are cosmetic and documented.
