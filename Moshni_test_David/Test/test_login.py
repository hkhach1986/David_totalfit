from Src.Pages.login_page import LoginPage
import pytest


class Test_Login(LoginPage):

    @pytest.mark.positive
    def test_login_positive(self, setup, login):
        self.driver = setup
        assert self.check_login(), "login fail"

    @pytest.mark.negative
    def test_login_negative(self, setup, login):
        self.driver = setup
        assert not self.check_login(), "Login success: shouldn't login"

