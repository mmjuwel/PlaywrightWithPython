# Rooya Test Automation

End-to-end test automation for [test.rooya.ai](https://test.rooya.ai) using Playwright + pytest.

## Prerequisites

- Python 3.8+
- [Allure CLI](https://allurereport.org/docs/install/) (for reports)

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv testenv
.\testenv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install browser
playwright install chromium

# 4. Configure environment
cp .env.example .env   # then edit .env with your credentials
```

## Environment Variables (`.env`)

```
EMAIL=your@email.com
PASSWORD=yourpassword
HEADLESS=false        # true = headless | false = headed
```

## Running Tests

```bash
# All tests
pytest

# Specific module
pytest tests/test_login.py -v
pytest tests/test_trip.py -v

# With Allure report
pytest
allure serve reports/allure-results
```

## Project Structure

```
├── pages/          # Page Object Model classes
├── tests/          # Test files
├── test_data/      # JSON test data
├── utils/          # Config and helpers
├── reports/        # Allure results (auto-cleared each run)
├── conftest.py     # Fixtures
└── pytest.ini      # pytest config
```

## Features

- Page Object Model (POM) pattern
- Data-driven tests via external JSON files
- Allure reporting with failure screenshots
- Auto-retry failed tests (2 retries with 2s delay)
- Headless/headed mode via `.env`
- Session-scoped login — authenticates once for all trip tests
