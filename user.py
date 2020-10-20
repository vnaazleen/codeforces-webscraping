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
    def __init__(self, name):
        self.name = name
        
    def about(self):
        url = "https://codeforces.com/api/user.info?handles="
        url += self.name
        
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print("Bad Response: " + str(response.status_code))
            return
        
        user_json = json.loads(response.text)
        
        data = {}
        for i in user_json['result']:
            data['Handle'] = i['handle']
            data['Name'] = i['lastName']
            data['Country'] = i['country']
            data['Rank']= i['rank']
            data['Rating'] = i['rating']
            data['Max Rating'] = i["maxRating"] 
            
        user_info = pd.Series(data)
        print(user_info)        
        
              
        
    def ratings(self):
        # Code Forces API for getting ratings list
        url = "https://codeforces.com/api/user.rating?handle=" 
        url += self.name
        
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
            

        plt.figure(figsize=(len(user_ratings)//2, len(user_ratings)//5))
        plt.plot(user_ratings, marker="o")
        plt.title(self.name + "'s Ratings")
        

if __name__ == "__main__":
    username = "tourist" #input()
    user = User(username)
    user.about()
    user.ratings()
