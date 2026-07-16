## 1. Remove Broken Artifacts

- [ ] 1.1 Delete the `.agents/` directory and all its contents
- [ ] 1.2 Verify no empty or broken skill directories remain in the project

## 2. Refine django-expert Skill

- [ ] 2.1 Remove references to non-existent `references/*.md` files from `.opencode/skills/django-expert/SKILL.md`
- [ ] 2.2 Remove phantom related skills (`fullstack-guardian`, `fastapi-expert`, `test-master`) from frontmatter
- [ ] 2.3 Add ruff lint/format commands to the skill's constraints section
- [ ] 2.4 Bump skill version to 2.0.0 in frontmatter
- [ ] 2.5 Verify the skill loads correctly and all self-contained examples are valid

## 3. Configure opencode.json

- [ ] 3.1 Set `"formatter": { "python": "ruff" }` in `opencode.json`
- [ ] 3.2 Add permission rules to allow all skills (`"*": "allow"`)
- [ ] 3.3 Verify `opencode.json` is valid JSON

## 4. Populate openspec/config.yaml

- [ ] 4.1 Add project context (tech stack, conventions) to the `context` field
- [ ] 4.2 Add per-artifact rules for `proposal` (word limit, non-goals section, affected apps)
- [ ] 4.3 Add per-artifact rules for `design` (model diagrams, API endpoints, indexes)
- [ ] 4.4 Add per-artifact rules for `tasks` (2-hour chunks, testable, migration tasks)
- [ ] 4.5 Add per-artifact rules for `specs` (SHALL statements, happy-path + error scenarios)

## 5. Enhance AGENTS.md

- [ ] 5.1 Add ruff lint/format commands (`ruff check .`, `ruff check --fix .`, `ruff format .`)
- [ ] 5.2 Add uv dependency management commands (`uv add`, `uv remove`, `uv sync`)
- [ ] 5.3 Add Django utility commands (`createsuperuser`, `shell`, `dbshell`, `showmigrations`)
- [ ] 5.4 Add DRF mention to the Technologies section
- [ ] 5.5 Add testing guidance (model tests, viewset tests, serializer tests)

## 6. Update .gitignore

- [ ] 6.1 Add Django-specific entries (`db.sqlite3`, `db.sqlite3-journal`, `*.log`, `media/`, `staticfiles/`)
- [ ] 6.2 Add environment variable file entries (`.env`, `.env.local`, `.env.*.local`)
- [ ] 6.3 Add IDE entries (`.idea/`, `*.swp`, `*.swo`)
- [ ] 6.4 Add Python packaging entries (`dist/`, `build/`, `*.egg-info/`, `*.egg`)

## 7. Verification

- [ ] 7.1 Run `openspec status --change "refine-agentic-setup" --json` and confirm all artifacts are done
- [ ] 7.2 Confirm no broken file references exist in any skill
- [ ] 7.3 Confirm `opencode.json` parses as valid JSON
- [ ] 7.4 Confirm `.gitignore` entries cover all Django-specific patterns
