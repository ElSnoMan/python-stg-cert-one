from selenium.webdriver.common.by import By


def test_loop_example(driver):
    driver.get('https://deckshop.pro')
    deck = driver.find_element(By.XPATH, "//a[contains(@href, '/deck/detail') and not(@class)]")
    cards = deck.find_elements(By.TAG_NAME, "img")
    assert len(cards) == 8  # there can only be 8 cards in a Clash Royale deck
    print()  # spacer so the print looks prettier

    for card in cards:
        alt_text = card.get_attribute('alt')
        source = card.get_attribute('src')
        print(f'{alt_text} - {source}')
