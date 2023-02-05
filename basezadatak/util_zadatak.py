from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import json


class Util_zadatak:
    """ Here is a collection of all methods that are not bound to specific page objects """

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_element_by_css(self, locator):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    @staticmethod
    def format_number_of_guests(guestNum, verify="no"):
        """Takes 8 and if verify == 'no' returns 2 or if verify == 'verify' returns 6-10"""
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

    def get_from_local_storage(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    @staticmethod
    def format_date(date):
        """Takes 2024.02.15 and returns 02152024"""
        return datetime.strptime(date, "%Y-%m-%d").strftime("%m%d%Y")

    @staticmethod
    def format_time(time):
        """Takes 20:30 and returns 0830PM"""
        return datetime.strptime(time, "%H:%M").strftime("%I%M%p")

    def get_elements_by_css(self, locator):
        """Returns a list"""
        self.wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    @staticmethod
    def data():
        with open("../testdata/data.json", "r") as read_file:
            return json.load(read_file)

    def wait_for_element_to_be_clickable(self, element):
        self.wait.until(ec.element_to_be_clickable(element))

    def scroll(self, v=0, h=0):
        self.driver.execute_script("window.scrollTo(" + str(h) + ", " + str(v) + ")")
