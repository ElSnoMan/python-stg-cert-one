import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    # driver = webdriver.Chrome('../venv/chromedriver-Darwin')  # use file path if chromedriver is NOT in your PATH
    driver = webdriver.Chrome()  # Use this if your chromedriver is in your PATH
    yield driver
    # code after yield is run After Each test
    driver.quit()
