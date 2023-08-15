import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def testidrive():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    email = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    email.send_keys("augtest_040823@idrive.com")
    password.send_keys("123456")
    driver.find_element(By.ID, "frm-btn").click()
    time.sleep(15)
    driver.find_element(By.ID, "add-device-header-btn").click()
    time.sleep(5)
    download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button")
    download_btn.click()
    time.sleep(8)
