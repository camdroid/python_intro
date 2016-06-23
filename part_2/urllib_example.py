import urllib.request
from secrets import api_key
import json


def simple_example():
    url = 'http://google.com'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page)


def api_example():
    url = 'http://api.brewerydb.com/v2/brewery/noGtDY?key={}'.format(api_key)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page)


def api_json_example():
    url = 'http://api.brewerydb.com/v2/brewery/noGtDY?key={}'.format(api_key)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        data = json.loads(the_page.decode('utf-8'))
    # print(data)
    return data


res = api_json_example()
