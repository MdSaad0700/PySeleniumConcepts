# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_kat():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    appoint = driver.find_element(By.ID, "btn-make-appointment")
    appoint.click()
    username = driver.find_element(By.ID, "txt-username")
    password = driver.find_element(By.ID, "txt-password")
    login = driver.find_element(By.ID, "btn-login")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")
    login.click()
    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Tokyo CURA Healthcare Center")
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicare").click()
    appdate = driver.find_element(By.ID, "txt_visit_date")
    appdate.send_keys("12/12/2023")
    driver.find_element(By.ID, "txt_comment").send_keys("I need appointment")
    driver.find_element(By.ID, "btn-book-appointment").click()
    time.sleep(5)
    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    #assert "Appointment Confirmation" == heading_h2.text
    print(heading_h2.text)
