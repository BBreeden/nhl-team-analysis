import json
import requests
from datetime import datetime

def get_request():
    return json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/schedule?date=' + get_today()).text)

def get_today():
    return datetime.today().strftime('%Y-%m-%d')