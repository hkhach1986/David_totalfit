import pytest

from Src.Pages.tribe_page import TribePage


class Test_Tribe(TribePage):
    
    @pytest.fixture(autouse=True)
    def setup_browser (self, setup):
        self.driver = setup
        self.driver.get(self.url)


    def test_create_tribe(self):
        tribe_name = "Tribe_Yerevan_Komitas"
        self.create_new_tribe(tribe_name)
        assert self.check_created_tribe(tribe_name)

    def test_invite_member(self):
        assert self.view_tribe()
        assert self.invite_tribe()

    def test_delete_tribe(self):
        self.delete_tribe()

