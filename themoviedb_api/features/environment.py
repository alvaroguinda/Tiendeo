from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
import json

def before_all(context):
    try:
        context.browser = webdriver.Chrome()
    except WebDriverException:
        context.browser = webdriver.Firefox()

    context.API_KEY = '2684d7e10e4ff5a1c7eda4112f74b4e8'
    context.API_KEY_INVALID = '2684d7e10e4ff5a1c7eda4112f74b4e9'
    context.SESSION_ID = 'bc731bd9b6a36e5496354777be991f746afddf44'
    context.SESSION_ID_INVALID = 'bc731bd9b6a36e5496354777be991f746afddf45'

def after_all(context):
    context.browser.quit()