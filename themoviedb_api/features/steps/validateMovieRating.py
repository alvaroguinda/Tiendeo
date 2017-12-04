from behave import *
import requests

@given(u'a valid api_key and movie_id')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/3/movie/278/rating?api_key={0}&session_id={1}'.format(context.API_KEY, context.SESSION_ID)

@when(u'request rating the movie')
def step_impl(context):
    payload = '{"value":5}'
    headers = {'content-type': 'application/json;charset=utf-8'}
    context.response = requests.request("POST", context.URL, data=payload, headers=headers)

@then(u'should return HTTP code 201')
def step_impl(context):
    assert context.response.status_code == 201

@given(u'a non valid api_key and valid movie_id')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/3/movie/278/rating?api_key={0}&session_id={1}'.format(context.API_KEY_INVALID, context.SESSION_ID)

@when(u'request rating the movie with no valid data')
def step_impl(context):
    payload = '{"value":5}'
    headers = {'content-type': 'application/json;charset=utf-8'}
    context.response = requests.request("POST", context.URL, data=payload, headers=headers)

@then(u'should return HTTP code 401')
def step_impl(context):
    assert context.response.status_code == 401

@given(u'a non valid URL')
def step_impl(context):
    context.URL = 'https://api.themoviedb.org/movie/999999999/rating'

@when(u'requesting rating the movie with no valid url')
def step_impl(context):
    payload = '{"value":5}'
    headers = {'content-type': 'application/json;charset=utf-8'}
    context.response = requests.request("POST", context.URL, data=payload, headers=headers)
    print(context.response)

@then(u'should return HTTP code 404')
def step_impl(context):
    assert context.response.status_code == 404