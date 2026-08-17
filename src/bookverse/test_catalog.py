import json
import pytest

from .catalog_store import (
    InvalidBookError,
    validate_book,
    load_catalog,
    save_catalog,
)


@pytest.fixture
def valid_book():
    return {
        "title": "Python Crash Course",
        "author": {"name": "Eric Matthes"},
        "price": 120,
        "stock": 5,
    }


def test_valid_book(valid_book):
    validate_book(valid_book)


def test_missing_title(valid_book):
    valid_book["title"] = ""

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


def test_missing_author(valid_book):
    valid_book["author"] = None

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


def test_negative_price(valid_book):
    valid_book["price"] = -10

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


def test_negative_stock(valid_book):
    valid_book["stock"] = -1

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


@pytest.mark.parametrize("price", [0, -1, -100])
def test_invalid_prices(valid_book, price):
    valid_book["price"] = price

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


@pytest.mark.parametrize("stock", [-1, -5, -10])
def test_invalid_stock(valid_book, stock):
    valid_book["stock"] = stock

    with pytest.raises(InvalidBookError):
        validate_book(valid_book)


def test_load_invalid_catalog(tmp_path, monkeypatch, valid_book):
    valid_book["title"] = ""

    file = tmp_path / "books.json"
    file.write_text(json.dumps([valid_book]))
    monkeypatch.chdir(tmp_path)

    with pytest.raises(InvalidBookError):
        load_catalog()


def test_save_catalog(tmp_path, monkeypatch, valid_book):
    file = tmp_path / "books.json"
    file.write_text(json.dumps([valid_book]))
    monkeypatch.chdir(tmp_path)

    save_catalog()

    with open("books.json") as f:
        books = json.load(f)

    assert len(books) == 2
    assert books[1]["title"] == "ABC"
    assert books[1]["price"] == 29
    assert books[1]["stock"] == 11