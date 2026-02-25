import pytest

@pytest.mark.asyncio
async def test_booking_flow(client):

    await client.post("/signup", json={
        "name": "User1",
        "email": "user1@example.com",
        "password": "password123"
    })

    login = await client.post("/login", data={
        "username": "user1@example.com",
        "password": "password123"
    })

    token = login.json()["access_token"]

    class_resp = await client.post(
        "/classes",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Zumba",
            "start_time": "2026-06-15T10:00:00Z",
            "instructor": "Trainer",
            "available_slots": 1
        }
    )

    class_id = class_resp.json()["id"]

    booking = await client.post(
        "/book",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "class_id": class_id,
            "client_name": "User1",
            "client_email": "user1@example.com"
        }
    )

    assert booking.status_code == 200

    overbook = await client.post(
        "/book",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "class_id": class_id,
            "client_name": "User1",
            "client_email": "user1@example.com"
        }
    )

    assert overbook.status_code == 400