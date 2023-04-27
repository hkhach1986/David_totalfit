from ..Pages.base_page import BasePage
from . login_locators import loginLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import json, os


class LoginPage(BasePage):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "data.json")
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    url = data.get("url")

    def login(self, username, password):
        self.username = self.data.get(username)
        self.password = self.data.get(password)
        username_locator = (By.NAME, loginLocators.textbox_username_name)
        password_locator = (By.NAME, loginLocators.textbox_password_name)
        login_btn_locator = (By.XPATH, loginLocators.btn_login_xpath)

        self.send_keys(username_locator, self.username)
        self.send_keys(password_locator, self.password)
        self.click_element(login_btn_locator)


    def check_login(self):
        tribe_locator = (By.XPATH, loginLocators.tribe_name_xpath)
        return self.is_element_visible(tribe_locator)

