## ADDED Requirements

### Requirement: Django project structure exists
The system SHALL have a Django project with a `core` app configured in `INSTALLED_APPS`.

#### Scenario: Project initialization
- **WHEN** the Django project is created
- **THEN** a project directory exists with `settings.py`, `urls.py`, and `wsgi.py`
- **THEN** a `core` app directory exists with `models.py`, `views.py`, and `apps.py`
- **THEN** the `core` app is listed in `INSTALLED_APPS` in `settings.py`

### Requirement: Item model exists with required fields
The system SHALL have an `Item` model with the following fields: `name` (CharField, max_length=200), `description` (TextField, blank=True), `created_at` (DateTimeField, auto_now_add=True), `updated_at` (DateTimeField, auto_now=True), and `is_active` (BooleanField, default=True).

#### Scenario: Model field validation
- **WHEN** an `Item` instance is created with a `name` longer than 200 characters
- **THEN** the system SHALL raise a validation error

#### Scenario: Model field defaults
- **WHEN** an `Item` instance is created without specifying `description`
- **THEN** the `description` field SHALL default to an empty string
- **WHEN** an `Item` instance is created without specifying `is_active`
- **THEN** the `is_active` field SHALL default to `True`

#### Scenario: Auto-generated timestamps
- **WHEN** an `Item` instance is created and saved to the database
- **THEN** the `created_at` field SHALL be automatically set to the current timestamp
- **WHEN** an existing `Item` instance is updated and saved
- **THEN** the `updated_at` field SHALL be automatically updated to the current timestamp
- **THEN** the `created_at` field SHALL remain unchanged

### Requirement: Item model has __str__ method
The system SHALL implement a `__str__()` method on the `Item` model that returns the item's name.

#### Scenario: String representation
- **WHEN** the `__str__()` method is called on an `Item` instance
- **THEN** the method SHALL return the value of the `name` field

### Requirement: Database indexes are created
The system SHALL create database indexes on the `name`, `is_active`, and `created_at` fields of the `Item` model.

#### Scenario: Index existence
- **WHEN** the database migrations are applied
- **THEN** an index SHALL exist on the `name` field
- **THEN** an index SHALL exist on the `is_active` field
- **THEN** an index SHALL exist on the `created_at` field

### Requirement: Initial migrations are created and applied
The system SHALL have initial database migrations for the `Item` model that can be applied successfully.

#### Scenario: Migration creation
- **WHEN** `python manage.py makemigrations` is executed
- **THEN** a migration file SHALL be created in the `core/migrations/` directory
- **THEN** the migration SHALL create the `Item` table with all specified fields and indexes

#### Scenario: Migration application
- **WHEN** `python manage.py migrate` is executed
- **THEN** the `Item` table SHALL be created in the database
- **THEN** all indexes SHALL be created in the database

### Requirement: Unit tests exist for Item model
The system SHALL have comprehensive unit tests for the `Item` model covering field validation, default values, auto fields, and the `__str__()` method.

#### Scenario: Test execution
- **WHEN** `pytest` is executed
- **THEN** all model tests SHALL pass
- **THEN** tests SHALL cover field validation (max_length, blank, default values)
- **THEN** tests SHALL cover auto-generated timestamps (created_at, updated_at)
- **THEN** tests SHALL cover the `__str__()` method output

#### Scenario: Test coverage
- **WHEN** `pytest --cov=core` is executed
- **THEN** the `Item` model SHALL have at least 90% test coverage
