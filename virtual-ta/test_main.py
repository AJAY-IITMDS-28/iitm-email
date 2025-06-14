from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_gpt_model_question():
    response = client.post("/api/", json={
        "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?"
    })
    assert response.status_code == 200
    data = response.json()
    assert "gpt-3.5-turbo-0125" in data["answer"]
    assert isinstance(data["links"], list)
    assert any("discourse.onlinedegree.iitm.ac.in" in link["url"] for link in data["links"])

def test_no_answer():
    response = client.post("/api/", json={
        "question": "What is the weather today?"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["answer"].startswith("Sorry")
    assert data["links"] == []
