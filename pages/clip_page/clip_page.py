from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class ClipPage(BaseCase):

    edit_clip = "(//*[text()='Clip 1']/preceding::*[text()='Edit'])[1]"
    kebab_menu = "//*[text()='Clip 1']/preceding::img[1]"
    auto_flip = "//*[text()='Auto flip/Dynamic flip']"
    close_icon = "//*[@role='dialog']//*[@class='ant-modal-close-x']"
    download = "//*[text()='Download']"
    download_confirmation = "//*[text()='Download started']"

    def click_on_edit(self):
        self.wait_for_element_visible(By.XPATH, ClipPage.edit_clip, timeout=10)
        self.click(By.XPATH, ClipPage.edit_clip)

    def click_on_kebab_menu(self):
        self.wait_for_element_visible(By.XPATH, ClipPage.edit_clip, timeout=10)
        self.click(By.XPATH, ClipPage.kebab_menu)
        self.click(By.XPATH, ClipPage.auto_flip)

    def download_video(self):
        self.click(By.XPATH, ClipPage.close_icon)
        self.click(By.XPATH, ClipPage.kebab_menu)
        self.click(By.XPATH, ClipPage.download)

