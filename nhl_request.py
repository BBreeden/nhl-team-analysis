import json
import requests
from datetime import datetime


'''
A GET request from the api to get the scheduled NHL games for today.
'''
def get_request():
    return json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/schedule?date=' + get_today()).text)

'''
Returns today's date in the YYYY-MM-DD format.
'''
def get_today():
    return datetime.today().strftime('%Y-%m-%d')