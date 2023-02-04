class Organize_page:

    def __init__(self, utilZadatak):
        self.utilZadatak = utilZadatak

    #   Getters:
    def get_organizer_textbox(self):
        return self.utilZadatak.get_element_by_css("input[placeholder = 'Who is organizing birthday']")

    def get_birthday_person_textbox(self):
        return self.utilZadatak.get_element_by_css("input[placeholder = 'Who is having birthday']")

    def get_age_of_pb_textbox(self):
        return self.utilZadatak.get_element_by_css("#age")

    def get_date_picker(self):
        return self.utilZadatak.get_element_by_css("#date")

    def get_time_picker(self):
        return self.utilZadatak.get_element_by_css("#time")

    def get_number_of_guests_button(self):
        return self.utilZadatak.get_element_by_css("#persons")

    def get_number_of_guests_selection(self, guestNum):
        return self.utilZadatak.get_element_by_css(
            "option[ value= '" + self.utilZadatak.parse_number_of_guests(guestNum) + "']")

    def get_allergies_radio(self, allergies):
        match allergies.lower():
            case "yes":
                return self.utilZadatak.get_element_by_css("input[name = 'alergies'][ value= 'Yes']")
            case "no":
                return self.utilZadatak.get_element_by_css("input[name = 'alergies'][ value= 'No']")
            case "maybe":
                return self.utilZadatak.get_element_by_css("input[name = 'alergies'][ value= 'Maybe']")
            case _:
                raise Exception("Invalid entry in click_allergies_radio()")

    def get_allergies_checkbox(self, allergy):
        return self.utilZadatak.get_element_by_css("input[type='checkbox'][ value= " + allergy + "]")

    def get_organize_button(self):
        return self.utilZadatak.get_element_by_css(".btn.btn-primary.px-5.py-3")

    def get_celebrant_from_modal(self):
        return self.utilZadatak.get_element_by_css("#cbr").text

    def get_organizer_from_modal(self):
        return self.utilZadatak.get_element_by_css("#orr").text

    def get_age_from_modal(self):
        return self.utilZadatak.get_element_by_css("#agr").text

    def get_date_from_modal(self):
        return self.utilZadatak.parse_date(self.utilZadatak.get_element_by_css("#dtr").text)

    def get_time_from_modal(self):
        return self.utilZadatak.get_element_by_css("#tmr").text

    def get_guests_from_modal(self):
        return self.utilZadatak.get_element_by_css("#gur").text

    def get_allergies_from_modal(self):
        return self.utilZadatak.get_element_by_css("#alr").text

    #   Setters:
    def set_organizer_textbox(self, name):
        self.get_organizer_textbox().clear()
        self.get_organizer_textbox().send_keys(name)

    def set_birthday_person_textbox(self, name):
        self.get_birthday_person_textbox().clear()
        self.get_birthday_person_textbox().send_keys(name)

    def set_age_of_pb_textbox(self, age):
        self.get_age_of_pb_textbox().clear()
        self.get_age_of_pb_textbox().send_keys(age)

    def set_date_picker(self, date):
        self.get_date_picker().clear()
        self.get_date_picker().send_keys(date)

    # TODO: probaj da ovo bude pikovano, a ne send keys
    def set_time_picker(self, time):
        self.get_time_picker().clear()
        self.get_time_picker().send_keys(time)

    # TODO: Neka sve klik metode provere stanje pre upotrebe, pa napravi check/uncheck metode gde treba
    def click_organize_button(self):
        self.get_organize_button().click()

    def click_allergies_radio(self, allergies):
        self.get_allergies_radio(allergies).click()

    def click_allergies_checkbox(self, allergy):
        self.get_allergies_checkbox(allergy).click()

    def click_number_of_guests_button(self):
        self.get_number_of_guests_button().click()

    def click_number_of_guests_selection(self, guestNum):
        self.get_number_of_guests_selection(guestNum).click()
