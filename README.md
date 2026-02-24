# SauceDemo Automation Framework

## Overview
This project is an automated test framework built using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Faker
- Pytest-HTML Reports

The framework automates:
- Login functionality
- Checkout form submission
- Explicit waits
- Screenshot capture on failure
- HTML test report generation

---

## Project Structure

pages/ – Page classes  
tests/ – Test cases  
utils/ – Driver setup & config  
reports/ – Test reports  

---

## How to Run

1. Clone the repository:
   git clone <repo-url>

2. Create virtual environment:
   python -m venv venv

3. Activate environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run tests:
   pytest -v

6. Generate report:
   pytest --html=reports/report.html --self-contained-html

---

## Author
Anusha
