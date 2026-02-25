import pytest

@pytest.mark.asyncio
async def test_get_my_bookings(client):

    await client.post("/signup", json={
        "name": "BookUser",
        "email": "book@example.com",
        "password": "password123"
    })

    login = await client.post("/login", data={
        "username": "book@example.com",
        "password": "password123"
    })

    token = login.json()["access_token"]

    response = await client.get(
        "/bookings",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)