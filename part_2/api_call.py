import urllib.request
import urllib.parse
from secrets import api_key
import json


def api_get(url, path='', params={}):
    params['key'] = api_key
    params = urllib.parse.urlencode(params)
    full_url = '{}{}?{}'.format(url, path, params)
    return api_call(full_url)


def api_post(url, path, data):
    pass


def api_call(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        data = json.loads(the_page.decode('utf-8'))
    if data['status'] == 'success':
        data = data['data']
        return data
