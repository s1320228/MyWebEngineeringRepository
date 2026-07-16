# AGENTS.md

## Project Scope

This is a Django web application developed for the Web Engineering course.

## Technologies

- Python 3.12+
- Django 5.0
- Django REST Framework
- uv for dependency management
- Git and GitHub

## Project Conventions

- Follow the existing project structure.
- Reuse existing code whenever possible.
- Keep views thin — place business logic in model methods or service modules.
- Use class-based views and DRF ViewSets over function-based views.
- Use `select_related` / `prefetch_related` to avoid N+1 queries.
- Add database indexes for frequently queried fields.
- Use environment variables for all secrets (never hardcode).
- Write clear and readable code.

## Commands

### Development Server
```bash
python manage.py runserver
```

### Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Testing
```bash
pytest
pytest --cov=.
pytest -v
```

### Linting & Formatting
```bash
ruff check .
ruff check --fix .
ruff format .
```

### Dependency Management (uv)
```bash
uv add <package>
uv remove <package>
uv sync
```

### Django Utilities
```bash
python manage.py createsuperuser
python manage.py shell
python manage.py dbshell
python manage.py showmigrations
```

## Constraints

- Do not modify unrelated files.
- Do not edit old/squashed migrations.
- Prefer small, focused commits.
- Always run `makemigrations` after model changes.
- Always run `ruff check` and `ruff format` before committing.

## Documentation

Keep README.md and project documentation up to date.

## Testing

When adding new functionality, also update or add appropriate tests.
- Model tests: test field validation, custom methods, relationships
- View/ViewSet tests: test endpoints with APITestCase
- Serializer tests: test validation logic
