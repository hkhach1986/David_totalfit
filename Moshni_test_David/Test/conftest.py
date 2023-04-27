import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Src.Pages.login_page import LoginPage


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


@pytest.fixture(scope="class")
def login(setup, request, username = "username", password = "password"):
    driver = setup
    login_page = LoginPage()
    login_page.driver = driver
    driver.get(login_page.url)
    if request.node.get_closest_marker("negative") is not None:
        print("Calling negative!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()
        login_page.login("false_username", "false_password")
    else:
        print("CALLING POSITIVE!!!!!!!!!!!!!!!!!!")
        login_page.login(username, password)
