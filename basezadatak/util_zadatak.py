from basezadatak.config_zadatak import driver, wait, Proba
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime


def get_element_by_css(by_locator):
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, by_locator)))
    return driver.find_element(By.CSS_SELECTOR, by_locator)


def parse_number_of_guests(guestNum, verify="no"):
    """ Takes 8 and if verify == 'no' returns 2 or if verify == 'verify' returns 6-10 """
    if verify != "no" and verify != "verify":
        raise Exception("Invalid input in pars_number_of_guests()")
    if 2 <= int(guestNum) <= 5:
        if verify == "no":
            return "1"
        else:
            return "2-5"
    elif 6 <= int(guestNum) <= 10:
        if verify == "no":
            return "2"
        else:
            return "6-10"
    elif 11 <= int(guestNum) <= 20:
        if verify == "no":
            return "3"
        else:
            return "11-20"
    elif int(guestNum) >= 21:
        if verify == "no":
            return "4"
        else:
            return "21+"
    else:
        raise Exception("Invalid entry in get_number_of_guests()")


def get_from_local_storage(key):
    return driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)


def parse_date(date):
    """ Takes 2024.02.15 and returns 02152024 """
    return datetime.strptime(date, "%Y-%m-%d").strftime("%m%d%Y")


def parse_time(time):
    """ Takes 20:30 and returns 0830PM """
    return datetime.strptime(time, "%H:%M").strftime("%I%M%p")


def get_element_by_xpath(by_locator):
    wait.until(ec.visibility_of_element_located((By.XPATH, by_locator)))
    return driver.find_element(By.XPATH, by_locator)


def do_click(self, by_locator):
    wait.until(ec.visibility_of_element_located(by_locator)).click()


def do_send_keys(self, by_locator, text):
    wait.until(ec.visibility_of_element_located(by_locator)).send_keys(text)


def get_element_text(self, by_locator):
    element = wait.until(ec.visibility_of_element_located(by_locator))
    return element.text


def is_enabled(self, by_locator):
    element = wait.until(ec.visibility_of_element_located(by_locator))
    return bool(element)


def get_title(self, title):
    wait.until(ec.title_is(title))
    return driver.title