from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given(u'a correct webpage')
def a_correct_webpage(context):
    WebDriverWait(context.browser,10).until(EC.title_contains('Barcelona'))
    pass

@when(u'navigating on webpage')
def navigating_on_webpage(context):
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
def should_exist_category_navigation_bar(context):
    assert context.existMenu is not False

@then(u'should exist top offer section')
def should_exist_top_offer_section(context):
    assert context.existOffers is not False

@then(u'should exist top stores')
def should_exist_top_stores(context):
    assert context.existTopRetailers is not False

@then('should exist suscribe alert')
def should_exist_suscribe_alert(context):
    assert context.existAlertTiendeo is not False

@then(u'should exist top categories')
def should_exist_top_categories(context):
    assert context.existTopCategories is not False

@then(u'should exist starred products')
def should_exist_starred_products(context):
    assert context.existTopProducts is not False

@then(u'should exist comercial shop center list')
def should_exist_comercial_shop_center_list(context):
    assert context.existMalls is not False

@then(u'should exist location information')
def should_exist_lcoation_information(context):
    assert context.existLocationDescr is not False

@then(u'should exist tiendeo information')
def should_exist_tiendeo_information(context):
    assert context.existAbout is not False

@then(u'should exist tiendeo international links')
def should_exist_tiendeo_internation_links(context):
    assert context.existInternational is not False

@then(u'should exist tiendeo mobile app')
def should_exist_tiendeo_mobile_app(context):
    assert context.existAppDownload is not False