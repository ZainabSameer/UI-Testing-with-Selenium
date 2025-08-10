import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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




'''
def test_click_add_button_updates_list():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/recipes")  
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "id")))

    driver.find_element(By.NAME, "id").send_keys("301")
    driver.find_element(By.NAME, "name").send_keys("Strawberry Shake")
    driver.find_element(By.NAME, "ingredients").send_keys("strawberries, milk, sugar")
    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Strawberry Shake" in d.find_element(By.ID, "recipe-list").text
    )
    assert "Strawberry Shake" in driver.find_element(By.ID, "recipe-list").text
    driver.quit()






def test_form_submission_flow():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/app/static/index.html")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "id")))

    driver.find_element(By.NAME, "id").send_keys("302")
    driver.find_element(By.NAME, "name").send_keys("Apple Pie")
    driver.find_element(By.NAME, "ingredients").send_keys("apple, flour, cinnamon")
    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Apple Pie" in d.find_element(By.ID, "recipe-list").text
    )
    assert "Apple Pie" in driver.find_element(By.ID, "recipe-list").text
    driver.quit()


def test_scroll_to_recipe_list_section():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/app/static/index.html")

    recipe_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recipe-list"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", recipe_list)
    assert recipe_list.is_displayed()
    driver.quit()


def test_backend_data_loading():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/app/static/index.html")

    recipe_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recipe-list"))
    )

    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_element(By.ID, "recipe-list").text.strip()) > 0
    )
    assert len(recipe_list.text.strip()) > 0
    driver.quit()
    '''