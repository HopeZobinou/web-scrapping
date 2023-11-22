import os
import time
import pandas as pd
import requests
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright
from scrape_twitter import get_auth_twitter_pg
from scrape_twitter import post_tweet
from NwalaTextUtils.textutils import readTextFromFile

#songs_path = 'c:/Users/hopez/Documents/Data440/Homework6/song_infos.csv'
df = pd.read_csv('c:/Users/hopez/Documents/Data440/Homework6/song_infos.csv')

def post_song_tweet(browser_dets, song_data):
    song_info = f"🎵 {song_data['song name']} by {song_data['artist name']} ({song_data['genre']}) 🕒 Duration: {song_data['duration']} 📅 Released: {song_data['date']}"
    
    post_tweet(browser_dets, song_info)
    print(f"Tweet posted: {song_info}")

unsafe_cred_path = 'c:/Users/hopez/Documents/Data440/Homework6/twitter_creds.txt'
twitter_account = 'xmcgeen'

with sync_playwright() as playwright:
    browser_dets = get_auth_twitter_pg(playwright, unsafe_cred_path=unsafe_cred_path)

    if not browser_dets:
        print("Authentication Failed!")
        exit()

    while True:
        #Loops through the data frame and posts the tweets 
        for _, row in df.iterrows():
            post_song_tweet(browser_dets, row)
            time.sleep(60) #Sleep for 1 min before next tweet