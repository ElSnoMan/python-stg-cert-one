import requests


API_URL = 'https://deckofcardsapi.com/api/deck'


def test_check_Types_example():
    """ test_challenge7.py has good examples working with JSON (or `dict` in Python) """
    new_deck_response = requests.get(f'{API_URL}/new/')
    deck = new_deck_response.json()

    # `isinstance()` is used to check Types
    assert isinstance(deck['deck_id'], str)
    assert isinstance(deck['shuffled'], bool)
