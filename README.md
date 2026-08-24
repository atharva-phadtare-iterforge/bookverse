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


## **Status:** Day 0 — Project Setup
- Set up `uv`, Python 3.12, Git, GitHub, VS Code, Docker, and PostgreSQL.
- Created the project using `uv init` and `uv venv`.
- Created the GitHub repository and initial README.

## Day 1: Python Core
- Reviewed comprehensions, slicing, f-strings, functions, and control flow.
- Created `data_structures.py` for filtering and sorting books.
- Practiced `*args`, `**kwargs`, and formatted reports.

## Day 2: OOP
- Practiced classes, dataclasses, type hints, inheritance, and `super()`.
- Created `models_plain.py` with `Book`, `Author`, and `Order`.
- Implemented `total_price()`, `__str__()`, and `__repr__()`.

## Day 3: Errors, Files & Logging
- Learned exception handling and custom `InvalidBookError`.
- Implemented JSON catalog loading, saving, and validation.
- Practiced logging validation errors to a file.

## Day 4: uv & Pydantic
- Practiced `uv add`, `uv remove`, `uv run`, `uv lock`, and `pyproject.toml`.
- Reviewed the Python `src` project structure.
- Started learning Pydantic v2, `BaseModel`, and field validation.

## Day 5: HTTP, Requests, HTTPX & Asyncio

- Learned `requests` for API calls.
- Practiced `asyncio` and `httpx` for async requests.
- Created `seed_data.py`.
- Fetched books from Open Library API.
- Mapped API data to Pydantic schemas.
- Saved books to `books.json`.
- Compared sync and async approaches.

## Day 6: Git & Testing

- Reviewed Git branches, commits, and `.gitignore`.
- Created `test_catalog.py`.
- Learned pytest fixtures, assertions, and `parametrize`.
- Added tests for validation and catalog functionality.
- Ran the full pytest suite successfully.

## Day 7: Week 1 Checkpoint

- Created `cli.py` using `argparse`.
- Implemented `add`, `list`, `search`, and `delete`.
- Connected CLI with Pydantic schemas and catalog store.
- Tested all CLI commands.
- Updated README with CLI usage.
- Ran the full pytest suite.

## Day 8: FastAPI

- Added FastAPI and Uvicorn.
- Created `main.py`.
- Implemented `GET`, `POST`, `PUT`, and `DELETE` `/books` endpoints.
- Practiced path parameters and request bodies.
- Verified endpoints using `/docs`.

## Day 9: FastAPI Structure & DI

- Added APIRouter and organized the project structure.
- Moved book endpoints to `routers/books.py`.
- Added BaseSettings with .env configuration.
- Added a global exception handler with consistent error JSON.
- Verified all endpoints using `/docs`.

## Day 10: PostgreSQL & Relational Schema
- Installed and started PostgreSQL locally/via Docker.
- Reviewed `psql` basics, constraints, primary/foreign keys, and basic indexing.
- Hand-wrote the relational schema in `psql` for `books`, `authors`, `users`, `orders`, and `order_items`.
- Manually inserted sample data into each table.
- Wrote and verified 10 practice queries (joins, aggregates, and filters) and saved them in `queries.sql`.

## Day 11: SQLAlchemy ORM & Alembic
- Added `sqlalchemy`, `alembic`, and `psycopg2-binary` as dependencies.
- Mapped Day 10's relational schema to SQLAlchemy 2.0 declarative models in `models.py`.
- Initialized Alembic and configured it to point to the PostgreSQL database.
- Generated and executed the initial migration via `alembic revision --autogenerate` and `alembic upgrade head`.
- Wired FastAPI to PostgreSQL using a database session dependency.
- Wrote a one-off `migrate_json_to_db.py` script to seed `books.json` into the new tables and verified via `psql`.

## Day 12: Async DB Access & Auth
- Configured async SQLAlchemy with `asyncpg` for non-blocking database operations.
- Implemented password hashing using `passlib` and JWT creation/verification utilities.
- Implemented `POST /register` to store hashed passwords securely.
- Implemented `POST /login` to verify credentials and issue JWT tokens.
- Added `OAuth2PasswordBearer` dependency to protect secure routes.
- Implemented authenticated `POST /orders` endpoint that creates orders, adds order items, and decrements book stock atomically.

## Day 13: Testing & Docker
- Configured `pytest` with `httpx.AsyncClient` targeting an isolated test database.
- Wrote a comprehensive pytest suite covering books, auth, and orders.
- Created a production-ready `Dockerfile` for the FastAPI application.
- Created `docker-compose.yml` to orchestrate the FastAPI app and PostgreSQL together.
- Confirmed end-to-end functionality using `docker-compose up`.

## Day 14: Capstone Demo Day
- Implemented bonus `POST /books/{id}/reviews` endpoint for ratings and comments.
- Added `GET /orders/me` for authenticated user order history.
- Finalized documentation, setup steps, architecture overview, and endpoint lists in `README.md`.
- Tagged the `v1.0` release on GitHub.
- Prepared and completed the live walkthrough (`/docs`, registration, login, browsing, ordering, and reviews).

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