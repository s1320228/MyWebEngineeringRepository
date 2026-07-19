# My Web Engineering Project

## Project Overview

This repository contains the project for the Web Engineering course. It is a Django web application with a REST API built using Django REST Framework.

## Technologies

- Python 3.12+
- Django 5.0+
- Django REST Framework
- SQLite (development) / PostgreSQL (production)
- uv (package management)
- Ruff (linter/formatter)
- Pytest (testing)

## Project Structure

```
MyWebEngineeringProject/
├── config/              # Django project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── core/                # Core application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   └── tests/           # Unit tests
├── manage.py            # Django management script
└── pyproject.toml       # Project dependencies
```

## Database Schema

### Item Model

The `Item` model is the foundational entity in the application.

| Field         | Type         | Constraints                    | Description                    |
|---------------|--------------|--------------------------------|--------------------------------|
| id            | BigAutoField | Primary Key                    | Auto-generated unique ID       |
| name          | CharField    | max_length=200, indexed        | Item name (required)           |
| description   | TextField    | blank=True, default=""         | Item description (optional)    |
| created_at    | DateTimeField| auto_now_add=True, indexed     | Creation timestamp             |
| updated_at    | DateTimeField| auto_now=True                  | Last update timestamp          |
| is_active     | BooleanField | default=True, indexed          | Soft delete flag               |

**Indexes:**
- `item_name_idx` - Index on `name` field for faster search/filter operations
- `item_is_active_idx` - Index on `is_active` field for filtering active items
- `item_created_at_idx` - Index on `created_at` field for ordering by date

**Ordering:** Items are ordered by `created_at` in descending order by default (newest first).

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd MyWebEngineeringProject
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Apply database migrations:

   ```bash
   uv run python manage.py migrate
   ```

4. Run the development server:

   ```bash
   uv run python manage.py runserver
   ```

## Configuration

The project uses environment variables for configuration. Create a `.env` file or set these variables:

- `DJANGO_SECRET_KEY` - Secret key for Django (required for production)
- `DJANGO_DEBUG` - Debug mode (default: True)
- `DJANGO_ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection URL (optional, uses SQLite by default)
- `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` - Individual database settings

## Testing

Run tests with pytest:

```bash
uv run pytest
```

Run tests with coverage report:

```bash
uv run pytest --cov=core
```

## Code Quality

Run linter:

```bash
uv run ruff check .
```

Fix linting issues:

```bash
uv run ruff check --fix .
```

Format code:

```bash
uv run ruff format .
```

## Version Control

This project uses Git and GitHub for version control.
