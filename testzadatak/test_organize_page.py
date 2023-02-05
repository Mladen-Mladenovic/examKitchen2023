from basezadatak.config_zadatak import Config_zadatak

organizePage = Config_zadatak.organizePage
utilZadatak = organizePage.utilZadatak
driver = organizePage.driver


class Test_organize_page(Config_zadatak):

    def test_setup(self):
        global url
        url = utilZadatak.data()["organizePage"]["url"]
        driver.maximize_window()

    def test_happy_path(self):
        driver.get(url)
        # Fill in the form
        organizerName = utilZadatak.data()["organizePage"]["Organizer"]
        organizePage.set_organizer_textbox(organizerName)

        birthdayPersonName = utilZadatak.data()["organizePage"]["Birthday_Person"]
        organizePage.set_birthday_person_textbox(birthdayPersonName)

        ageOfCelebrant = utilZadatak.data()["organizePage"]["Age"]
        organizePage.set_age_of_pb_textbox(ageOfCelebrant)

        dateOfEvent = utilZadatak.data()["organizePage"]["Date"]
        organizePage.set_date_picker(utilZadatak.format_date(dateOfEvent))

        timeOfEvent = utilZadatak.data()["organizePage"]["Time"]
        organizePage.set_time_picker(utilZadatak.format_time(timeOfEvent))

        allergiesRadio = utilZadatak.data()["organizePage"]["alergy"]
        organizePage.click_allergies_radio(allergiesRadio)

        allergiesCheckbox = utilZadatak.data()["organizePage"]["alergies"]
        organizePage.click_allergies_checkbox(allergiesCheckbox)

        guestNum = utilZadatak.data()["organizePage"]["Number_Of_People"]
        organizePage.click_number_of_guests_selection(guestNum)

        organizePage.click_organize_button()

        # Assertions on the modal values
        assert organizePage.get_celebrant_from_modal() == birthdayPersonName
        assert organizePage.get_organizer_from_modal() == organizerName
        assert organizePage.get_age_from_modal() == ageOfCelebrant
        assert organizePage.get_date_from_modal() == utilZadatak.format_date(dateOfEvent)
        assert organizePage.get_time_from_modal() == timeOfEvent
        assert organizePage.get_guests_from_modal() == utilZadatak.format_number_of_guests(guestNum, "verify")
        assert organizePage.get_allergies_from_modal() == allergiesRadio

        # Assertions on the local storage values
        assert utilZadatak.get_from_local_storage("Organizer") == organizerName
        assert utilZadatak.get_from_local_storage("Birthday_Person") == birthdayPersonName
        assert utilZadatak.get_from_local_storage("Age") == ageOfCelebrant
        assert utilZadatak.get_from_local_storage("Date") == dateOfEvent
        assert utilZadatak.get_from_local_storage("Time") == timeOfEvent
        assert utilZadatak.get_from_local_storage("Number_Of_People") == utilZadatak.format_number_of_guests(
            guestNum, "verify")
        assert utilZadatak.get_from_local_storage("alergy") == allergiesRadio
        assert utilZadatak.get_from_local_storage("alergies") == allergiesCheckbox
