from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def before_all(context):
    try:
        context.browser = webdriver.Chrome()
    except WebDriverException:
        context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()