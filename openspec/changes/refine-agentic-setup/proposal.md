## Why

The project's agentic setup (OpenCode skills, AGENTS.md, opencode.json, OpenSpec config) was scaffolded but contained broken artifacts, missing references, and incomplete configuration. Before the Django project scope is defined, the agent infrastructure must be clean and reliable so that future feature work benefits from accurate skill guidance, correct commands, and coherent planning rules.

## What Changes

- **Remove broken `.agents/skills/` directory** — contained 5 empty directories with `.md` suffix names that were non-functional and not discoverable by OpenCode.
- **Refine `django-expert` skill** — remove references to non-existent `references/*.md` files and phantom related skills (`fullstack-guardian`, `fastapi-expert`, `test-master`); bump version to 2.0.0; add ruff commands to constraints.
- **Configure `opencode.json`** — set ruff as the Python formatter, allow all skills via permission rules.
- **Populate `openspec/config.yaml`** — add project context (tech stack, conventions) and per-artifact rules for proposals, designs, tasks, and specs.
- **Enhance `AGENTS.md`** — add ruff lint/format commands, uv dependency management commands, Django utility commands, DRF mentions, and testing guidance.
- **Update `.gitignore`** — add Django-specific entries (`db.sqlite3`, `media/`, `staticfiles/`), environment variable files, IDE files, and packaging artifacts.

## Non-goals

- This change does not define the Django project's domain or features — that is deferred to future OpenSpec changes.
- No application code (models, views, serializers) is created or modified.
- No new Django apps are introduced.
- OpenSpec workflow skills (openspec-*) are not modified.

## Capabilities

### New Capabilities
- `agentic-setup`: Configuration and maintenance of the AI agent infrastructure — OpenCode skills, AGENTS.md, opencode.json, OpenSpec config, and .gitignore for the Django project.

### Modified Capabilities
<!-- None — no existing specs to modify -->

## Impact

- **Affected files**: `AGENTS.md`, `opencode.json`, `.gitignore`, `openspec/config.yaml`, `.opencode/skills/django-expert/SKILL.md`
- **Removed**: `.agents/` directory (was empty/broken)
- **Affected Django apps**: None — this is purely agent infrastructure, no Django apps exist yet.
- **Dependencies**: No new Python packages added.
