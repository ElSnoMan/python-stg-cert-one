import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    driver = webdriver.Chrome('../venv/chromedriver-Darwin')
    yield driver
    # code after yield is run After Each test
    driver.quit()
