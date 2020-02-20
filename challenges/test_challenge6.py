from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_try_except_example(driver, wait):
    driver.get('https://deckshop.pro')
    driver.find_element(By.CSS_SELECTOR, "a[href='https://spy.deckshop.pro/']").click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Top 10 Players')))

    try:
        # Check that the first place player is Carlos Kidman
        driver.find_element(By.XPATH, "//a[contains(@href, '/player') and text()='Carlos Kidman']")
    except NoSuchElementException or BaseException as error:
        # `NoSuchElementException` is raised if driver can't find the element.
        # For now, we'll also catch BaseException which will catch any and all exceptions.
        # This is just so you can see the syntax in case you don't know the exact Exception to catch.

        # `except` is the keyword to "catch" these errors so we can do something with it.
        # `as error` holds the exception in a variable.

        # In this case, we will:
        #     1. take a screenshot
        #     2. re-raise the error so the test fails
        driver.save_screenshot('test_challenge6_player_not_found.png')
        raise error
