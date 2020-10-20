# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:20:44 2020

@author: Vaseem Naazleen Shaik
"""


import requests
import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime



class User:
    def ratings(self, name):
        # Code Forces API for getting ratings list
        url = "https://codeforces.com/api/user.rating?handle=" 
        url += name
        
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print("Bad Response: " + str(response.status_code))
            return
        
        ratings_json = json.loads(response.text)
        if len(ratings_json['result']) == 0:
            print("No Ratings yet!")
            return
    
        user_ratings = []
        time = []
        for rating in ratings_json['result'][1:]:
            user_ratings.append(rating["newRating"])
            time.append(rating["ratingUpdateTimeSeconds"])
            
        time = [datetime.fromtimestamp(t) for t in time]
        time = [t.strftime("%B-%d") for t in time]
        time = [t[0:3]+t[t.index('-'):] for t in time]
        
        if len(user_ratings) > 25:
            user_ratings = user_ratings[-25:]
            time = time[-25:]
            
        user_ratings = np.array(user_ratings)
        time = np.array(time)

        plt.figure(figsize=(len(user_ratings),5))
        plt.plot(time,user_ratings, marker="o")
        plt.title(name + "'s Ratings")
        

if __name__ == "__main__":
    user = User()
    username = input()
    user.ratings(username)
        
        
