# 爬虫下载工具包

import logging
from time import sleep

import requests

_request = requests.request
_get = requests.get
_post = requests.post
ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/' \
     '537.36(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'


def request(*args, **kwargs):
    headers = kwargs.get('headers', {})
    if 'user-agent' not in headers:
        headers['user-agent'] = ua
    try:
        return _request(*args, **kwargs)
    except requests.exceptions.ConnectionError:
        logging.error("ConnectionError已捕捉，120s后重试")
        sleep(120)
        return _request(*args, **kwargs)


def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
