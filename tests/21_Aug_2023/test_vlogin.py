# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# def test_app_vwo(driver):
#     url = "https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1"
#     driver.get(url)
#     driver.maximize_window()
#     # variation=driver.find_element(By.CSS_SELECTOR,"[data-qa='meqeqiwiwe']")
#     # time.sleep(5)
#     #
#     # action=ActionChains(driver)
#     # action.move_to_element(variation).click().perform()
#     # time.sleep(5)
# from faker import Faker
#
#
# faker = Faker()
#
# print(f"{faker.name()}")
# print(f"{faker.first_name()}")
# print(f"{faker.middle_name()}")
# print(f"{faker.last_name()}")
# print(f"{faker.password()}")
