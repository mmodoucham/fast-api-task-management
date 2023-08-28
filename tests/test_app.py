# app/test/test_tasks.py
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running ✅!"}


def test_create_task():
    response = client.post(
        "/api/tasks/",
        json={
            "id": 1,  # This will be ignored by the API
            "title": "Test",
            "description": "task",
            "dueDate": "2023-08-28T17:32:35.971Z",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == "success"
    assert data["response"]["title"] == "Test"


def test_get_all_tasks():
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "success"
    assert isinstance(data["response"], list)


def test_get_task_by_id():
    task_id = 2
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "success"
    assert data["response"]["id"] == task_id


def test_update_task():
    task_id = 3
    response = client.put(
        f"/api/tasks/{task_id}",
        json={
            "id": task_id,  # This will be ignored by the API
            "title": "Updated Task",
            "description": "Updated Task description",
            "dueDate": "2023-08-28T17:32:35.971Z",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "success"
    assert data["response"]["title"] == "Updated Task"


def test_delete_task():
    task_id = 5
    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200

    # Verify that the task doesnt exist anymore
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 404
