from selenium import webdriver
import time


def test_chrome():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.google.com/")
    time.sleep(5)
    # print(driver.title)
    assert "Google" == driver.title
