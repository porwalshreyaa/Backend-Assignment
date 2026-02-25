import pytest

@pytest.mark.asyncio
async def test_signup(client):
    response = await client.post("/signup", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    })

    assert response.status_code == 200
    assert "id" in response.json()


@pytest.mark.asyncio
async def test_login(client):
    await client.post("/signup", json={
        "name": "Login User",
        "email": "login@example.com",
        "password": "password123"
    })

    response = await client.post("/login", data={
        "username": "login@example.com",
        "password": "password123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()