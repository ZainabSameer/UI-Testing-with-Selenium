def is_valid_recipe_name(name: str) -> bool:
    return bool(name.strip()) and name.isalpha()