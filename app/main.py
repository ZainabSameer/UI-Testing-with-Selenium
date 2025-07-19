from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Recipe App")

# 🧠 In-memory storage for recipes
recipes_db = []

# 📦 Recipe schema
class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]

# 🔍 List all recipes
@app.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes_db

# ➕ Add a new recipe
@app.post("/recipes", response_model=Recipe)
def add_recipe(recipe: Recipe):
    recipes_db.append(recipe)
    return recipe

# ❌ Delete a recipe by ID
@app.delete("/recipes/{id}", response_model=Recipe)
def delete_recipe(id: int):
    for r in recipes_db:
        if r.id == id:
            recipes_db.remove(r)
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")