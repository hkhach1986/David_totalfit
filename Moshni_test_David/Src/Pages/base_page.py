from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def is_element_visible(self, by_locator, timeout=10, status=True):
        if status == True:
            try:
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            except TimeoutException:
                return False
        else:
            try:
                return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(by_locator))
            except TimeoutException:
                return False

    def get_element(self, by_locator, timeout=10, status=True):
        if self.is_element_visible(by_locator) and status == True:
            return self.is_element_visible(by_locator)
        elif status == False:
            return self.is_element_visible(by_locator, status=False)
        else:
            raise NoSuchElementException(f"element with locator {by_locator} couldn't find in timeout = {timeout}")

    def click_element(self, by_locator):
        self.get_element(by_locator).click()

    def send_keys(self, by_locator, text):
        self.get_element(by_locator).send_keys(text)

    def scroll_into_view(self, by_locator):
        element = self.is_element_visible(by_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_element_text(self, by_locator):
        return self.is_element_visible(by_locator).text

