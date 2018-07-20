from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given(u'a valid location')
def a_valid_location(context):
    context.location = 'Barcelona'
    pass

@when(u'select location using form')
def select_location_using_form(context):
    cityDropdownElement = context.browser.find_element(by=By.CLASS_NAME, value='dropdown-city')
    cityDropdownElement.click()
    textElement = context.browser.find_element(by=By.ID, value='city-input')
    textElement.send_keys('Barcelona')
    time.sleep(1)
    textElement.send_keys(Keys.ENTER)

@then(u'should show location information')
def should_show_location_information(context):
    try:
        WebDriverWait(context.browser,30).until(EC.title_contains('Barcelona'))
        time.sleep(5)
        assert True is not False
    except:
        assert True is not True

@then(u'should show location information navbar')
def should_show_location_information_navbar(context):
    cityElement = context.browser.find_element(by=By.CSS_SELECTOR, value=".dropdown.dropdown-city span[@class='dropdown-toggle yamm-dropdown-link'] span[@title='Barcelona']")
    assert cityElement.text == 'Barcelona'

@then(u'should show location description')
def should_show_location_description(context):
    cityDescriptionTitle = context.browser.find_element(by=By.XPATH, value="//section[@id='landing-Description']/div/div[@class='description-title text-center']")
    assert cityDescriptionTitle.text == 'Barcelona'