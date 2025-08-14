from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
from typing import List

app = FastAPI(title="Recipe App")

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

recipes_db: List["Recipe"] = []

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = STATIC_DIR / "index.html"
    return html_path.read_text()

@app.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes_db

@app.post("/recipes", response_model=Recipe)
def add_recipe(recipe: Recipe):
    print("Recipe received:", recipe.dict())
    recipes_db.append(recipe)
    return recipe


@app.delete("/recipes/{id}", response_model=Recipe)
def delete_recipe(id: int):
    for r in recipes_db:
        if r.id == id:
            recipes_db.remove(r)
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")
