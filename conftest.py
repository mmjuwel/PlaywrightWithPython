import os
import shutil
import platform
import pytest
from playwright.sync_api import sync_playwright
import allure
from pages.loginPage import LoginPage
from utils.config import Config

def pytest_configure(config):
    allure_results_dir = "reports/allure-results"
    
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
        print(f"\n✓ Cleared previous allure results: {allure_results_dir}")
    
    os.makedirs(allure_results_dir, exist_ok=True)

    env_properties = f"""Browser={Config.BROWSER}
    Headless={Config.HEADLESS}
    Base URL={Config.BASE_URL}
    Environment=Test
    OS={platform.system()} {platform.release()}
    Python={platform.python_version()}
    """
    with open(os.path.join(allure_results_dir, "environment.properties"), "w") as f:
        f.write(env_properties)

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=Config.HEADLESS)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   page.set_default_timeout(60000)
   yield page
   page.close()

@pytest.fixture(scope="session")
def authenticated_page(browser):
    page = browser.new_page()
    page.set_default_timeout(60000)
    
    login_page = LoginPage(page)
    login_page.navigate()
    page.wait_for_load_state("networkidle")
    
    login_page.login(
        email=Config.EMAIL,
        password=Config.PASSWORD
    )

    page.wait_for_url(lambda url: "/login" not in url, timeout=60000)
    page.wait_for_load_state("networkidle")
    
    yield page
    
    page.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("authenticated_page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )