from pprint import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_if_else(driver, wait):
    driver.get('https://deckshop.pro')
    driver.find_element(By.ID, 'smartSearch').send_keys('ram' + Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='smartResponse']//a[text()='Best decks']"))).click()

    # In this example, I want to count the number of decks that have certain cards
    card_occurrences = {
        'Battle Healer': 0,
        'P.E.K.K.A': 0,
        'Bandit': 0,
        'Ice Golem': 0,
        'Royal Ghost': 0,
        'Misc': 0
    }

    cards = driver.find_elements(By.CSS_SELECTOR, 'img.cr-card')
    for card in cards:
        name = card.get_attribute('alt')
        if name in card_occurrences.keys():
            card_occurrences[name] += 1
        else:
            card_occurrences['Misc'] += 1

    print()  # spacer to make output better
    pprint(card_occurrences)  # pprint (short for pretty print) prints dict/json in a prettier format
