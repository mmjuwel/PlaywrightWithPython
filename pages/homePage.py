from playwright.sync_api import Page
from pages.basePage import BasePage
from utils.config import Config
import re

class HomePage(BasePage):
    
    URL = Config.HOME_URL
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.trip_menu = page.locator("div").filter(has_text=re.compile(r"^Trips$")).nth(1)

        
    def navigate(self) -> None:
        super().navigate(self.URL)
        
    def click_trip_menu(self) -> None:
        self.trip_menu.click()
    