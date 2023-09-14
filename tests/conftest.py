import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def setup1(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def setup2(request):
    driver = webdriver.Safari()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()



