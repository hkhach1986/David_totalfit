import pytest
import time 

from Src.Pages.tribe_page import TribePage

@pytest.mark.parametrize("login", ["positive"], indirect=True)
class Test_Tribe(TribePage):
    
    tribe_name = "Tribe_Yerevan_Komitas22"
    def test_create_tribe(self, setup, login):
        self.driver = setup
        self.create_new_tribe(self.tribe_name)
        assert self.check_tribe(self.tribe_name)

    
    def test_invite_member(self, setup, login):
        self.driver = setup
        assert self.view_tribe(self.tribe_name)
        assert self.invite_tribe()

    def test_compleate_workouts(self, setup, login):
        self.driver = setup
        self.driver.back() # navigate back to the previous page
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        assert self.view_tribe(self.tribe_name)
        assert self.completed_workouts()

    def test_waiting_for_reaction(self, setup, login):
        self.driver = setup
        self.driver.back() # navigate back to the previous page
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        assert self.view_tribe(self.tribe_name)
        assert self.waiting_for_reaction()

    
    def test_delete_tribe(self, setup, login):
        self.driver = setup
        self.driver.back() # navigate back to the previous page
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.delete_tribe(self.tribe_name)
        assert not self.check_tribe(self.tribe_name)