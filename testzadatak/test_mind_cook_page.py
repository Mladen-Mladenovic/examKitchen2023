from basezadatak.config_zadatak import Config_zadatak
import time

mindCookPage = Config_zadatak.mindCookPage
utilZadatak = mindCookPage.utilZadatak
driver = mindCookPage.driver


class Test_mind_cook_page(Config_zadatak):
    def test_setup(self):
        global url
        url = utilZadatak.data()["mindCookPage"]["url"]
        driver.maximize_window()

    def test_happy_path(self):
        driver.get(url)
        pitanja = utilZadatak.data()["mindCookPage"]["pitanja"]
        jela = utilZadatak.data()["mindCookPage"]["jela"]
        # Pick a defined dish
        for key in jela:
            vrednosti = jela[key]
            # Count the number of total answers in the answer list
            for i in range(len(vrednosti)):
                # Pick a question for which to give an answer
                pitanje = str(i)
                # Define a question an answer
                mindCookPage.click_on_card_button(pitanja[pitanje], vrednosti[i])
            mindCookPage.click_on_read_my_mind_button()
            # Scroll is required to get the dish name element
            utilZadatak.scroll(550)
            assert mindCookPage.get_dish_name() == key
            # Refresh to be able to move to another dish
            driver.refresh()
