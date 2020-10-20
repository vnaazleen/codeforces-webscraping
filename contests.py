# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:04:03 2020

@author: Vaseem Naazleen Shaik
"""

import requests
import json
import pandas as pd
from datetime import datetime, timedelta


class Contests:
    def list(self, gym=False):
        # Code Forces API for getting contest list
        url = "https://codeforces.com/api/contest.list?gym=" 
        if gym:
            url += "True"
        else:
            url += "False"
        
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print("Bad Response: " + str(response.status_code))
            return
        
        contests_json = json.loads(response.text)
        
        if not len(contests_json['result']):
            print("No upcoming contests!")
            return
        
        upcoming_contests = []
        for contest in contests_json['result']:
            if contest['phase'] == 'BEFORE':
                upcoming_contests.append({
                    'Name': contest['name'],
                    'Duration': str(timedelta(seconds=contest['durationSeconds'])),
                    'Start': str(datetime.fromtimestamp(contest['startTimeSeconds']))
                    })
            
        contests_table = pd.DataFrame.from_dict(upcoming_contests, orient='columns') 
        print(contests_table)

if __name__ == "__main__":
    cf = Contests()
    cf.list()
        
        
        

