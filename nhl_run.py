import json
import requests

request = json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/schedule?date=2019-10-22').text)
away_id = request['dates'][0]['games'][0]['teams']['away']['team']['id']
home_id = request['dates'][0]['games'][0]['teams']['home']['team']['id']
print('home:', home_id)
print('away', away_id)