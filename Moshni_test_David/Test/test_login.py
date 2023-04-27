from Src.Pages.login_page import LoginPage
import pytest


class Test_Login(LoginPage):

    def test_login_positive(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.login(self.data.get("username"), self.data.get("password"))
        assert self.check_login(), "login fail"

    def test_login_negative(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.login(self.data.get("false_username"), self.data.get("false_password"))
        assert not self.check_login(), "Login success: shouldn't login"

