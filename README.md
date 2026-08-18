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