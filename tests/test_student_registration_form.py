from selene.support.shared import browser
from selene import have
from selene import command
import os


def given_opened_text_box_page():
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


# DO
def test_submit_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    given_opened_text_box_page()
    browser.element('#firstName').type('Тигран')
    browser.element('#lastName').type('Светов')
    browser.element('#userEmail').type('mrlibertarian@gmail.com')
    male_radiobutton.click()
    browser.element('#userNumber').type('5990807420')
    browser.element('#dateOfBirthInput').perform(command.js.set_value('29 Dec 1996'))
    browser.element('#subjectsInput').type('Ma').press_enter()
    browser.element('#subjectsInput').type('Bi').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_media/kitten.png'))
    browser.element('#currentAddress').type('Tbilisi, Petre Kavtaradze, 22a')
    state_selector.type('NC').press_enter()
    city_selector.type('Noi').press_enter()
    browser.element('#submit').perform(command.js.click)


# ASSERT
def check_submitted_data():
    browser.element('.table-responsive').should(have.text('Тигран Светов'))
    browser.element('.table-responsive').should(have.text('	mrlibertarian@gmail.com'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('5990807420'))
    browser.element('.table-responsive').should(have.text('5990807420'))
    browser.element('.table-responsive').should(have.text('5990807420'))
    browser.element('.table-responsive').should(have.text('5990807420'))
    browser.element('.table-responsive').should(have.text('kitten.png'))
    browser.element('.table-responsive').should(have.text('Tbilisi, Petre Kavtaradze, 22a'))
    browser.element('.table-responsive').should(have.text('NCR Noida'))


state_selector = browser.element('#react-select-3-input')
city_selector = browser.element('#react-select-4-input')
male_radiobutton = browser.element('[for=gender-radio-1]')
