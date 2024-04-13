**Testing of www.elefant.ro in Python using Selenium library and unittest framework**

**Description of the project structure:**\
The main folder, **Elefant**, contains 2 directories: **pages** and **tests**, which contain the python files of pages and tests, respectively.\
The **reports** sub-folder, where the **Test Results_2024-04-08_05-29-29.html** report was generated regarding the executed tests and their status was automatically created in the **tests** directory after running the test suite from the **test_suite.py** file.\
The **base_page.py** file in the **pages** directory includes the **BasePage** class with various methods that perform certain repetitive operations, such as searching for elements on a page, inserting text into input fields, pressing buttons, etc.\
In **page_locators.py** there are several classes that contain data constants, messages, texts, links, locators that are used in the other files.\
In **home_page.py**, **login_page.py** and **search_page.py**, classes were defined that contain methods that perform various actions on pages with the same name, e.g.: perform the login operation with valid data.\
In the files that start with **test_** in the **tests** directory, classes with test methods and **setUp** and **tearDown** methods, which are executed before each test and after each test, have been added.\
In the **setUp** method, a driver object from the Chrome() class is instantiated, the browser window is maximized and all the elements on the respective page are waiting to be loaded.\
In the **tearDown** method, the browser that was opened using Selenium WebDriver is closed (self.driver.quit()).\
This command is important to ensure that all resources associated with the browser are released and that processes associated with it are properly closed after testing or automation operations have completed.\
In **test_suite.py**, all the test classes were added, with all the written tests and the instructions for generating the execution report with the test results.

**Tests created and executed:**
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

**The framework used for testing was _unittest_.**

**Preconditions: to have a user already created.**

**Running the tests** can be done in several ways:
1. Click on the green triangle next to the name of the test class -> it will run all the tests in that class
2. Click on the green triangle next to the name of the test method -> it will only execute the test method that I ran
3. Running a specific test file from the terminal: python -m unittest filename.py
4. Running all test files from the terminal: python -m unittest

When we want to skip some tests at runtime, we can use the @unittest.skip decorator placed before each test method that we want to skip.\
**Alternatively:** from the **test_suite.py** file click on the green triangle next to the name of the class that includes the test suite or from **the terminal** according to point 3 above and all the tests added to the test suite will run.

**The results obtained:**\
10 tests grouped into 4 test classes were created and executed. As tested modules or functionalities are the following: Login Module (both positive and negative testing), Search Module, Adding and Deleting from the cart, Home page.\
All the tests were added to a **test suite**, and after running it all the tests passed. At the same time, an **execution report** was generated from which it can be seen that all the tests run have a **PASS status**. No bugs were found, but that doesn't mean there aren't any.

