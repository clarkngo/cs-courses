import pytest
from todo_app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Buy milk"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Buy milk"
    assert data["completed"] is False

def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")
    tasks = response.get_json()

    assert len(tasks) == 2

def test_complete_task(client):
    create = client.post("/tasks", json={"title": "Do homework"})
    task_id = create.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}")
    assert response.get_json()["completed"] is True