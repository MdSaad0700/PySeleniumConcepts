# import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/b/PC-Desktops-All-In-One-Computers/179/bn_661752")
    see_all = driver.find_element(By.XPATH,
                                  "//section[contains(@class,'b-module b-carousel b-guidance b-display--landscape')]"
                                  "//span[contains(text(),'See All')]")
    see_all.click()
    element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'ABS Computer Technologies')]"))
    )
    element.click()
    apply = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Apply']"))
    )
    apply.click()
    headers=WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='45 Results']"))
    )
    print(headers.text)
