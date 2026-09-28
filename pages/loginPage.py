from playwright.sync_api import Page
from pages.basePage import BasePage
from utils.config import Config

class LoginPage(BasePage):
    
    URL = Config.LOGIN_URL
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.emailTextbox = page.get_by_role("textbox", name="Email Email")
        self.passwordTextbox = page.get_by_role("textbox", name="Password Password")
        self.login_button = page.get_by_role("button", name="Log In")
        
    def navigate(self) -> None:
        super().navigate(self.URL)
        
    def insert_email(self, email: str):
        self.emailTextbox.fill(email)
        
    def insert_password(self, password: str):
        self.passwordTextbox.fill(password)
        
    def click_login(self):
        self.login_button.click()
        
    def login(self, email: str, password: str):
        self.insert_email(email)
        self.insert_password(password)
        self.click_login()