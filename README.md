# BookVerse

BookVerse is a REST API for an online bookstore.

## Features

- Browse books and authors
- User registration and login
- Place orders
- Manage book stock
- Leave book reviews

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- pytest
- Docker
- Git & GitHub

## Running the Project with Docker

### Prerequisites

Make sure Docker Desktop is installed and running.

### 1. Pull the PostgreSQL Image

```powershell
docker compose pull db
```

### 2. Build and Start the Containers

```powershell
docker compose up -d --build
```

### 3. Check Container Status

```powershell
docker compose ps
```

### 4. Run Database Migrations

```powershell
docker compose exec app /app/.venv/bin/alembic upgrade head
```

### 5. Seed the Database

```powershell
docker compose exec -T db psql -U postgres -d bookverse -f /docker/seed.sql
```

### 6. Run Tests

```powershell
docker compose exec app /app/.venv/bin/pytest -v
```

### 7. Access the API

The API is available at:
```powershell
http://localhost:8000
```

##  Full API Endpoint List

### General
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | API health and welcome message | No |

### Books & Reviews
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **GET** | `/books/` | List all books (with filtering options) | No |
| **GET** | `/books/{book_id}` | Get a specific book by ID | No |
| **POST** | `/books/` | Create a new book entry | No |
| **PUT** | `/books/{book_id}` | Update an existing book | No |
| **DELETE** | `/books/{book_id}` | Delete a book | No |
| **POST** | `/books/{book_id}/reviews` | Add a rating and comment to a book | Yes (`Bearer Token`) |

### Authentication & Users
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **POST** | `/register` | Register a new user account | No |
| **POST** | `/login` | Authenticate credentials and issue JWT | No |

### Orders
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **POST** | `/orders` | Place a new order (decrements stock) | Yes (`Bearer Token`) |
| **GET** | `/orders/me` | Get the authenticated user's order history | Yes (`Bearer Token`) |