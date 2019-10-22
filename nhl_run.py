import requests
import nhl_sch_request
import get_nhl_team_stats

'''
Gets the JSON object that returns data associated with the NHL games that take place today.
'''
def init():
    return nhl_sch_request.get_request()

'''
//TODO
Still not quite sure what to do here. Right now, all it does it assign the collection of games to a variable.
'''
def get_playing_team_stats(req):
    games = req['dates'][0]['games'] #fetchs all of the games returned
    stats = get_nhl_team_stats.get_request()
    print(stats)

    for i, game in enumerate(games): #loops through each game
        home_id = req['dates'][0]['games'][i]['teams']['home']['team']['id']
        away_id = req['dates'][0]['games'][i]['teams']['away']['team']['id']
        #get stats for the home and away team and print them side by side
        print('{} @ {}'.format(away_id, home_id))

if __name__ == '__main__':
    req = init()
    get_playing_team_stats(req)