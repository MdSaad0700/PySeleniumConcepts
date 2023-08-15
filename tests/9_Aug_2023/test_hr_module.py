import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_hr():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username.send_keys("admin")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("Hacker@4321")
    login = driver.find_element(By.XPATH, "//button[@type='submit']")
    login.click()
    time.sleep(5)
    add = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    add.click()
    time.sleep(10)
    firstname = driver.find_element(By.XPATH, "//input[@name='firstName']")
    firstname.send_keys("Mohammad Saad")
    middlename = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
    middlename.send_keys("Shakir")
    lastname = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    lastname.send_keys("Shaikh")
    eid = driver.find_element(*(By.XPATH,
                                "//div[@class='oxd-input-group oxd-input-field-bottom-space']"
                                "//div//input[@class='oxd-input oxd-input--active']"))
    eid.send_keys(700)
    time.sleep(10)
    save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    save.click()
