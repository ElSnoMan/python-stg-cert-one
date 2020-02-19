import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    # driver = webdriver.Chrome('../venv/chromedriver-Darwin')  # use file path if chromedriver is NOT in your PATH
    driver = webdriver.Chrome()  # Use this if your chromedriver is in your PATH
    yield driver
    # code after yield is run After Each test
    driver.quit()


@pytest.fixture
def wait(driver):
    """ WebDriverWait allows us to wait until a condition is True.

    For example, wait until an element is displayed
    """
    # timeout is the max number of seconds to wait for.
    return WebDriverWait(driver, timeout=10)
