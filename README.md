# API Automation Framework

I built this project to practice API test automation using Python and Pytest.
The target API is JSONPlaceholder which is a free mock REST API.

## Why I Built This
During my QA learning journey I wanted to go beyond Selenium and understand
how backend APIs are tested in real projects. This framework is the result
of that practice.

## What I Used
- Python
- Pytest
- Requests library
- pytest-html for reports

## How to Run

Install packages:
pip install -r requirements.txt

Run all tests:
pytest -v

Run with report:
pytest -v --html=reports/report.html

## What I Tested
I covered all four CRUD operations against the users endpoint:
- GET - fetch a single user and handle invalid user
- POST - create user with single and multiple data sets
- PUT - update user details and handle invalid user
- DELETE - delete user and handle invalid user

## What I Learned
- How to structure an API automation project
- Using fixtures in conftest.py to avoid repeating code
- Parametrize for data driven testing
- Difference between mock API behavior and real API behavior

## Author
Shijindas KP
github.com/shijindaskp7358
linkedin.com/in/shijindas-kp-19b631276