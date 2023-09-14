import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_accordion(driver):
    url = "https://automationtesting.co.uk/accordion.html"
    driver.get(url)
    radio = driver.find_element(By.XPATH, "//div[normalize-space()='Platform Portability']")

    if not radio.is_selected():
        radio.click()
 