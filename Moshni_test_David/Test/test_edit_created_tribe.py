from Src.Pages.tribe_page import TribePage


class Test_Edit_Tribe(TribePage):

    def test_edit_new_tribe(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        tribe_name = "Tribe_Yerevan_Komitas"
        self.create_new_tribe(tribe_name)
        assert self.check_created_tribe(tribe_name)
        self.view_tribe()

        