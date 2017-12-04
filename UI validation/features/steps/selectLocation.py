from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given(u'a valid location')
def step_impl(context):
    context.location = 'Barcelona'
    pass

@when(u'select location using form')
def step_impl(context):
    cityDropdownElement = context.browser.find_element(by=By.XPATH, value='//header/nav/div/div/ul/li')
    cityDropdownElement.click()
    textElement = context.browser.find_element(by=By.ID, value='city-input')
    textElement.send_keys('Barcelona')
    time.sleep(1)
    textElement.send_keys(Keys.ENTER)

@then(u'should show location information')
def step_impl(context):
    try:
        WebDriverWait(context.browser,30).until(EC.title_contains('Barcelona'))
        time.sleep(5)
        assert True is not False
    except:
        assert True is not True

@then(u'should show location information navbar')
def step_impl(context):
    cityElement = context.browser.find_element(by=By.XPATH, value='//header/nav/div/div/ul/li/span/span')
    assert cityElement.text == 'Barcelona'

@then(u'should show location description')
def step_impl(context):
    cityDescriptionTitle = context.browser.find_element(by=By.XPATH, value="//section[@id='landing-Description']/div/div[@class='description-title text-center']")
    assert cityDescriptionTitle.text == 'Barcelona'