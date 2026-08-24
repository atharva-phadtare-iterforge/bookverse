import os

os.environ["DATABASE_URL"] = (
    "postgresql+psycopg2://postgres:123456@localhost:5432/bookverse_test"
)

import pytest
from httpx import ASGITransport, AsyncClient

from bookverse.main import app
from bookverse.db.db import engine, get_db
from bookverse.models.models import Base, User, Author, Book
from bookverse.core.config import get_current_user


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture
async def order_client():
    db = next(get_db())

    user = User(
        email="order@test.com",
        hashed_password="password",
    )
    db.add(user)

    author = Author(name="Eric Matthes")
    db.add(author)
    db.flush()

    book = Book(
        title="Python Crash Course",
        isbn=123456789,
        price=120,
        stock=5,
        author_id=author.id,
    )
    db.add(book)
    db.commit()
    db.refresh(user)
    db.refresh(book)

    async def current_user():
        return user

    app.dependency_overrides[get_current_user] = current_user

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client, book

    app.dependency_overrides.clear()
    db.close()
