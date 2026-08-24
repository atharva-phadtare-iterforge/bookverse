import pytest


@pytest.mark.anyio
async def test_bad_token(client):
    r = await client.post(
        "/orders",
        headers={"Authorization": "Bearer bad-token"},
        json={"items": [{"book_id": 1, "quantity": 1}]},
    )

    assert r.status_code == 401


@pytest.mark.anyio
async def test_create_order(order_client):
    client, book = order_client

    r = await client.post(
        "/orders",
        json={
            "items": [
                {
                    "book_id": book.id,
                    "quantity": 2,
                }
            ]
        },
    )

    assert r.status_code == 200
    assert r.json()["status"] == "Created"


@pytest.mark.anyio
async def test_insufficient_stock(order_client):
    client, book = order_client

    r = await client.post(
        "/orders",
        json={
            "items": [
                {
                    "book_id": book.id,
                    "quantity": 999,
                }
            ]
        },
    )

    assert r.status_code == 400
