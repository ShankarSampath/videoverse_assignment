from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class AutoFlipPage(BaseCase):

    aspect_ratio = "//*[@role='dialog']//*[text()='16:9']"
    get_preview_details = "//*[@role='dialog']//*[@class='style_previewTitle__0r-4Q']"

    def edit_clip(self):

        self.click(By.XPATH, AutoFlipPage.aspect_ratio)
        self.wait(5)