import pytest
from selenium import webdriver
import time


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser


def test_vist_facebook(browser):
    browser.get("https://www.facebook.com/")
    # print(browser.title)
    time.sleep(5)
    assert "Facebook – log in or sign up" == browser.title

