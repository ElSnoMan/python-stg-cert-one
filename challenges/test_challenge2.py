from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search_example(driver):
    driver.get('https://deckshop.pro')
    driver.find_element(By.ID, 'smartSearch').send_keys('ram' + Keys.ENTER)
    driver.find_element(By.XPATH, "//a[text()='Best decks']").click()
    header = driver.find_element(By.XPATH, "//*[text()='Best Clash Royale decks']")
    assert header.is_displayed()
