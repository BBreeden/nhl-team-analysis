import json
import requests

def get_request():
    return json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/schedule?date=2019-10-22').text)
request =get_request()
away_id = request['dates'][0]['games'][0]['teams']['away']['team']['id']
home_id = request['dates'][0]['games'][0]['teams']['home']['team']['id']
print('home:', home_id)
print('away', away_id)