import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()


def test_switch(driver):
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)
    main_window = driver.current_window_handle
    new = driver.find_element(By.XPATH,"//button[normalize-space()='New Browser Window']")
    new.click()
    time.sleep(5)
    window_handles=driver.window_handles
    if "Your_Store" in driver.page_source:
        print("Text 'Your_Store' found on the page.")
        print("Page Title:", driver.title)
    driver.switch_to.window(main_window)
    driver.quit()

