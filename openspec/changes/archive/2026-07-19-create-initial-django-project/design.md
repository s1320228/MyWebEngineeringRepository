## Context

This is a greenfield Django project for a Web Engineering course. The project requires establishing a solid foundation with a Django application, database schema, and testing infrastructure. The domain is currently undefined (TBD), so the initial schema will be minimal and extensible.

Current state: No Django project exists yet. The repository contains only OpenSpec planning artifacts and project configuration files (AGENTS.md, pyproject.toml, etc.).

Constraints:
- Must follow Django best practices and project conventions from AGENTS.md
- Must use Django 5.0 and Python 3.12+
- Must include comprehensive unit tests for models
- Must use environment variables for configuration

## Goals / Non-Goals

**Goals:**
- Establish a working Django project with a single app
- Create a foundational database schema with at least one model
- Ensure all models have proper `__str__()` methods
- Set up database migrations
- Implement unit tests for all models
- Follow Django conventions and project standards

**Non-Goals:**
- Implementing views, URLs, or API endpoints
- Adding user authentication or authorization
- Creating business logic beyond model definitions
- Integrating external services or APIs
- Optimizing for production deployment

## Decisions

### 1. Project Structure

**Decision**: Use standard Django project layout with one app named `core`.

**Rationale**: The `core` app will contain foundational models and shared functionality. This follows Django convention of having a central app for cross-cutting concerns.

**Alternatives considered**:
- Multiple domain-specific apps: Rejected because the domain is not yet defined
- No app structure: Rejected because Django requires at least one app

### 2. Initial Models

**Decision**: Create a minimal but extensible model structure. Since the domain is TBD, I will create a generic `Item` model that can serve as a placeholder or be renamed later.

**Model Structure**:
```
Item
├── id (AutoField, primary key)
├── name (CharField, max_length=200)
├── description (TextField, blank=True)
├── created_at (DateTimeField, auto_now_add=True)
├── updated_at (DateTimeField, auto_now=True)
└── is_active (BooleanField, default=True)
```

**Rationale**: Provides a simple, reusable model with common fields. The `is_active` field allows soft deletes. Timestamps enable audit trails.

**Alternatives considered**:
- No models until domain is defined: Rejected because the requirement explicitly asks for database schema
- Complex domain models: Rejected because domain is unknown

### 3. Database Backend

**Decision**: Use SQLite for development (Django default).

**Rationale**: SQLite is zero-configuration, file-based, and sufficient for development and testing. Can be switched to PostgreSQL/MySQL for production via environment variables.

**Alternatives considered**:
- PostgreSQL from the start: Rejected because it requires additional setup and the domain is not yet defined
- MySQL: Rejected for same reasons as PostgreSQL

### 4. Database Indexes

**Decision**: Add indexes on frequently queried fields:
- `name` (for search/filter operations)
- `is_active` (for filtering active items)
- `created_at` (for ordering by date)

**Rationale**: These fields are commonly used in queries and sorting. Indexes improve query performance.

### 5. Testing Strategy

**Decision**: Use pytest with pytest-django for model tests.

**Test Coverage**:
- Model field validation (required fields, max_length, choices)
- Model `__str__()` method output
- Model relationships (if any are added)
- Custom model methods (if any)
- Default values and auto fields

**Rationale**: pytest is more concise than Django's unittest runner. pytest-django provides excellent Django integration. Testing models ensures data integrity.

**Alternatives considered**:
- Django's built-in test runner: Rejected because pytest is more popular and concise
- No tests: Rejected because AGENTS.md requires tests alongside features

### 6. Model Relationship Diagram

```
┌─────────────────────────────────────┐
│              Item                   │
├─────────────────────────────────────┤
│ id (PK)                           │
│ name (VARCHAR 200, indexed)       │
│ description (TEXT)                │
│ created_at (DATETIME, indexed)    │
│ updated_at (DATETIME)             │
│ is_active (BOOLEAN, indexed)      │
└─────────────────────────────────────┘
```

### 7. API Endpoints

**Decision**: No API endpoints will be created in this change.

**Rationale**: The proposal explicitly states this is out of scope. Views and URLs will be added in future changes once the domain is defined.

## Risks / Trade-offs

**[Risk] Generic model may not fit future domain** → **Mitigation**: The `Item` model is simple and can be renamed or replaced. Migration history will be squashed before production if needed.

**[Risk] SQLite limitations for production** → **Mitigation**: Database backend is configurable via environment variables. Switching to PostgreSQL/MySQL is straightforward.

**[Risk] Minimal schema requires future migrations** → **Mitigation**: Django migrations handle schema evolution. Initial migration establishes the baseline.

**[Trade-off] Simplicity vs. Future-proofing**: Chose a minimal, generic schema over trying to predict future needs. This reduces complexity now but may require refactoring later.
