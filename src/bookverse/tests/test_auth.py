import pytest


@pytest.mark.anyio
async def test_register(client):
    r = await client.post(
        "/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert r.status_code == 200


@pytest.mark.anyio
async def test_login(client):
    await client.post(
        "/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    r = await client.post(
        "/login",
        data={
            "username": "test@example.com",
            "password": "password123"
        }
    )

    assert r.status_code == 200
    assert "access_token" in r.json()
