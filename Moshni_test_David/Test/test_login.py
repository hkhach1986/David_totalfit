from Src.Pages.login_page import LoginPage
import pytest


class Test_Login(LoginPage):

    @pytest.mark.parametrize("login", ["positive"], indirect=True)
    def test_login_positive(self, setup, login):
        self.driver = setup
        assert self.check_login(), "login fail"

    @pytest.mark.parametrize("login", ["negative"], indirect=True)
    def test_login_negative(self, setup, login):
        self.driver = setup
        assert not self.check_login(), "Login success: shouldn't login"

