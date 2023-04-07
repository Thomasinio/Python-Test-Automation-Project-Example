# Python API Test Automation Example

## Table of contents
* [Project description](#project-description)
* [Technologies](#technologies)
* [Setup](#setup)

## Project description
The objective of this mini-project is to provide a clear, concise, and well-organized example of a Python API test automation project. The code is designed to be easily readable, extensible, and maintainable, and can serve as a foundation for building your own API test automation projects.

In addition to providing a working codebase, this project also aims to answer common questions that automation engineers may have when starting out, such as:
 * How do I validate API responses?
 * How can I implement logging in my tests?
 * What's the best way to generate reports for my test runs?

By following the examples and best practices in this project, you can gain a better understanding of how to write effective and efficient API tests in Python.
```
.
├── src                    
│   ├── configs          
│   ├── enums         
│   ├── models
│   └── test_data   
├── tests                    
│   ├── allure_results          
│   └── logs         
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```
## Technologies
This project uses the following technologies:
 * Python 3.x
 * Requests library
 * PyTest testing framework
	
## Setup
To get started with this project, you'll need to do the following:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Open the `config.ini` file and enter your API endpoint and any necessary credentials.
4. Run the tests using the command `pytest -v`.
That's it! With these simple steps, you should be able to run the example tests and see how they work. Feel free to modify the code and experiment with different test scenarios to see how they affect the test results.

TEMP
 * docker build -t py_test_auto_project .
 * docker run --env-file .env -p 5050:8080 --rm py_test_auto_project
 * On the host machine go to localhost:5050




