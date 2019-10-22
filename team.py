import json
import re
import requests
import math


class Team():
    def __init__(self, id):
        '''
        Calls to the API which has the return casted into a JSON object. Dictionaries are created with static JSON calls preceeding the custom calls for ranks and statistics.
        '''
        req = json.loads(requests.get('https://statsapi.web.nhl.com/api/v1/teams/'+ str(id) + '?expand=team.stats').text)
        v_dict = req['teams'][0]['teamStats'][0]['splits'][0]['stat'] #statistic value
        r_dict = req['teams'][0]['teamStats'][0]['splits'][1]['stat'] #team ranking in that particular statistic

        self.id = req['teams'][0]['id']
        self.name = req['teams'][0]['name']
        self.abrv = req['teams'][0]['abbreviation']

        '''
        Loop through all of the statistics and assign them to class variables.
        
        The details for the statistics can be viewed at the official API: https://github.com/dword4/nhlapi
        
        There are two loops: the first assigns the statistics themselves while the second assigns the rankings in each statistic.
        
        To call an attribute, call the object and then the associated value from the API. If it is a rank statistic, it is preceeded by a 'r_'
        
        IE: team = Team(15)
        print(team.r_wins) #rank will be returned
        print(team.wins) #number of wins will be returned.
        '''
        for k, v in v_dict.items():
            setattr(self, k, v)

        for k, v in r_dict.items():
            v = int(re.sub(r'\D', '', v))
            setattr(self, 'r_'+k, v)

        # The API does not include these by default. They will need necessary to calculate the P. Exception.
        # The attributes of a team object are dynamically generated. The below code will throw an error, disregard.
        self.totalGoals = math.ceil((self.gamesPlayed * self.goalsPerGame)) #Rounds up
        self.totalGoalsAllowed = math.ceil((self.gamesPlayed * self.goalsAgainstPerGame)) #Rounds up
        self.pyExp = py_exp(self.totalGoals, self.totalGoalsAllowed)
        self.winPerc = (self.wins / self.gamesPlayed)

'''
Calculates the Pythagorean Expectation given the goals a team has scored and how many they have allowed.
'''
def py_exp(goals_scored, goals_allowed):
    exp = 2
    goal_exp = goals_scored ** exp
    goals_allowed_exp = goals_allowed ** exp
    return goal_exp / (goal_exp + goals_allowed_exp)
