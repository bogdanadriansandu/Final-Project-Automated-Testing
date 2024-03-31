Testing of www.elefant.ro in Python using Selenium library and unittest framework

Description of the project structure:
The main folder Elefant contains the subfolder reports, where the report Test Results_2024-03-31_20-47-30.html was generated regarding the tests executed and their status and several python files.\
The base_page.py file includes the BasePage class with various methods that perform certain repetitive operations, such as searching for elements on a page, inserting text into input fields, pressing buttons, etc.\
In page_locators.py there are several classes that contain data constants, messages, texts, links, locators that are used in the other files.\
In home_page.py, login_page.py and search_page classes have been defined that contain methods that perform various actions on the pages with the same name, e.g.: perform the login operation with valid data.\
In the files that start with test_, classes with test methods and setup and teardown methods, which are executed before each test and after each test, have been added.\
In test_suite.py, all the test classes were added, with all the written tests and the instructions for generating the report with the test results.

Tests:
- test_home_page_load
- test_valid_login
- test_empty_fields_login
- test_wrong_format_email
- test_invalid_credentials
- test_search_functionality
- test_check_results
- test_product_listing
- test_add_to_cart
- test_remove_from_cart

The framework used for testing was unittest.

The results obtained: all 10 tests in 4 classes were executed and they all have Pass status.