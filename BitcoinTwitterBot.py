# model scraping for spacepics

import requests
from bs4 import BeautifulSoup as bs
import os
import tweepy as tp 
import time

#Posting to twitter
consumer_key = 'l90Uqef9DemV6UVs2KUp43N3o'
consumer_secret = 'InmRixCRocX3yTJIaxjH94gwMVWq4DtuuEqXuXQ62afzsDSw2O'
access_token = '959960392087867393-9qbzNIcHXYz3bugxD03a8RZBqZ93fcl'
access_secret = 'gxq6RxSc7NriMPFKz1ceUNzkAIKCbH7cmEjMLBNYha0Ii'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


while True:
    #Get Bitcoin Price
    url = 'https://coinmarketcap.com/currencies/bitcoin/'

    # download page for parsing
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    found = soup.find('div', {'class' : 'col-xs-6 col-sm-8 col-md-4 text-left'}). find("span", {"class" : "text-large2"})

    #Update Twitter
    status = time.strftime("%Y-%m-%d %H:%M:%S ") +  "Bitcoin price currently at $" + found.text + " coinmarketcap.com"
    api.update_status(status)
    time.sleep(3600)
    





