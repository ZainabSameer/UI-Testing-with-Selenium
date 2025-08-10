from fastapi.testclient import TestClient
from app.main import app, recipes_db 
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    recipes_db.clear()

def test_get_recipes_empty():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert response.json() == []

def test_post_recipe():
    recipe = {
        "id": 1,
        "name": "Spaghetti Carbonara",
        "ingredients": ["spaghetti", "eggs", "bacon", "parmesan"]
    }
    response = client.post("/recipes", json=recipe)
    assert response.status_code == 200
    assert response.json()["name"] == "Spaghetti Carbonara"

def test_delete_recipe():
    client.post("/recipes", json={
        "id": 2,
        "name": "Tacos",
        "ingredients": ["tortilla", "beef", "cheese", "lettuce"]
    })

    response = client.delete("/recipes/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Tacos"