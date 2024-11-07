from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

from data.config import BASE_URL, user_name, password


class LoginPage(BaseCase):

    email_id = "//*[@name='email']"
    password = "//*[@name='password']"
    submit = "//*[@type='submit']"
    welcome_text = "//*[contains(@class,'style_container')]//*[contains(text(),'Welcome')]"

    def login_using_valid_credentials(self):
        self.get(BASE_URL)
        self.maximize_window()
        self.send_keys(LoginPage.email_id, user_name)
        self.send_keys(LoginPage.password,password)
        self.click(By.XPATH, LoginPage.submit)
