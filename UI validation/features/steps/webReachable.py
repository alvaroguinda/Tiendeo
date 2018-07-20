from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26
import time

@given(u'valid url address')
def valid_url_address(context):
    context.url = 'http://www.tiendeo.com'

@when(u'navigate to the url on a browser')
def navigate_to_the_url_on_a_browser(context):
    try:
        context.browser.get(context.url)
        time.sleep(4)
        assert True is not False
    except:
        assert False

@then(u'should load the webpage')
def should_load_the_webpage(context):
    WebDriverWait(context.browser,10).until(EC.title_contains(u'Comprar en '))
    assert context.failed is False