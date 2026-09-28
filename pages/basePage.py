from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def get_current_url(self) -> str:
        return self.page.url