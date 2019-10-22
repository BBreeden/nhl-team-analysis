import requests
import nhl_request

'''
Gets the JSON object that returns data associated with the NHL games that take place today.
'''
def init():
    return nhl_request.get_request()

'''
//TODO
Still not quite sure what to do here. Right now, all it does it assign the collection of games to a variable.
'''
def get_games(req):
    games = req['dates'][0]['games'] #fetchs all of the games returned

    for i, game in enumerate(games): #loops through each game
        home_id = req['dates'][0]['games'][i]['teams']['home']['team']['id']
        away_id = req['dates'][0]['games'][i]['teams']['away']['team']['id']
        print('{} @ {}'.format(away_id, home_id))

if __name__ == '__main__':
    req = init()
    get_games(req)
