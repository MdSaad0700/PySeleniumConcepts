import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://app.vwo.com")

    email_add = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")

    submit_button = driver.find_element(By.ID, "js-login-btn")

    email_add.send_keys("93npu2yyb0@esiix.com")
    password.send_keys("Wingify@123")
    submit_button.click()

    time.sleep(5)
    assert "Dashboard" == driver.title
    print(driver.title)
