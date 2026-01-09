# AI-Assisted Automation Testing using Selenium (Python)

## Overview
This project demonstrates AI-assisted test design and automation testing using Selenium WebDriver with Python.  
The objective is to show how AI can help generate effective test scenarios and how one selected scenario can be automated.

The application under test is the SauceDemo sample web application:
https://www.saucedemo.com

---

## Tools and Technologies Used
- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- Git and GitHub

---

## AI-Generated Test Cases

AI was used to generate the following login test scenarios to ensure adequate functional coverage.

### Test Case 1: Valid Login with Correct Credentials
**Description:** Verify that a user can log in using valid credentials.  
**Expected Result:** User is redirected to the products page after successful login.

### Test Case 2: Login with Invalid Password
**Description:** Verify error message when an incorrect password is entered.  
**Expected Result:** Error message indicating invalid credentials is displayed.

### Test Case 3: Login with Invalid Username
**Description:** Verify error message when an invalid username is entered.  
**Expected Result:** Error message indicating invalid credentials is displayed.

### Test Case 4: Login with Empty Username
**Description:** Verify validation when username field is left empty.  
**Expected Result:** Error message indicating username is required.

### Test Case 5: Login with Empty Password
**Description:** Verify validation when password field is left empty.  
**Expected Result:** Error message indicating password is required.

---

## Automated Test Case

The automated test covers **Test Case 1: Valid Login with Correct Credentials**.

### Reason for Selection
- It validates the core login functionality
- It confirms successful authentication and navigation
- It is stable and not dependent on UI error message text

---

## Test Execution Steps

### Prerequisites
- Python installed
- Google Chrome installed

### Setup
1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/ai-assisted-automation-testing.git
   cd ai-assisted-automation-testing
3. Create and activate a virtual environment
   ```bash
   .\venv\Scripts\activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the test
   ```bash
   python tests/test_login.py

### Expected Outcome
- Chrome browser opens
- Login is performed automatically
- User is redirected to the inventory page
- Browser closes
- Console displays a sucess message

---

## Conclusion
This project demonstrates how AI can assist in test case generation and how Selenium automation can be used to validate core application functionality efficiently.
