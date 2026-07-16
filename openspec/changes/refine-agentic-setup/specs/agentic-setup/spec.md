## ADDED Requirements

### Requirement: Broken agent artifacts MUST be removed
The system SHALL NOT contain any non-functional or empty skill directories. Any directory under `.agents/skills/` or `.opencode/skills/` that does not contain a valid `SKILL.md` file SHALL be removed.

#### Scenario: Empty directories detected and removed
- **WHEN** the `.agents/skills/` directory contains subdirectories that are empty or lack a valid `SKILL.md` file
- **THEN** the entire `.agents/` directory is removed from the project

#### Scenario: No broken artifacts remain after cleanup
- **WHEN** the cleanup is complete
- **THEN** no empty directories or broken skill references exist in the project

### Requirement: django-expert skill MUST be self-contained
The `django-expert` skill SHALL contain all necessary guidance inline. It MUST NOT reference external files that do not exist. It MUST NOT list related skills that do not exist in the project.

#### Scenario: Skill loads without broken references
- **WHEN** the agent loads the `django-expert` skill
- **THEN** all referenced files and related skills exist and are accessible

#### Scenario: Skill contains complete Django guidance
- **WHEN** the agent needs Django expertise for a task
- **THEN** the skill provides models, serializers, views, testing, and constraints guidance inline without requiring external reference files

### Requirement: opencode.json MUST configure formatter and permissions
The `opencode.json` file SHALL specify the Python formatter and define skill permission rules.

#### Scenario: Formatter is configured
- **WHEN** `opencode.json` is loaded
- **THEN** the Python formatter is set to `ruff`

#### Scenario: Skills are allowed by default
- **WHEN** `opencode.json` is loaded
- **THEN** the permission rules allow all skills (`"*": "allow"`)

### Requirement: openspec/config.yaml MUST contain project context
The `openspec/config.yaml` file SHALL include the project's tech stack, conventions, and per-artifact rules for proposals, designs, tasks, and specs.

#### Scenario: Project context is populated
- **WHEN** `openspec/config.yaml` is loaded
- **THEN** the `context` field contains the tech stack (Python 3.12+, Django 5.0, DRF, uv) and project conventions

#### Scenario: Per-artifact rules are defined
- **WHEN** an OpenSpec artifact is being created
- **THEN** the corresponding rules (proposal, design, tasks, specs) provide specific guidance for that artifact type

### Requirement: AGENTS.md MUST provide complete command reference
The `AGENTS.md` file SHALL include all development commands: development server, migrations, testing, linting, formatting, dependency management, and Django utilities.

#### Scenario: Agent can find lint/format commands
- **WHEN** the agent needs to lint or format code
- **THEN** `AGENTS.md` contains `ruff check .` and `ruff format .` commands

#### Scenario: Agent can find uv commands
- **WHEN** the agent needs to manage dependencies
- **THEN** `AGENTS.md` contains `uv add`, `uv remove`, and `uv sync` commands

#### Scenario: Agent can find Django commands
- **WHEN** the agent needs to run Django operations
- **THEN** `AGENTS.md` contains `runserver`, `makemigrations`, `migrate`, `createsuperuser`, `shell`, and `showmigrations` commands

### Requirement: .gitignore MUST exclude Django-specific files
The `.gitignore` file SHALL exclude Django database files, media directories, static files, environment variable files, and common IDE artifacts.

#### Scenario: Django database files are ignored
- **WHEN** a `db.sqlite3` file is created
- **THEN** it is not tracked by git

#### Scenario: Environment files are ignored
- **WHEN** a `.env` or `.env.local` file is created
- **THEN** it is not tracked by git

#### Scenario: Media and static directories are ignored
- **WHEN** `media/` or `staticfiles/` directories are created
- **THEN** they are not tracked by git
