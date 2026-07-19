## 1. Django Project Setup

- [x] 1.1 Create Django project structure using `django-admin startproject config .`
- [x] 1.2 Create `core` app using `python manage.py startapp core`
- [x] 1.3 Add `core` app to `INSTALLED_APPS` in `config/settings.py`
- [x] 1.4 Verify project structure with `python manage.py check`

## 2. Item Model Implementation

- [x] 2.1 Define `Item` model in `core/models.py` with fields: `name`, `description`, `created_at`, `updated_at`, `is_active`
- [x] 2.2 Add database indexes on `name`, `is_active`, and `created_at` fields using `Meta.indexes`
- [x] 2.3 Implement `__str__()` method to return the item's name
- [x] 2.4 Add `Meta` class with `ordering = ['-created_at']` and `verbose_name`/`verbose_name_plural`

## 3. Model Unit Tests

- [x] 3.1 Create `core/tests/test_models.py` with test class for `Item` model
- [x] 3.2 Write tests for field validation (max_length on `name`, blank on `description`)
- [x] 3.3 Write tests for default values (`is_active` defaults to `True`, `description` defaults to empty string)
- [x] 3.4 Write tests for auto-generated timestamps (`created_at` set on creation, `updated_at` updated on save)
- [x] 3.5 Write tests for `__str__()` method output
- [x] 3.6 Run tests with `pytest core/tests/test_models.py -v` and verify all pass

## 4. Database Migrations

- [x] 4.1 Create initial migration with `python manage.py makemigrations core`
- [x] 4.2 Verify migration file exists in `core/migrations/` and contains correct operations
- [x] 4.3 Apply migrations with `python manage.py migrate`
- [x] 4.4 Verify database schema with `python manage.py dbshell` and check table structure

## 5. Configuration and Verification

- [x] 5.1 Configure database settings in `config/settings.py` to use environment variables for production flexibility
- [x] 5.2 Add `pytest` and `pytest-django` to project dependencies if not already present
- [x] 5.3 Configure pytest in `pyproject.toml` or `pytest.ini` with Django settings module
- [x] 5.4 Run full test suite with `pytest --cov=core` and verify coverage is above 90%
- [x] 5.5 Run linter with `ruff check .` and fix any issues
- [x] 5.6 Run formatter with `ruff format .` to ensure code style consistency

## 6. Documentation

- [x] 6.1 Update `README.md` with project setup instructions and database schema overview
- [x] 6.2 Add model documentation comments to `core/models.py` explaining field purposes
