# Python WebDriver STG Certification: Level 1 & 2

## Overview
This certification is meant to introduce you to Python and Selenium for testing (UI & API) and automation.

To get started and follow along, make sure to setup your machine and project to use Python. You can do this by following the instructions for our standardized setup in this google doc:

[Machine and Project Setup](https://docs.google.com/document/d/1kT83D6PEf_x3U7z1TRD33dPOJ_z9JjZ7PZWdaIOLyMs/edit?usp=sharing)

## GOALS

* Each challenge will introduce different concepts.
* Complete each challenge and push your code to GitHub so the instructor(s) can validate.
* Completing all challenges will get you this certification!
* The student is familiar enough with Python, Selenium and Pytest that they can begin automating tests and solving problems.

## QUESTIONS?

The best place to ask questions is the **#autobots** channel in our **QA Utah Slack group** which you can join by going to https://qap.dev/autobots. Otherwise, feel free to reach out to the instructors:

* Matt Chiang
* Carlos Kidman

## HOW TO USE THIS REPO

This README will contain the high-level overview and requirements for each challenge. However, make sure to checkout the Wiki which will contain more specific details and information about each challenge, if applicable.

Also, you will have access to the code base which will provide structure and examples so you can have a reference.

## LEVEL 1 CHALLENGES

### Pre-Challenge: Setup Selenium

Complete the `Start Here` section of the Wiki to get everything setup: [Wiki Home Page](https://github.com/ElSnoMan/python-stg-cert-one/wiki)

Now you are ready to take on the challenges!

### Challenge 1
---

Within `test_challenge1.py`, write a new test that does the following:

1. Go to google.com
2. Search for “puppies”
3. Assert that the results page that loads has “puppies” in its title

### Challenge 2
---

Create `test_challenge2.py` and write a test that does the following:

1. Go to copart.com
2. Search for "exotics"
3. Assert "PORSCHE" is in the list of cars on the Results Page

### Challenge 3
---

Create `test_challenge3.py` and write a test that does the following:

1. Go to copart.com
2. On the Home Page, under `Most Popular Items`, there is a `Makes/Models` section. For each Make or Model in this section, print the name of the Make or Model with its URL (aka `href`) next to it

> Example Output: `SILVERADO - https://www.copart.com/popular/model/silverado`

### Challenge 4
---

Fibonacci (recursion)

Create `test_challenge4.py` and write a test that does the following:

1. Displays the fibonnaci sequence for N numbers
2. However, print the number(s) as English words

> Example: If the sequence is `18`, then print `"Eighteen"`

> Example: If the seqence is `120`, then print `"One Hundred Twenty"`

### Challenge 5
---

Part 1 - Create `test_challenge5.py` and write a test that does the following:

1. Go to copart.com
2. Search for "porsche"
3. Change `Show Entries` to 100
4. Print the number of occurrences for each Model

> Example: There might be x3 `PANAMERA T` and x11 `CAYENNE`

Part 2 - Using the same, first three steps of Part 1, write a test that then does the following:

1. Count the number of occurrences of each Damage type
2. However, you need to map the Damage types to these:

* REAR END
* FRONT END
* MINOR DENT/SCRATCHES
* UNDERCARRIAGE

3. Any Damage type that does NOT match the above types should be grouped into a `MISC` Damage type

> Example: `SIDE` and `ALL OVER` would each count towards `MISC`

> Example Output: `REAR END: 2, FRONT END: 7, MINOR DENT/SCRATCHES: 22, UNDERCARRIAGE: 0, MISC: 4`

### Challenge 6
---

Create `test_challenge6.py` and write a test that does the following:

1. Go to copart.com
2. Search for 'nissan'
3. Then for the Model, search 'skyline'. This is a rare car that might not exist
4. If it doesn't exist, catch the exception and take a screenshot

### Challenge 7
---

Create `test_challenge7.py` and write a test that does the following:

1. Go to copart.com
2. Look at the `Makes/Models` section of the page
3. Create a `two-dimensional` list that stores the names of the Make/Model as well as their URLs
4. Check that each element in this list navigates to the correct page

### Level 1 Complete!

1. Push all of your completed code to your repo
2. Notify `Matt Chiang` or `Carlos Kidman`
3. Code Review will be done
4. Complete any requests that are given from review
5. Once the challenges are signed off, you will receive the certification!


## LEVEL 2 CHALLENGES

### Setup to work with HTTP Clients

Now that you have done some work in Python and Selenium, we are going to go level deeper and work with RESTful APIs and data. We will use a library called `requests` to make working with these APIs easier.

1. Open the Terminal in PyCharm
2. Install `requests`

```bash
$ pip install requests
```

3. All set! You can now `import requests`

### Challenge 8
---

The API Endpoint
https://www.copart.com/public/lots/search

Create `test_challenge8.py` and write a test that does the following:

1. Using the above endpoint, search for `Toyota Camry` and print the results
2. Do this for 9 other cars that you like. ('Nissan Maxima', etc.) 

### Challenge 9
---

> This is an extension of Challenge 8.

Create `test_challenge9.py` and write a test that does the following:

1. Uses the same response as Challenge 8, but write assertions about elements in the JSON response
2. Part of your test(s) needs to assert that those elements are of the correct Type.

> Example, "lotNumberStr" should be a String

### Challenge 10
---

> This is also an extension of Challenge 8.

Create `test_challenge10.py` and write a test that does the following:

1. You will be reading data from an Excel Spreadsheet or CSV file.
2. Depending on the columns and rows of data, you will generate test cases from this

For example, you may have a data table that looks like this:

```
   |     MAKE     |     MODEL     |     YEAR      
___|_____________________________________________
1  |    toyota    |               |
2  |              |     camry     |
3  |              |               |     1997
4  |    toyota    |     avalon    |     2018
```

In that case, you would have a single test function that had 4 separate test cases.
You would only need to switch out the `make`, `model` and `year` variables with the data from this table.

> HINT: Pytest's `@pytest.mark.parameratize` decorator will be helpful once you have read the data from the file.

### Challenge 11
---

Create `test_challenge11.py`.

1. Write a webcrawler that will navigate to every page on copart.com

> Don't worry about crawling all of the data for now because we don't want to seem like we're doing a DOS Attack

### Challenge 12
---

This is the final challenge for the Level 2 Certification.

This challenge will act as sort of a "Master Thesis" meaning that you need to do your own research and build your own solution.

### Acceptance Criteria

1. Create a mechanism to automatically trigger your tests
2. Hook your tests to a reporting framework

### Continuous Testing

Part 1 of this challenge is to automatically trigger your tests. There are so many ways to do this, but to give you some help as to the tools that are out there, here's a list of possible options (remember, there are more):

* Jenkins
* TeamCity
* Bamboo
* Code Fresh

### Reporting

Part 2 of this challenge is to make your tests self-reporting. Again, there are many ways to do this. Maybe you save a spreadsheet with your results or send yourself an email.

### Conclusion

Challenge 12 is an opportunity to show what you learned throughout these challenges and really be creative and express your thoughts and ideas as code. Have fun with it, and as always, let us know if you have any questions.

GOOD LUCK!

## CERTIFICATION COMPLETE!

1. Push all of your completed code to your repo
2. Notify `Matt Chiang` or `Carlos Kidman`
3. Code Review will be done
4. Complete any requests that are given from review
5. Once the challenges are signed off, you will receive the certification!
