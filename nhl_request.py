import json
import requests

def get_request():
    return json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/schedule?date=2019-10-22').text)