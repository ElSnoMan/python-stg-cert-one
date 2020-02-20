""" This is example will be using a CSV file.

However, you can store and get data from many sources like a database.
https://realpython.com is a great resource for learning Python,
but this is the link to working with CSV files:

https://realpython.com/python-csv/
"""
import csv
import pytest


people = []

# Read from my .csv file and turn each row into a dict
with open('test_challenge10.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        people.append(row)


# 'person' is the name of the variable
# people is the data source
@pytest.mark.parametrize('person', people)
def test_test_cases_example(person):
    """ This is a single test function.

    However, it will turn into a separate test case
    for each row in my CSV (each input).
    """
    assert person['name'].endswith('Smith')
