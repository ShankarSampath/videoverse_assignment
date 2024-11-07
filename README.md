
# Videoverse Assignment - SeleniumBase and Page Object Model

A Selenium automation framework for Videoverse, utilizing the Page Object Model (POM) design pattern with SeleniumBase and Pytest.

## Technologies and Tools

- **Selenium WebDriver**
- **Python**
- **PyCharm** (IDE)
- **GitHub** (Version Control)
- **SeleniumBase** (Automation Framework)
- **Pytest** (Testing Framework)
- **Chrome Browser**

## Project Features

- **Data-Driven Testing**: Enables running tests with multiple sets of data.
- **Page Object Model (POM)**: Promotes reusable, maintainable, and structured code by separating page elements from test logic.
- **GitHub Repository**: Version control for collaboration and code management.
- **Allure Reporting**: Generate detailed test reports for better insights.

## Setup

1. **Configure Python Interpreter**  
   Ensure Python is configured in your IDE.

2. **Install Dependencies**  
   Run the following command to install all dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Running Test Scripts

3. **Execute Test Suite**  
   Run tests marked with `videoverse` using Pytest and generate results for Allure:
   ```bash
    pytest -m videoverse --headless --alluredir allure-results
   ```

## Generating Allure Report

4. **Generate and View Report**  
   Use Allure to serve the test report locally:
   ```bash
   allure serve allure-results
   ```
