# Test Automation Project (Page Object Model)

UI autotests project using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern for an e-commerce website.

## Project Structure

```text
.
├── conftest.py           # Pytest fixtures (browser initialization with language support)
├── pytest.ini            # Pytest configuration and registered custom markers
├── requirements.txt      # Project dependencies
├── test_main_page.py     # Autotests for Main Page
├── test_product_page.py  # Autotests for Product Page
└── pages/                # Page Object classes
    ├── __init__.py
    ├── base_page.py      # Base class with shared methods and locators
    ├── main_page.py      # Main page class
    ├── product_page.py   # Product page class
    ├── login_page.py     # Login and registration page class
    ├── basket_page.py    # Basket page class
    └── locators.py       # Locators for all pages
```

## Setup & Installation

1. Clone repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Linux / macOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run peer-review test suite:
```bash
pytest -v --tb=line --language=en -m need_review
```

### Run all tests on Product Page:
```bash
pytest -v --tb=line --language=en test_product_page.py
```

### Run all tests on Main Page:
```bash
pytest -v --tb=line --language=en test_main_page.py
```
