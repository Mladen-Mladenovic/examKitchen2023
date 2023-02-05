import pytest
from pagezadatak.organize_page import Organize_page
from pagezadatak.mind_cook_page import Mind_cook_page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Config_zadatak:
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    organizePage = Organize_page(driver, wait)
    mindCookPage = Mind_cook_page(driver, wait)


@pytest.fixture(scope="session")
def teardown():
    Config_zadatak.driver.delete_all_cookies()
    Config_zadatak.driver.quit()
