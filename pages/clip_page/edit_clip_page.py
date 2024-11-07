import time

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

from data.config import start_time, end_time


class EditClipPage(BaseCase):


    trim_option = "//*[@data-testid='EditingSidebarToolBarItem-trim']"
    start_time = "//*[text()='Start Time']/following::*[@data-testid='EditingSidebarContentTrim-startTime']"
    end_time = "//*[text()='Start Time']/following::*[@data-testid='EditingSidebarContentTrim-endTime']"
    apply_button = "//*[text()='Apply']"
    generate_button = "//*[text()='Generate']"
    save_as_new_clip = "//*[text()='Save as New']"
    enter_title_for_new_clip = "//*[@data-testid='ClipEditorTrimClipConfirmationModal-input-Title']"
    save_button = "//*[text()='Save']"
    clip_created_success_message = "//*[text()='Clip has been created successfully!']"
    accept_cookies = "//*[text()='Accept All']"
    view_clip = "//*[text()='View Clip']"
    verify_start_time = "//*[@data-testid = 'ClipTrimModal-startTime']"
    verify_end_time = "//*[@data-testid = 'ClipTrimModal-endTime']"

    def click_on_trim(self):
        self.wait_for_element_visible(By.XPATH, EditClipPage.trim_option, timeout=10)
        self.click(By.XPATH, EditClipPage.trim_option)

    def update_start_time(self):
        self.clear(EditClipPage.start_time)
        self.send_keys(EditClipPage.start_time, start_time)

    def update_end_time(self):
        self.clear(EditClipPage.end_time)
        self.send_keys(EditClipPage.end_time, end_time)
        self.click(By.XPATH, EditClipPage.accept_cookies)

    def edit_clip_by_applying_trim(self):
        EditClipPage.click_on_trim(self)
        EditClipPage.update_start_time(self)
        EditClipPage.update_end_time(self)
        self.click_if_visible(By.XPATH, EditClipPage.accept_cookies)
        self.click(By.XPATH, EditClipPage.apply_button)

    def generate_trimmed_clip(self):
        self.click(By.XPATH, EditClipPage.generate_button)
        self.click(By.XPATH, EditClipPage.save_as_new_clip)
        self.send_keys(EditClipPage.enter_title_for_new_clip, 'Shankar_Assignment')
        self.click(By.XPATH, EditClipPage.save_button)
        time.sleep(5)
        self.click_if_visible(By.XPATH, EditClipPage.accept_cookies)

    def verify_view_clip(self):
        self.click_if_visible(By.XPATH, EditClipPage.accept_cookies)
        self.click(By.XPATH, EditClipPage.view_clip)


