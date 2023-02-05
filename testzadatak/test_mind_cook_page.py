from basezadatak.config_zadatak import Config_zadatak
import time

driver = Config_zadatak.driver
utilZadatak = Config_zadatak.utilZadatak
mindCookPage = Config_zadatak.mindCookPage


class Test_mind_cook_page(Config_zadatak):
    def test_setup(self):
        global url
        url = utilZadatak.data()["mindCookPage"]["url"]
        driver.maximize_window()

    def test_happy_path(self):
        driver.get(url)
        pitanja = utilZadatak.data()["mindCookPage"]["pitanja"]
        jela = utilZadatak.data()["mindCookPage"]["jela"]
        for key in jela:
            vrednosti = jela[key]
            for i in range(len(vrednosti)):
                pitanje = str(i)
                mindCookPage.click_on_card_button(pitanja[pitanje], vrednosti[i])
            mindCookPage.click_on_read_my_mind_button()
            utilZadatak.scroll(550)
            assert mindCookPage.get_dish_name() == key
            driver.refresh()
