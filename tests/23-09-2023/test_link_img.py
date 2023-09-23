import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSauce:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_login(self, driver):

        url = "https://www.saucedemo.com/"

        driver.get(url)
        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username.send_keys("standard_user")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("secret_sauce")
        submit = driver.find_element(By.XPATH, "//input[@id='login-button']")
        submit.click()
        time.sleep(5)

    def test_link_img(self, driver):
        self.test_login(driver)
        url = "https://www.saucedemo.com/inventory.html"
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        images = driver.find_elements(By.TAG_NAME, "img")

        broken_links = []
        valid_links = []
        broken_images = []
        valid_images = []

        for link in links:
            url = link.get_attribute("href")
            if url and url.startswith("http"):
                response = requests.head(url)
                # time.sleep(1)
                if response.status_code != 200:
                    broken_links.append(url)
                # print(f"Broken link:-{url} , Status Code:- {response.status_code}")
                else:
                    valid_links.append(url)
        for image in images:
            src = image.get_attribute("src")
            if src and src.startswith("http"):
                response = requests.head(src)
                if response.status_code != 200:
                    broken_images.append(src)
                    # print(f"Broken Image:-{src} , Status Code:- {response.status_code}")
                else:
                    valid_images.append(src)
        print("Broken Links:")
        for link in broken_links:
            response = requests.head(link)
            print(f"{link} (Status Code: {response.status_code})")

        print("\nValid Links:")
        for link in valid_links:
            response = requests.head(link)
            print(f"{link} (Status Code: {response.status_code})")

        print("\nBroken Images:")
        for image in broken_images:
            response = requests.head(image)
            print(f"{image} (Status Code: {response.status_code})")

        print("\nValid Images:")
        for image in valid_images:
            response = requests.head(image)
            print(f"{image} (Status Code: {response.status_code})")

        driver.quit()
