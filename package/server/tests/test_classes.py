import pytest

@pytest.mark.asyncio
async def test_create_class_requires_auth(client):
    response = await client.post("/classes", json={
        "name": "Yoga",
        "start_time": "2026-06-15T10:00:00Z",
        "instructor": "John",
        "available_slots": 5
    })

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_class_authenticated(client):
    await client.post("/signup", json={
        "name": "Admin",
        "email": "admin@example.com",
        "password": "password123"
    })

    login = await client.post("/login", data={
        "username": "admin@example.com",
        "password": "password123"
    })

    token = login.json()["access_token"]

    response = await client.post(
        "/classes",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "HIIT",
            "start_time": "2026-06-15T10:00:00Z",
            "instructor": "Jane",
            "available_slots": 3
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "HIIT"