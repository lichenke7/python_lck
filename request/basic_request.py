import requests
from utils import constants


def basic_request_get(url, headers):
    return requests.get(url, headers=headers)


def request_get(url, headers):
    rl = basic_request_get(url, headers=headers)
    if constants.print_response:
        print(rl.json())
    return rl.json()


def basic_request_post(url, headers, params):
    return requests.post(url, data=params, headers=headers)


def request_post(url, headers, params):
    rl = basic_request_post(url, params=params, headers=headers)
    if constants.print_response:
        print(rl.json())
    return rl.json()
