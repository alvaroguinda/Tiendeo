from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given(u'a correct webpage')
def step_impl(context):
    WebDriverWait(context.browser,10).until(EC.title_contains('Barcelona'))
    pass

@when(u'navigating on webpage')
def step_impl(context):
    context.existMenu = False
    try:
        _ = context.browser.find_element(by=By.ID, value="categoriesMenu")
        context.existMenu = True
    except:
        assert True is not True
    context.existOffers = False
    try:
        _ = context.browser.find_element(by=By.ID, value="results-allOffersSection")
        context.existOffers = True
    except:
        assert True is not True
    context.existTopRetailers = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-topRetailers")
        context.existTopRetailers = True
    except:
        assert True is not True
    context.existAlertTiendeo = False
    try:
        _ = context.browser.find_element(by=By.XPATH, value="//div[@class='landing-section landing-alert']")
        context.existAlertTiendeo = True
    except:
        assert True is not True
    context.existTopCategories = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-topCategories")
        context.existTopCategories = True
    except:
        assert True is not True
    context.existTopProducts = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-highlightedProducts")
        context.existTopProducts = True
    except:
        assert True is not True
    context.existMalls = False
    try:
        _ = context.browser.find_element(by=By.XPATH, value="//div[@class='malls']")
        context.existMalls = True
    except:
        assert True is not True
    context.existLocationDescr = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-Description")
        context.existLocationDescr = True
    except:
        assert True is not True
    context.existAbout = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-About")
        context.existAbout = True
    except:
        assert True is not True
    context.existInternational = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-Countries")
        context.existInternational = True
    except:
        assert True is not True
    context.existAppDownload = False
    try:
        _ = context.browser.find_element(by=By.ID, value="landing-appDownload")
        context.existAppDownload = True
    except:
        assert True is not True

@then(u'should exist category navigation bar')
def step_impl(context):
    assert context.existMenu is not False

@then(u'should exist top offer section')
def step_impl(context):
    assert context.existOffers is not False

@then(u'should exist top stores')
def step_impl(context):
    assert context.existTopRetailers is not False

@then('should exist suscribe alert')
def step_impl(context):
    assert context.existAlertTiendeo is not False

@then(u'should exist top categories')
def step_impl(context):
    assert context.existTopCategories is not False

@then(u'should exist starred products')
def step_impl(context):
    assert context.existTopProducts is not False

@then(u'should exist comercial shop center list')
def step_impl(context):
    assert context.existMalls is not False

@then(u'should exist location information')
def step_impl(context):
    assert context.existLocationDescr is not False

@then(u'should exist tiendeo information')
def step_impl(context):
    assert context.existAbout is not False

@then(u'should exist tiendeo international links')
def step_impl(context):
    assert context.existInternational is not False

@then(u'should exist tiendeo mobile app')
def step_impl(context):
    assert context.existAppDownload is not False