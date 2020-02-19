from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_search_example(driver, wait):
    driver.get('https://deckshop.pro')
    driver.find_element(By.ID, 'smartSearch').send_keys('ram' + Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='smartResponse']//a[text()='Best decks']"))).click()
    header = driver.find_element(By.XPATH, "//*[text()='Best Clash Royale decks']")
    assert header.is_displayed()
