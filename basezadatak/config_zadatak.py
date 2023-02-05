from basezadatak.util_zadatak import Util_zadatak
from pagezadatak.organize_page import Organize_page
from pagezadatak.mind_cook_page import Mind_cook_page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Config_zadatak:
    options = Options()
    # options.binary_location = "../driverslib/chromedriver"
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    utilZadatak = Util_zadatak(driver, wait)
    organizePage = Organize_page(utilZadatak)
    mindCookPage = Mind_cook_page(utilZadatak)
