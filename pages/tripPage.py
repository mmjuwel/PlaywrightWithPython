from playwright.sync_api import Page
from pages.basePage import BasePage
from utils.config import Config
import re

class TripPage(BasePage):
    
    URL = Config.TRIPS_URL
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.searchOptionDropdown = page.locator(".v-btn--density-compact > .v-btn__content")
        self.deviceIdOption = page.locator("div").filter(has_text=re.compile(r"^Device ID$")).nth(2)
        self.searchInput = page.get_by_test_id("trips-device-search-input").get_by_role("textbox", name="Search")
        self.searchButton = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4)
        self.completed_trip = page.get_by_test_id("completed-trips-button").get_by_label("Badge")
        self.inprogress_trip = page.get_by_test_id("in-progress-button").get_by_label("Badge")
        self.unidentified_trip = page.get_by_test_id("unidentified-button").get_by_label("Badge")


    def navigate(self) -> None:
        super().navigate(self.URL)  

    def click_search_option_dropdown(self) -> None:
        self.searchOptionDropdown.click()

    def select_device_id_option(self) -> None:
        self.deviceIdOption.click()

    def enter_search_input(self, device_id: str) -> None:
        self.searchInput.fill(device_id)

    def click_search_button(self) -> None:
        self.searchButton.click()

    def wait_for_loading(self) -> None:
        loading = self.page.get_by_text("Loading...")
        try:
            loading.wait_for(state="visible", timeout=3000)
            loading.wait_for(state="hidden", timeout=30000)
        except Exception:
            pass 

    def search_by_device_id(self, device_id: str) -> None:
        self.click_search_option_dropdown()
        self.select_device_id_option()
        self.enter_search_input(device_id)
        self.click_search_button()
        self.wait_for_loading()

    def _get_badge_count(self, badge_locator) -> int:
        if badge_locator.is_visible():
            return int(badge_locator.inner_text())
        return 0

    def get_completed_trip_count(self) -> int:
        return self._get_badge_count(self.completed_trip)
    
    def get_inprogress_trip_count(self) -> int:
        return self._get_badge_count(self.inprogress_trip)
    
    def get_unidentified_trip_count(self) -> int:
        return self._get_badge_count(self.unidentified_trip)
    
    