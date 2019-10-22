import requests
import nhl_request



request = nhl_request.get_request()
away_id = request['dates'][0]['games'][0]['teams']['away']['team']['id']
home_id = request['dates'][0]['games'][0]['teams']['home']['team']['id']
print('home:', home_id)
print('away', away_id)