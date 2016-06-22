import urllib.request
import json
from secrets import api_key
full_url = 'http://api.brewerydb.com/v2/brewery/noGtDY?key={}'.format(api_key)

def api_call(url, path, params):
    # Calculate the full url
    req = urllib.request.Request(full_url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        data = json.loads(the_page.decode('utf-8'))
    if data['status'] == 'success':
        response = data['data']
        return response
    raise Exception('Something went wrong')

print(api_call(None, None, None))