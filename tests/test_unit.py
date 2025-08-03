import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import is_valid_recipe_name

def test_valid_name():
    assert is_valid_recipe_name("Tiramisu") is True

def test_empty_name():
    assert is_valid_recipe_name("   ") is False

def test_name_with_numbers():
    assert is_valid_recipe_name("Cake123") is False