import requests
from common.config_value import config
import random


def get_token(grant_type, appid, secret):
    url = 'cgi-bin/token'
    get_data = {'grant_type': grant_type, 'appid': appid,
                'secret': secret}
    response = requests.get(url=config.hosts + url, params=get_data).json()
    return response


def get_success_token():
    res = get_token(config.grant_type, config.appid, config.secret)
    token = res['access_token']
    return token


def create_tag(token, tag_name):
    token = get_success_token()
    url = 'cgi-bin/tags/create'
    get_data = {'access_token': token}
    post_data = {'tag': {'name': tag_name}}
    response = requests.post(url=config.hosts + url, params=get_data, json=post_data).json()
    return response



if __name__ == '__main__':
    print(get_token())
