# EduTrack API

A RESTful API for managing students, courses, and enrollments built with FastAPI and SQLAlchemy.

## Features

- JWT-based authentication with role-based access control (student / admin)
- User registration and login
- Course management (create, update, activate/deactivate)
- Student enrollment and deregistration
- UUID primary keys across all models

## Tech Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Migrations:** Alembic
- **Auth:** JWT (python-jose / PyJWT)
- **Validation:** Pydantic v2
- **Server:** Uvicorn

## Project Structure

```
app/
├── api/
│   ├── deps.py               # Auth dependencies
│   └── v1/
│       ├── auth.py           # Signup & login
│       ├── user.py           # User profile
│       ├── course.py         # Course endpoints
│       └── enrollment.py     # Enrollment endpoints
├── core/
│   ├── config.py             # App settings
│   └── security.py           # Password hashing, JWT
├── db/
│   ├── base.py               # SQLAlchemy Base
│   └── session.py            # DB engine & session
├── models/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── schemas/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── services/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── tests/
│   ├── test_users.py
│   └── test_courses.py
└── main.py
```

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL

### Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd Edutrack_App
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/edutrack
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
```

5. Run database migrations:

```bash
alembic upgrade head
```

6. Start the server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs: `http://127.0.0.1:8000/docs`

## API Endpoints

### Auth

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| POST | `/api/v1/signup` | Register a new user | Public |
| POST | `/api/v1/login` | Login and get access token | Public |

### Users

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/api/v1/users/me` | Get current user profile | Student |

### Courses

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/api/v1/courses` | List all active courses | Public |
| GET | `/api/v1/courses/{id}` | Get a course by ID | Public |
| POST | `/api/v1/courses` | Create a course | Admin |
| PUT | `/api/v1/courses/{id}` | Update a course | Admin |
| PATCH | `/api/v1/courses/{id}` | Activate or deactivate a course | Admin |

### Enrollments

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| POST | `/api/v1/enrollments` | Enroll in a course | Student |
| GET | `/api/v1/enrollments` | List all enrollments | Admin |
| GET | `/api/v1/enrollments/by-course/{id}` | List enrollments for a course | Admin |
| DELETE | `/api/v1/enrollments/course/{id}` | Deregister from a course | Student |

## Roles

| Role | Permissions |
|------|-------------|
| `student` | View courses, enroll/deregister, view own profile |
| `admin` | All student permissions + manage courses, view all enrollments |

## Running Tests

```bash
pytest app/tests/ -v
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key for JWT signing |
| `ALGORITHM` | JWT algorithm (e.g. `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry duration in minutes |
