from basezadatak.util_zadatak import Util_zadatak


class Mind_cook_page:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.utilZadatak = Util_zadatak(driver, wait)

    # Getters
    def get_list_of_question_cards(self):
        return self.utilZadatak.get_elements_by_css("#exampleModalLabel")

    def get_question(self, questionIndex):
        return self.get_list_of_question_cards()[questionIndex]

    def get_list_of_buttons(self):
        return self.utilZadatak.get_elements_by_css(".btn-group>button")

    def get_list_of_card_buttons(self):
        """"Returns dictionary with question as a key and button names in a list as a value"""
        listOfButtons = self.get_list_of_buttons()
        sortedButtonsDict = {}
        if len(listOfButtons) % 2 != 0:
            raise Exception("The number or question button elements is not even.")
        counter = 0

        # Count question card names
        for i in range(int(len(listOfButtons) / 2)):
            # Create an empty list for every question card
            sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]] = []

            # Add 2 elements from listOfButtons to the appropriate list
            while len(sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]]) < 2:
                sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]].append(
                    listOfButtons[counter])
                counter += 1

            # Sort list items so their index reflects their value in the calculation
            temp1 = sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]][1]
            sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]][1] = \
                sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]][0]
            sortedButtonsDict[self.utilZadatak.data()["mindCookPage"]["pitanja"][str(i)]][0] = temp1

        return sortedButtonsDict

    def get_read_my_mind_button(self):
        return self.utilZadatak.get_element_by_css("#readmymind")

    def get_dish_name(self):
        return self.utilZadatak.get_element_by_css(".Recomendation>.card>h4").text

    # Setters

    def click_on_card_button(self, question, button_value):
        # Access a value from a list inside a dictionary
        self.get_list_of_card_buttons()[question][button_value].click()

    def click_on_read_my_mind_button(self):
        self.get_read_my_mind_button().click()
