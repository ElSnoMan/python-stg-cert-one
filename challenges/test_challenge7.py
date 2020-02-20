from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_list_dict_example(driver, wait):
    driver.get('https://deckshop.pro')
    driver.find_element(By.XPATH, "//a[@class='nav-link' and @href='/card/']").click()
    training_camp_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='list-of-cards']")))
    cards = training_camp_section.find_elements(By.TAG_NAME, "a")
    cards_with_urls = []

    for card in cards:
        name = card.find_element(By.TAG_NAME, 'img').get_attribute('alt')
        url = card.get_attribute('href')
        cards_with_urls.append([name, url])

    print()  # spacer
    for card in cards_with_urls:
        name = card[0]
        url = card[1]
        driver.get(url)
        wait.until(lambda _: name in driver.find_element(By.CSS_SELECTOR, "h2[class$='detail-card']").text)
        print(f'{card} PASSED')
