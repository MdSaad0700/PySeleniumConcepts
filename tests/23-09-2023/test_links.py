import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_link(driver):
    url = "https://selectorshub.com/xpath-practice-page/"
    driver.get(url)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.get_attribute("href")
        if url and url.startswith("http"):
            response = requests.head(url)
            time.sleep(1)
            if response.status_code != 200:
                print(f"Broken link:-{url} , Status Code:- {response.status_code}")
            else:
                print("Okay")
    driver.quit()

# def test_ec(driver):
#     url = "https://selectorshub.com/xpath-practice-page/"
#     driver.get(url)
#     link_elements = driver.find_elements(By.TAG_NAME, "a")
#
#     for link_element in link_elements:
#         original_window = driver.current_window_handle
#         link_url = link_element.get_attribute("href")
#         driver.execute_script(f"window.open('{link_url}', '_blank');")
#         driver.switch_to.window(driver.window_handles[-1])
#         driver.get(link_url)
#         # driver.switch_to.window(original_window)
#     driver.quit()
#

# def test_se(driver):
#     driver.get("https://selectorshub.com/xpath-practice-page/")
#     link_elements = driver.find_elements(By.TAG_NAME, "a")
#     for link_element in link_elements:
#         link_url = link_element.get_attribute("href")
#
#         driver.execute_script(f"window.open('{link_url}', '_blank');")
#         time.sleep(2)
#         # driver.switch_to.window(driver.window_handles)
#
#         driver.switch_to.window(driver.window_handles[-1])
#         driver.get(link_url)
#         # driver.switch_to.window(driver.window_handles[0])
#     driver.quit()

#
# def test_ec(driver):
#     url = "https://selectorshub.com/xpath-practice-page/"
#     driver.get(url)
#     link_elements = driver.find_elements(By.TAG_NAME, "a")
#
#     # Get the original window handle
#     original_window = driver.current_window_handle
#
#     for link_element in link_elements:
#         link_url = link_element.get_attribute("href")
#
#         # Open a new tab
#         driver.execute_script(f"window.open('{link_url}', '_blank');")
#
#         # Switch to the new tab
#         driver.switch_to.window(driver.window_handles[-1])
#
#         driver.switch_to.window(original_window)
#
#     driver.quit()
