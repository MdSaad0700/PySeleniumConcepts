# import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/b/PC-Desktops-All-In-One-Computers/179/bn_661752")

    inputbox = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    inputbox.send_keys("ABS Computer Technologies")
    search = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='gh-btn']"))
    )
    search.click()
    result = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='clearfix srp-controls__row-2']//h1"))
    )
    ebay_items_list = driver.find_elements(By.XPATH, "//div[@class='srp-river srp-layout-inner']//li//a")
    items_list = []
    for item_list in ebay_items_list:
        items_list.append(item_list.text)

    print(items_list)
    print(len(items_list))

    # ebay_item_list = driver.find_element(By.XPATH, "//div[@class='srp-river srp-layout-inner']//li//a")
    # item_list = []
    # for item_list in ebay_item_list:
    #     item_list.append(item_list.text)
    # print(item_list)
    # print(item_list.text)
    print(result.text)

    # see_all = driver.find_element(By.XPATH,
    #                               "//section[contains(@class,'b-module b-carousel b-guidance b-display--landscape')]"
    #                               "//span[contains(text(),'See All')]")
    # see_all.click()
    # element = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'ABS Computer Technologies')]"))
    # )
    # element.click()
    # apply = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Apply']"))
    # )

    # apply.click()
    # headers = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='clearfix']//h2"))
    # )
    # print(headers.get_attribute('textContent'))
    # time.sleep(5)
