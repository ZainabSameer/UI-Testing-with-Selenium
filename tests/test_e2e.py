import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_recipe():
    driver = webdriver.Chrome()
    try:
        driver.get("http://127.0.0.1:8000/")
        driver.find_element(By.ID, "id").send_keys("123")
        driver.find_element(By.ID, "name").send_keys("Chocolate Cake")
        driver.find_element(By.ID, "ingredients").send_keys("chocolate, flour, eggs")

        driver.find_element(By.ID, "submit").click()


        WebDriverWait(driver, 10).until(
            lambda d: "Chocolate Cake" in d.find_element(By.ID, "recipe-list").text
        )

        time.sleep(1)

        assert "Chocolate Cake" in driver.find_element(By.ID, "recipe-list").text


    finally:
        driver.quit()


def test_invalid_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("http://127.0.0.1:8000/")


        driver.find_element(By.ID, "id").send_keys("100")

        driver.find_element(By.ID, "ingredients").send_keys("flour, sugar, eggs")

        driver.find_element(By.ID, "submit").click()

        WebDriverWait(driver, 10)


        recipe_list_text = driver.find_element(By.ID, "recipe-list").text
        assert "100" not in recipe_list_text 

    finally:
        driver.quit()


def test_delete_recipe():
    driver = webdriver.Chrome()
    try:
        driver.get("http://127.0.0.1:8000/")
        
        driver.find_element(By.ID, "id").send_keys("999")
        driver.find_element(By.ID, "name").send_keys("Test Delete Cake")
        driver.find_element(By.ID, "ingredients").send_keys("test, delete, ingredients")
        driver.find_element(By.ID, "submit").click()


        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "recipe-list"), "Test Delete Cake")
        )

        time.sleep(1) 

        list_items = driver.find_elements(By.CSS_SELECTOR, "#recipe-list li")
        target_li = None
        for li in list_items:
            if "Test Delete Cake" in li.text:
                target_li = li
                break

        assert target_li is not None, "Recipe not found in list."


        delete_button = target_li.find_element(By.CLASS_NAME, "delete-btn")
        delete_button.click()

        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert.accept()


        WebDriverWait(driver, 10).until_not(
            EC.text_to_be_present_in_element((By.ID, "recipe-list"), "Test Delete Cake")
        )

        assert "Test Delete Cake" not in driver.find_element(By.ID, "recipe-list").text

    finally:
        driver.quit()


def test_multiple_recipes_display():
    driver = webdriver.Chrome()
    try:
        driver.get("http://127.0.0.1:8000/")

        recipes = [
            {"id": "201", "name": "Pancakes", "ingredients": "flour, eggs, milk"},
            {"id": "202", "name": "Salad", "ingredients": "lettuce, tomato, cucumber"},
            {"id": "203", "name": "Soup", "ingredients": "chicken, carrots, onions"},
        ]

        for r in recipes:
            driver.find_element(By.ID, "id").clear()
            driver.find_element(By.ID, "id").send_keys(r["id"])
            driver.find_element(By.ID, "name").clear()
            driver.find_element(By.ID, "name").send_keys(r["name"])
            driver.find_element(By.ID, "ingredients").clear()
            driver.find_element(By.ID, "ingredients").send_keys(r["ingredients"])
            driver.find_element(By.ID, "submit").click()

            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.ID, "recipe-list"), r["name"])
            )


        list_text = driver.find_element(By.ID, "recipe-list").text
        for r in recipes:
            assert r["name"] in list_text

    finally:
        driver.quit()
