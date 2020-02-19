

def test_go_to_google(driver):
    driver.get('https://google.com')
    assert 'Google' in driver.title
