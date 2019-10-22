import requests
import nhl_sch_request
import get_nhl_team_stats
import pandas as pd

'''
Gets the JSON object that returns data associated with the NHL games that take place today.
'''
def init():
    return nhl_sch_request.get_request()

'''
This function is a bit complex. Refactoring may be needed here. This function does a few things.

1. Fetches all of the games that are scheduled to be played today.
2. Builds a dataframe with stats for all teams.
3. Iterates through the games and pulls the statistics for the teams playing today.
4. Prints the stats side by side for comparison.
'''
def get_playing_team_stats(req):
    games = req['dates'][0]['games'] #fetchs all of the games returned
    stats = get_nhl_team_stats.get_request()

    for i, game in enumerate(games): #loops through each game
        home = req['dates'][0]['games'][i]['teams']['home']['team']['name']
        away = req['dates'][0]['games'][i]['teams']['away']['team']['name']
        home_stats = stats.loc[stats['name'] == home]
        away_stats = stats.loc[stats['name'] == away]
        game_stats = pd.concat([home_stats, away_stats])
        for column in home_stats:
            print('{} {} {} {} {}'.format(home_stats.iloc[0]['abrv'], '-', column, '-', home_stats.iloc[0][column]))
            print('{} {} {} {} {}'.format(away_stats.iloc[0]['abrv'], '-', column, '-', away_stats.iloc[0][column]))
            print('-----')
        
        print('-------------------------------------------')


if __name__ == '__main__':
    req = init()
    get_playing_team_stats(req)