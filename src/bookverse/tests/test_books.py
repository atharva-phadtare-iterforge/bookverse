import pytest


@pytest.mark.anyio
async def test_books(client):
    r = await client.get("/books/")
    assert r.status_code == 200
