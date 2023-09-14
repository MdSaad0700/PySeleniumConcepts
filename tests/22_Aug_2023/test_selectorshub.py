import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_selector(driver):
    url = "https://selectorshub.com/xpath-practice-page/"
    driver.get(url)
    driver.maximize_window()
    #js_ex = driver.execute_script
    # email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    # email.send_keys("saadshaikh@gmail.com")
    # time.sleep(5)
    # password = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    # password.send_keys("Wingfly@123")
    # company = driver.find_element(By.XPATH, "//input[@placeholder='Enter your company']")
    # company.send_keys("IBM")
    # submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
    # submit.click()
    div = driver.find_element(By.CSS_SELECTOR,
                              "div[class='elementor-element elementor-element-5c632b2 result"
                              " elementor-widget elementor-widget-html']"
                              " "
                              "div[class='elementor-widget-container']")
    driver.execute_script("arguments[0].scrollIntoView(true);", div)
    pass1 = driver.execute_script(
        "return document.querySelector('div.jackPart').shadowRoot.querySelector('a.learningHub');")
    driver.execute_script("arguments[0].click();", pass1)

    href = pass1.get_attribute("class")
    print(href)

