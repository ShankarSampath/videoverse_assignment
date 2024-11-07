import allure
import pytest
from allure_commons.types import AttachmentType
from seleniumbase import BaseCase


from data.config import start_time, end_time, download_confirmation
from pages.clip_page.auto_flip_page import AutoFlipPage
from pages.clip_page.clip_page import ClipPage
from pages.clip_page.edit_clip_page import EditClipPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.videos_page import VideosPage


class TestVideoEdit(BaseCase):

    @pytest.mark.videoverse
    @pytest.mark.trim
    def test_verify_user_is_able_to_edit_video(self):
        expected_success_message = 'Clip has been created successfully!'
        LoginPage.login_using_valid_credentials(self)
        DashboardPage.navigate_to_video_page(self)
        VideosPage.click_on_stream_video(self)
        ClipPage.click_on_edit(self)
        EditClipPage.edit_clip_by_applying_trim(self)
        EditClipPage.generate_trimmed_clip(self)
        actual_success_message = self.get_text(EditClipPage.clip_created_success_message)
        self.assert_equal(actual_success_message, expected_success_message)
        EditClipPage.verify_view_clip(self)
        actual_start_time = self.get_text(EditClipPage.verify_start_time)
        actual_end_time = self.get_text(EditClipPage.verify_end_time)
        self.assert_equal(actual_start_time, start_time)
        self.assert_equal(actual_end_time, end_time)
        allure.attach(self.driver.get_screenshot_as_png(), name='User is Able to Edit Video Successfully',
                      attachment_type=AttachmentType.PNG)

    @pytest.mark.videoverse
    @pytest.mark.flip_and_crop
    def test_verify_user_is_able_to_flip_and_crop_video(self):
        expected_selected_aspect_ratio = 'Preview (16:9)'
        LoginPage.login_using_valid_credentials(self)
        DashboardPage.navigate_to_video_page(self)
        VideosPage.click_on_stream_video(self)
        ClipPage.click_on_kebab_menu(self)
        AutoFlipPage.edit_clip(self)
        actual_selected_aspect_ratio = self.get_text(AutoFlipPage.get_preview_details)
        self.assert_equal(actual_selected_aspect_ratio, expected_selected_aspect_ratio)
        allure.attach(self.driver.get_screenshot_as_png(), name='Aspect Ratio is Selected Successfully',
                      attachment_type=AttachmentType.PNG)
        ClipPage.download_video(self)
        actual_download_confirmation_message = self.get_text(ClipPage.download_confirmation)
        self.assert_equal(actual_download_confirmation_message, download_confirmation)
        allure.attach(self.driver.get_screenshot_as_png(), name='Clip is Downloaded Successfully',
                      attachment_type=AttachmentType.PNG)