from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class VideosPage(BaseCase):

    stream_video = "//*[text()='Test_Stream']"

    def click_on_stream_video(self):
        self.wait_for_element_visible(By.XPATH, VideosPage.stream_video, timeout=10)
        self.click(By.XPATH, VideosPage.stream_video)
