from pagezadatak.organize_page import *
from basezadatak.util_zadatak import get_from_local_storage, parse_time
from basezadatak.config_zadatak import driver, data


def test_setup():
    global url
    url = data()["organizePage"]["url"]
    driver.maximize_window()


def test_happy_path():
    driver.get(url)
    # Fill in the form
    organizerName = data()["organizePage"]["Organizer"]
    set_organizer_textbox(organizerName)

    birthdayPersonName = data()["organizePage"]["Birthday_Person"]
    set_birthday_person_textbox(birthdayPersonName)

    ageOfCelebrant = data()["organizePage"]["Age"]
    set_age_of_pb_textbox(ageOfCelebrant)

    dateOfEvent = data()["organizePage"]["Date"]
    set_date_picker(parse_date(dateOfEvent))

    timeOfEvent = data()["organizePage"]["Time"]
    set_time_picker(parse_time(timeOfEvent))

    allergiesRadio = data()["organizePage"]["alergy"]
    click_allergies_radio(allergiesRadio)

    allergiesCheckbox = data()["organizePage"]["alergies"]
    click_allergies_checkbox(allergiesCheckbox)

    guestNum = data()["organizePage"]["Number_Of_People"]
    click_number_of_guests_selection(guestNum)

    click_organize_button()

    # Assertions on the modal values
    assert get_celebrant_from_modal() == birthdayPersonName
    assert get_organizer_from_modal() == organizerName
    assert get_age_from_modal() == ageOfCelebrant
    assert get_date_from_modal() == parse_date(dateOfEvent)
    assert get_time_from_modal() == timeOfEvent
    assert get_guests_from_modal() == parse_number_of_guests(guestNum, "verify")
    assert get_allergies_from_modal() == allergiesRadio

    # Assertions on the local storage values
    assert get_from_local_storage("Organizer") == organizerName
    assert get_from_local_storage("Birthday_Person") == birthdayPersonName
    assert get_from_local_storage("Age") == ageOfCelebrant
    assert get_from_local_storage("Date") == dateOfEvent
    assert get_from_local_storage("Time") == timeOfEvent
    assert get_from_local_storage("Number_Of_People") == parse_number_of_guests(guestNum, "verify")
    assert get_from_local_storage("alergy") == allergiesRadio
    assert get_from_local_storage("alergies") == allergiesCheckbox
