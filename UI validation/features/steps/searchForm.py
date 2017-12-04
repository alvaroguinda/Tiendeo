from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given(u'a valid product')
def step_impl(context):
    context.product = 'Tablet'
    pass

@when(u'search for a product')
def step_impl(context):
    searchElement = context.browser.find_element(by=By.ID, value='search-input')
    searchElement.send_keys(context.product + Keys.RETURN)

@then(u'offers should be related to this product')
def step_impl(context):
    try:
        WebDriverWait(context.browser,30).until(EC.title_contains(context.product))
        assert True is not False
    except:
        assert True is not True