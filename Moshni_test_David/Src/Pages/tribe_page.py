from time import sleep
from . tribe_locators import tribeLocators
from ..Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ..Pages.login_page import LoginPage
from . login_locators import loginLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class TribePage(LoginPage):

    def create_new_tribe(self, tribe_name):
        add_new_tribe_btn_loc = (By.XPATH, tribeLocators.add_new_tribe_btn)
        add_new_tribe_field_loc = (By.XPATH, tribeLocators.add_tribe_field)
        save_new_tribe_loc = (By.XPATH, tribeLocators.add_tribe_save_btn)
        sleep(3)
        self.click_element(add_new_tribe_btn_loc)
        self.click_element(add_new_tribe_field_loc)
        sleep(3)
        self.send_keys(add_new_tribe_field_loc, tribe_name)
        self.click_element(save_new_tribe_loc)
        sleep(3)

    def check_tribe(self, tribe_name):
        tribe_loc_name = tribeLocators.tribe_window_xpath.replace("name", tribe_name)
        tribe_name_loc = (By.XPATH, tribe_loc_name)
        return self.is_element_visible(tribe_name_loc)


    def view_tribe(self, tribe_name):
        more_horiz_btn = tribeLocators.more_horiz_btn.replace('tribe name', tribe_name)
        more_horiz_loc = (By.XPATH, more_horiz_btn)
        view_tribe_loc = (By.XPATH, tribeLocators.tribe_view_btn)
        tribe_page_name = tribeLocators.tribe_page_name.replace('tribe name', tribe_name)
        tribe_page_name_loc = (By.XPATH, tribe_page_name)
        self.click_element(more_horiz_loc)
        sleep(3)
        self.click_element(view_tribe_loc)
        sleep(3)
        return self.is_element_visible(tribe_page_name_loc)

    def invite_tribe(self):
        invite_tribe_member_loc = (By.XPATH, tribeLocators.tribe_members_invite)
        tribe_members_page_loc = (By.XPATH, tribeLocators.tribe_members_page)
        self.click_element(invite_tribe_member_loc)
        return self.is_element_visible(tribe_members_page_loc)
    
    def completed_workouts(self):
        tribe_completed_workouts_btn_loc = (By.XPATH, tribeLocators.tribe_completed_workouts_btn)
        tribe_completed_workouts_page_loc = (By.XPATH, tribeLocators.tribe_completed_workouts_page)
        self.click_element(tribe_completed_workouts_btn_loc)
        return self.is_element_visible(tribe_completed_workouts_page_loc)

    def waiting_for_reaction(self):
        tribe_waiting_for_reaction_btn_loc = (By.XPATH, tribeLocators.tribe_witing_for_reaction_btn)
        tribe_waiting_for_reaction_page_loc = (By.XPATH, tribeLocators.tribe_witing_for_reaction_page)
        self.click_element(tribe_waiting_for_reaction_btn_loc)
        return self.is_element_visible(tribe_waiting_for_reaction_page_loc)

    def delete_tribe(self, tribe_name):
        more_horiz_btn = tribeLocators.more_horiz_btn.replace('tribe name', tribe_name)
        more_horiz_loc = (By.XPATH, more_horiz_btn)
        delete_tribe_loc = (By.XPATH, tribeLocators.tribe_delete_btn)
        self.click_element(more_horiz_loc)
        sleep(2)
        self.click_element(delete_tribe_loc)
        sleep(2)
        self.click_element(delete_tribe_loc)
        sleep(2)
    