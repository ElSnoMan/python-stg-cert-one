from pprint import pprint
import requests


API_URL = 'https://deckofcardsapi.com/api/deck'


def test_REST_example():
    """ Work with RESTful APIs.

    API Documentation: http://deckofcardsapi.com/
    """
    new_deck_payload = {
        'jokers_enabled': False
    }

    # create a new deck without Jokers
    new_deck_response = requests.get(f'{API_URL}/new/', data=new_deck_payload)
    deck = new_deck_response.json()
    assert deck['remaining'] == 52  # without Jokers, a standard deck should be 52 cards
    assert deck['shuffled'] is False

    # shuffle the deck
    deck_id = deck['deck_id']
    shuffle_response = requests.get(f'{API_URL}/{deck_id}/shuffle/').json()
    assert shuffle_response['shuffled'] is True

    print()  # spacer
    pprint(deck)
    pprint(shuffle_response)
