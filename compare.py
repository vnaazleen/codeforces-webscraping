# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:20:05 2020

@author: dell
"""
import requests
import json
from matplotlib import pyplot as plt

def compare(user1, user2):
    url = 'https://codeforces.com/api/user.rating?handle='
    url1= url + user1
    url2= url + user2

    resp1 = requests.get(url1, timeout=5)
    resp2 = requests.get(url2, timeout=5)

    
    if resp1.status_code != 200 or resp2.status_code != 200:
        print("Bad Reqeust!")
        
    ratingJson1 = json.loads(resp1.text)
    ratingJson2 = json.loads(resp2.text)

    ratingdata1=[]
    ratingdata2=[]
    
    for rating in ratingJson1['result']:
        ratingdata1.append(rating['newRating'])
        
    for rating in ratingJson2['result']:
        ratingdata2.append(rating['newRating'])

    
    plt.plot(ratingdata1, marker="o")
    plt.plot(ratingdata2, marker="*")

    plt.show()
    
username1 = input()
username2 = input()
compare(username1, username2)
