from behave import *
from selenium import webdriver

@given(u'a valid api_key')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key={0}'.format(context.API_KEY)

@when(u'requesting movie top rated')
def step_impl(context):
    context.browser.get(context.URL)

@then(u'api should return valid data')
def step_impl(context):
    assert '"page":1' in context.browser.page_source

@given(u'a non valid api_key')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key={0}'.format(context.API_KEY_INVALID)

@when(u'requesting movie top rated with no valid data')
def step_impl(context):
    context.browser.get(context.URL)

@then(u'api return http code error 401')
def step_impl(context):
    assert '"status_code":7' in context.browser.page_source

@given(u'a non api valid URL')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/3/movie/top_rated2?api_key={0}'.format(context.API_KEY)

@when(u'requesting movie top rated with no valid url')
def step_impl(context):
    context.browser.get(context.URL)

@then(u'api should return a HTTP error code 404')
def step_impl(context):
    assert '"status_code":34' in context.browser.page_source
