## Why

The project needs a foundational Django application with a database schema to support the Web Engineering course requirements. This establishes the core data model and project structure that all future features will build upon.

## What Changes

- Create a new Django project with standard configuration
- Create a new Django app for the core domain
- Define database models with appropriate fields, relationships, and indexes
- Implement `__str__()` methods for all models to improve admin and debug readability
- Configure the project to include the new app in `INSTALLED_APPS`
- Create and apply initial database migrations
- Add unit tests for all models covering field validation, relationships, and custom methods
- Update project documentation to reflect the database design

## Capabilities

### New Capabilities

- `database-schema`: Core database models and relationships for the application domain

### Modified Capabilities

None - this is the initial project setup.

## Impact

- **Code**: New Django project structure, app directory, models.py, migrations, tests
- **Dependencies**: Django 5.0, Django REST Framework (already in project scope)
- **Database**: New SQLite database with initial schema (or configured database backend)
- **Configuration**: settings.py updated with new app, database configuration

## Non-goals

- This change does not implement any views, URLs, or API endpoints
- No user authentication or authorization is included
- No business logic beyond model definitions and their tests
- No integration with external services or APIs
