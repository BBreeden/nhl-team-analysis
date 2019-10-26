import nhl_sch_request
import get_nhl_team_stats
import pandas as pd
from datetime import datetime
import os

'''
Gets the JSON object that returns data associated with the NHL games that take place today.
'''
def init():
    return nhl_sch_request.get_request()

'''
Returns today's date in the YYYY-MM-DD format.
'''
def get_today():
    return str(datetime.today().strftime('%Y-%m-%d'))

'''
A simple greeting (with the current date) to be displayed when the script runs.
'''
def greeting():
    print('Good morning and welcome to your scouting report.')
    print(get_today())

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

    #Report generation start
    report = open('report.txt', 'w+')
    report.write((get_today()) + '\n')

    for i, game in enumerate(games): #loops through each game
        away = req['dates'][0]['games'][i]['teams']['away']['team']['name']
        home = req['dates'][0]['games'][i]['teams']['home']['team']['name']

        away_stats = stats.loc[stats['name'] == away]
        home_stats = stats.loc[stats['name'] == home]

        for column in home_stats:
            report.write('{} {} {} {} {}'.format(away_stats.iloc[0]['abrv'], '-', column, '-', away_stats.iloc[0][column]) + '\n')
            report.write('{} {} {} {} {}'.format(home_stats.iloc[0]['abrv'], '-', column, '-', home_stats.iloc[0][column]) + '\n')
            report.write('-----' + '\n')
        
        report.write('-------------------------------------------' + '\n')
    
    report.close()
    print('Report generation complete.')
    #Report generation end


if __name__ == '__main__':
    greeting()
    get_playing_team_stats(init())