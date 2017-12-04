from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26
import time

@given(u'valid url address')
def step_impl(context):
    context.url = 'http://www.tiendeo.com'

@when(u'navigate to the url on a browser')
def step_impl(context):
    try:
        context.browser.get(context.url)
        time.sleep(4)
        assert True is not False
    except:
        assert False

@then(u'should load the webpage')
def step_impl(context):
    WebDriverWait(context.browser,30).until(EC.title_contains('Tiendeo | '))
    assert context.failed is False