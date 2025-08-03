from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_add_recipe():
    new_recipe = {
        "id": 101,
        "name": "Banana Pancakes",
        "ingredients": ["banana", "flour", "eggs"]
    }
    response = client.post("/recipes", json=new_recipe)
    assert response.status_code == 200

    get_response = client.get("/recipes")
    assert get_response.status_code == 200
    recipes = get_response.json()

    names = [r["name"] for r in recipes]
    assert "Banana Pancakes" in names