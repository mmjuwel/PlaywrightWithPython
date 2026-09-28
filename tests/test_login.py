import pytest
from pages.loginPage import LoginPage
from playwright.sync_api import expect
from utils.test_data_loader import get_login_test_data
import allure

LOGIN_DATA = get_login_test_data()
TEST_IDS = [data["test_id"] for data in LOGIN_DATA]

class TestLogin:
   
    @pytest.mark.parametrize("login_data", LOGIN_DATA, ids=TEST_IDS)
    @allure.title("Login Test")
    @allure.description("Test login functionality with various credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_external_data(self, page, login_data):
   
        login_page = LoginPage(page)
        email = login_data["email"]
        password = login_data["password"]
        expected_user = login_data.get("expected_user")
        should_succeed = login_data["should_succeed"]
        message = login_data["message"]

        with allure.step("Open login page"):
            login_page.navigate()
            page.wait_for_load_state("networkidle")

        with allure.step(f"Enter credentials - Email: {email}"):
            login_page.insert_email(email)
           
        with allure.step(f"Enter credentials - Password: {password}"):
            login_page.insert_password(password)
     
        with allure.step(f"Click login button"):
            login_page.click_login()
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("domcontentloaded")
     
        with allure.step("Verify login result"):
            if should_succeed:
                with allure.step(f"Verify Login Success"):
                    page.get_by_text(message).wait_for(timeout=10000)
                    expect(page.get_by_text(message)).to_be_visible()
                    expect(page.get_by_text(expected_user)).to_be_visible()
            else:
                with allure.step("Verify login failed properly"):
                    error_messages = page.get_by_text(message).all()
                    
                    if len(error_messages) > 1:
                        expect(page.get_by_text(message).first).to_be_visible()
                    else:
                        expect(page.get_by_text(message)).to_be_visible()
