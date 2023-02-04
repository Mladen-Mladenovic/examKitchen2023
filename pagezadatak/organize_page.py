from basezadatak.util_zadatak import get_element_by_css, parse_number_of_guests, parse_date


#   Getters:
def get_organizer_textbox():
    return get_element_by_css("input[placeholder = 'Who is organizing birthday']")


def get_birthday_person_textbox():
    return get_element_by_css("input[placeholder = 'Who is having birthday']")


def get_age_of_pb_textbox():
    return get_element_by_css("#age")


def get_date_picker():
    return get_element_by_css("#date")


def get_time_picker():
    return get_element_by_css("#time")


def get_number_of_guests_button():
    return get_element_by_css("#persons")


def get_number_of_guests_selection(guestNum):
    return get_element_by_css("option[ value= '" + parse_number_of_guests(guestNum) + "']")


def get_allergies_radio(allergies):
    match allergies.lower():
        case "yes":
            return get_element_by_css("input[name = 'alergies'][ value= 'Yes']")
        case "no":
            return get_element_by_css("input[name = 'alergies'][ value= 'No']")
        case "maybe":
            return get_element_by_css("input[name = 'alergies'][ value= 'Maybe']")
        case _:
            raise Exception("Invalid entry in click_allergies_radio()")


def get_allergies_checkbox(allergy):
    return get_element_by_css("input[type='checkbox'][ value= " + allergy + "]")


def get_organize_button():
    return get_element_by_css(".btn.btn-primary.px-5.py-3")


def get_celebrant_from_modal():
    return get_element_by_css("#cbr").text


def get_organizer_from_modal():
    return get_element_by_css("#orr").text


def get_age_from_modal():
    return get_element_by_css("#agr").text


def get_date_from_modal():
    return parse_date(get_element_by_css("#dtr").text)


def get_time_from_modal():
    return get_element_by_css("#tmr").text


def get_guests_from_modal():
    return get_element_by_css("#gur").text


def get_allergies_from_modal():
    return get_element_by_css("#alr").text


#   Setters:
def set_organizer_textbox(name):
    get_organizer_textbox().send_keys(name)


def set_birthday_person_textbox(name):
    get_birthday_person_textbox().send_keys(name)


def set_age_of_pb_textbox(age):
    get_age_of_pb_textbox().send_keys(age)


def set_date_picker(date):
    get_date_picker().send_keys(date)


# TODO: probaj da ovo bude pikovano, a ne send keys
def set_time_picker(time):
    get_time_picker().send_keys(time)


def click_organize_button():
    get_organize_button().click()


def click_allergies_radio(allergies):
    get_allergies_radio(allergies).click()


def click_allergies_checkbox(allergy):
    get_allergies_checkbox(allergy).click()


def click_number_of_guests_button():
    get_number_of_guests_button().click()


def click_number_of_guests_selection(guestNum):
    get_number_of_guests_selection(guestNum).click()
