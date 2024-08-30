Saucedemo Automation Test Suite
This project contains an automated test suite for the Saucedemo website. It is designed to validate the login functionality and the ability to order a product based on the provided scenarios. The test suite uses Python, Selenium, and Behave to automate the acceptance criteria.

Table of Contents
Prerequisites
Project Structure
Setup Instructions
Running the Tests
Test Scenarios
Generating Reports
Known Issues
Contributing
Prerequisites
Python 3.6 or higher
Google Chrome browser
Git
Project Structure
bash
Copy code
sauce_demo_test/
├── features/
│   ├── steps/
│   │   └── test_steps.py             # Step definitions implementing the test logic
│   ├── environment.py                # Environment setup and teardown
│   └── sauce_demo.feature            # Gherkin feature file with test scenarios
├── reports/
│   └── report.html                   # HTML report of the test results
├── scripts/
│   └── run_tests.sh                  # Shell script to run the tests
├── tests/
│   └── test_script.sh                # Additional test scripts if needed
├── README.md                         # Project documentation
└── requirements.txt                  # Dependencies required for the project
Setup Instructions
Clone the Repository

bash
Copy code
git clone <repository-link>
cd sauce_demo_test
Create a Virtual Environment (Optional)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install Required Dependencies

Install the required Python libraries using the requirements.txt file.

bash
Copy code
pip install -r requirements.txt
Running the Tests
Run the Test Suite

Execute the shell script to run the tests and generate the report.

bash
Copy code
./scripts/run_tests.sh
View the Report

The test results will be saved in the reports/report.html file. Open this file in your browser to see the detailed report.

Test Scenarios
Successful Login

Verify that a valid user can log in successfully and is redirected to the main page.
Failed Login

Validate that an error message is displayed when a locked-out user attempts to log in.
Order a Product

Test the ability to sort products, add the highest-priced product to the cart, and verify the total amount during checkout.
Generating Reports
Reports are automatically generated in the reports/ directory as an HTML file after running the test suite. You can customize the report generation in the run_tests.sh script.
Known Issues
WebDriver Manager: Ensure you have the latest ChromeDriver installed via webdriver-manager to avoid version mismatches.
Parallel Execution: Currently, tests are not set up for parallel execution but can be modified to support it using Behave plugins.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.