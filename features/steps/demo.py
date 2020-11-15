from hamcrest import assert_that, equal_to
from behave import given, when, then
import requests
import json

@given('I send a simple GET request')
def step_impl(context):
    response = requests.get(context.base_url + '/get')
    context.response_body = response.json()
    context.status_code = response.status_code

@given('I send a login request')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    payload = {
        'username': context.username, 
        'password': context.password,
        'durable': False
    }
    response = requests.post(context.base_url + '/post', headers=headers, data=json.dumps(payload))
    response_body = response.json()
    assert_that(response_body['json']['durable'], equal_to(False))

@given('I send a simple POST request')
def step_impl(context):
    response = requests.post(context.base_url + '/post')
    context.status_code = response.status_code

@given('I send a predefined JSON body with my POST request')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(context.base_url + '/post',
                             data=open('features/json/demo.json', 'rb'), headers=headers)
    context.response_body = response.json()

@given('I send a modified JSON body with my POST request')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    json_file = open('features/json/demo.json', 'rb')
    data = json.load(json_file)
    data['version'] = 2
    response = requests.post(context.base_url + '/post',
                             data=json.dumps(data), headers=headers)
    context.response_body = response.json()

@given('I send the JSON body with my POST request')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(context.base_url + '/post',
                             data=json.dumps(context.body), headers=headers)
    context.response_body = response.json()

@given('I use "{filename}" as payload')
def step_impl(context, filename):
    headers = {'Content-Type': 'application/json'}
    json_file = open('features/json/' + filename, 'rb')
    context.body = json.load(json_file)

@given('I replace version with "{version}"')
def step_impl(context, version):
    context.body['version'] = version

@given('I replace name with "{name}"')
def step_impl(context, name):
    context.body['name'] = name

@then('the response code is "{code}"')
def step_impl(context, code):
    assert_that(context.status_code, equal_to(int(code)))

@then('response contains version "{version}"')
def step_impl(context, version):
    assert_that(
        int(context.response_body['json']['version']), equal_to(int(version)))

@then('I can pass the response to another request')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(context.base_url + '/post', data=json.dumps(
        {'url': context.response_body['url']}), headers=headers)
    response_body = response.json()
    assert_that(response_body['json']['url'],
                equal_to('http://httpbin.org/get'))