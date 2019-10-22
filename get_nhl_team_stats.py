import json
import requests
import team
import pandas as pd

def get_request():
    ids = get_team_ids()
    features = get_team_features()

    #Collect all of the data for the teams and add them to the dataframe.
    team_stats_all = []
    for id in ids:
        print('Team id found: ', id)
        team_stats = []
        t = team.Team(id)
        for attr, value in t.__dict__.items():
            team_stats.append(value)
        team_stats_all.append(team_stats)
    
    #Construct, index, and return the data frame.
    df = pd.DataFrame(team_stats_all, columns = features)
    df.set_index('id', inplace=True)
    return df

def get_team_ids():
    req = json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/teams').text)
    teams = req['teams']
    id_list = []
    for team in teams:
        id_list.append(team['id'])
    return id_list

def get_team_features():
    model_team = team.Team(1) #Any id can be used here, defaulted to 1.
    return [attr for attr, value in model_team.__dict__.items()]