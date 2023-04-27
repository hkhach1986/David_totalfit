import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session", params=['chrome'])
def setup(request):
    if request.param == 'chrome':
        user_chrome_options = Options()
        user_chrome_options.add_argument('--log-level=3')
        user_chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=user_chrome_options)
        driver.implicitly_wait(5)
    yield driver
    driver.quit()