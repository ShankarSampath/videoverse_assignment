from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class DashboardPage(BaseCase):

    welcome_text = "//*[contains(@class,'style_container')]//*[contains(text(),'Welcome')]"
    videos = "//*[contains(@class,'style_container')]//*[text()='Videos']"

    def navigate_to_video_page(self):
        self.wait_for_element_visible(By.XPATH, DashboardPage.welcome_text, timeout=10)
        self.click(By.XPATH, DashboardPage.videos)
        self.clear_all_cookies()

