# Royal Dance School Reservation System

## Project Overview

Royal Dance School Reservation System is a Django web application developed for the Web Engineering course.

The application allows users to:

- Create an account
- Log in and log out
- View dance instructors
- View instructor profile images
- Select an instructor
- Check available lesson dates dynamically
- Submit a dance lesson reservation

The interface uses Bootstrap for responsive design and HTMX for asynchronous content updates.

---

## Main Features

- User registration
- User login and logout
- Authentication-protected reservation page
- Instructor listing with profile images
- Dance lesson reservation form
- Database-backed reservation storage
- Dynamic available-date display using HTMX
- Responsive Bootstrap navigation
- Black-and-gold visual theme
- Django administration interface
- Automated tests with Pytest

---

## Technologies

- Python 3.12+
- Django
- SQLite for local development
- HTML5
- CSS3
- Bootstrap 5
- HTMX
- Pillow
- uv
- Ruff
- Pytest
- pytest-django
- Git
- GitHub
- OpenCode
- OpenSpec
- PostgreSQL for production
- Gunicorn
- WhiteNoise
- Render
- dj-database-url

---

## Project Structure

```text
MyWebEngineeringProject/
├── .opencode/
│   ├── commands/
│   └── skills/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_forms.py
│   │   ├── test_views.py
│   │   └── test_auth.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/
│   └── instructors/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── instructor_list.html
│   ├── reservation.html
│   ├── available_dates.html
│   ├── success.html
│   ├── login.html
│   └── register.html
├── AGENTS.md
├── manage.py
├── pyproject.toml
└── README.md
```

---

## Database Schema

The application uses Django's built-in user model together with the `Instructor` and `Reservation` models.

### Instructor Model

The `Instructor` model stores information about dance instructors.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary key | Automatically generated instructor ID |
| `name` | CharField | Maximum length 100 | Instructor name |
| `photo` | ImageField | Optional | Instructor profile image |

### Reservation Model

The `Reservation` model stores dance lesson reservations.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary key | Automatically generated reservation ID |
| `instructor` | ForeignKey | References Instructor | Selected instructor |
| `customer_name` | CharField | Maximum length 100 | Name entered by the customer |
| `reservation_date` | DateField | Required | Requested lesson date |
| `created_at` | DateTimeField | Automatically generated | Reservation creation time |

### Relationships

One instructor can have multiple reservations.

```text
Instructor 1 ─────────── * Reservation
```

Django's built-in authentication tables are also used to store user accounts, passwords and sessions.

---

## Business Logic

The application includes the following business logic:

- Only authenticated users can access the reservation page.
- Submitted reservation data is validated with a Django `ModelForm`.
- Valid reservations are saved to the database.
- Invalid reservations are returned to the form with validation errors.
- The selected instructor determines the available dates shown by HTMX.
- Users can register, log in and log out securely.
- Logout requests use the POST method with CSRF protection.

---

## Templates

Page presentation is separated from Python business logic.

Django views pass context data to HTML templates using `render()`.

The base template provides:

- Shared navigation
- Bootstrap integration
- HTMX integration
- Login and logout controls
- Shared footer
- Shared stylesheet

Individual templates extend the base template and provide page-specific content.

---

## HTMX Interface

HTMX is used on the reservation page.

When the user selects an instructor, the browser sends an asynchronous request to the available-dates endpoint.

The returned partial template is inserted into the following element:

```html
<div id="available"></div>
```

This allows the page to display available lesson dates without performing a full-page reload.

---

## User Input

The application accepts user input through:

- Registration form
- Login form
- Instructor selection
- Customer name field
- Reservation date field
- Logout POST form

Django forms provide server-side validation and CSRF protection.

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd MyWebEngineeringProject
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Apply database migrations

```bash
uv run python manage.py migrate
```

### 4. Create an administrator account

```bash
uv run python manage.py createsuperuser
```

### 5. Run the development server

```bash
uv run python manage.py runserver
```

Open the following address in a browser:

```text
http://127.0.0.1:8000/
```

---

## Adding Instructors

Instructors can be added through the Django administration site.

```text
http://127.0.0.1:8000/admin/
```

An instructor can have:

- A name
- A profile image

Uploaded images are stored under:

```text
static/images/instructors/
```

---

## URL Documentation

### Home

```text
/
```

Displays the Royal Dance School home page.

### Instructor List

```text
/instructors/
```

Displays available instructors and their profile images.

### Reservation

```text
/reservation/
```

Displays the reservation form.

Authentication is required.

### Available Dates

```text
/available-dates/
```

Returns an HTML fragment containing dates for the selected instructor.

This endpoint is called asynchronously by HTMX.

### Register

```text
/register/
```

Displays the user registration form and creates a new account.

### Login

```text
/login/
```

Displays the login form.

### Logout

```text
/logout/
```

Logs out the current user through a POST request.

### Django Administration

```text
/admin/
```

Allows administrators to manage users, instructors and reservations.

---

## Testing

The project uses Pytest and pytest-django.

Run all tests:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

Run a specific test file:

```bash
uv run pytest core/tests/test_views.py
```

Run tests with coverage:

```bash
uv run pytest --cov=core
```

The automated tests cover:

- Instructor model creation
- Reservation model creation
- Model relationships
- Reservation form validation
- Required form fields
- Authentication requirements
- Registration
- Login
- Logout
- Reservation submission
- Invalid reservation rejection
- Instructor list display
- HTMX available-date responses

---

## Code Quality

Run Ruff:

```bash
uv run ruff check .
```

Automatically fix supported linting problems:

```bash
uv run ruff check --fix .
```

Format Python files:

```bash
uv run ruff format .
```

Check formatting without changing files:

```bash
uv run ruff format --check .
```

---

## Development and AI Tools

The project includes development instructions and AI-assisted development configuration.

Included tools and files:

- `.gitignore`
- `AGENTS.md`
- `pyproject.toml`
- OpenCode commands
- OpenCode skills
- OpenSpec specifications
- Ruff configuration
- Pytest configuration

OpenCode and OpenSpec were used to assist with:

- Feature planning
- Django implementation
- Specification management
- Testing
- Documentation
- Code quality checks

All generated or suggested code was reviewed and tested before being committed.

---

## Project Management

Development work is managed using:

- GitHub Issues
- Feature branches
- Issue-linked commits
- Pull Requests
- Code review comments
- Automated and manual testing

Example workflow:

```text
GitHub Issue
    ↓
Feature branch
    ↓
Implementation and tests
    ↓
Issue-linked commit
    ↓
Pull Request
    ↓
Code review
    ↓
Merge into main
```

Commit messages reference their related Issue number.

Example:

```text
Add reservation feature tests #18
```

Pull Requests link to Issues using:

```text
Closes #18
```

When the Pull Request is merged, the linked Issue is automatically closed.

---

## Version Control

The project uses Git and GitHub.

Typical feature workflow:

```bash
git checkout main
git pull origin main
git checkout -b issue-18-reservation-tests
```

After completing and testing the changes:

```bash
git add .
git commit -m "Add reservation feature tests #18"
git push -u origin issue-18-reservation-tests
```

A Pull Request is then opened from the feature branch into `main`.

---

## Security

The application uses Django security features including:

- CSRF protection
- Password hashing
- Session-based authentication
- Login-required views
- POST-based logout
- Server-side form validation

Production deployments should use:

- A secure secret key
- `DEBUG=False`
- HTTPS
- Appropriate allowed hosts
- A production database
- Secure cookie settings

---

## Author

Developed as part of the Web Engineering course.
