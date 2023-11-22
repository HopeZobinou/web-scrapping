# HW6 - Title
### Hope Zobinou
### DATA 440, Fall 2023 
### 11/21/2023

## Assignment

Social bots have been used to inflate the popularity of political candidates, influence public opinion through the spread of disinformation and conspiracy theories, and manipulate stock prices through coordinated campaigns. The threats posed by malicious actors that utilize social bots are far-reaching, endangering democracy, public health, and the economy.

However, not all bots are bad. In this assignment, you will prove this point by creating a (good) Twitter bot. You will NOT be scored on the complexity or sophistication of the Twitter bot, instead, you will be scored on the **usefulness** and **originality/innovation** of the bot.

Your Twitter bot must [post tweets](https://github.com/anwala/teaching-web-science/tree/main/fall-2023/week-3/twitter-scraper#example-3-post-a-tweet) on a special Twitter account created by you.

 
# Criteria 1. Usefulness

Consider creating a bot to solve or partly solve a problem you care about --- maybe not poverty or crime or income inequality. In other words create a tool to address a need. Provide an argument in your report for the reason your Twitter bot is useful.

## Answer

My bot tweets out a song (including the artists' name, genre, duration, and date) from an underground artist (that is in the hip-hip/rap genre or subgenre) every minute. This bot reads in a data frame with all the song info and it goes down the rows and tweets out each row. Below is the code I used to create the bot and pictures of the results. The code is based on the functions the professor provided-Reference 1. 

```python
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

    if not browser_dets: #Testing of the account is real
        print("Authentication Failed!") 
        exit()

    while True:
        #Loops through the data frame and posts the tweets 
        for _, row in df.iterrows():
            post_song_tweet(browser_dets, row)
            time.sleep(60) #Sleep for 1 min before next tweet
```

![hw6_terminal_pic](https://github.com/HopeZobinou/data440/assets/81893993/c1a7309a-f0ec-4c4b-836b-51b199d506d0)
![tweets_pic2](https://github.com/HopeZobinou/data440/assets/81893993/1f57831f-7ea0-4527-9a53-e2f96cc24fb8)
![tweets_pic](https://github.com/HopeZobinou/data440/assets/81893993/02ee8cb6-6114-45c1-a99f-6c92f3a67dd8)

## Discussion

This bot solves the problem of underground artists not having their music promoted for free and solves the problem of people wanting to find new music to listen to that isn't mainstream. The problem isn't a major one but it does make it convenient for consumers and artists especially when you follow the bot account and turn post notifications on. Consumers are introduced to new music by new up-and-coming artists and artists are getting their music promoted for free. The tweet per minute is for test purposes. Theoretically, it should be a tweet per hour or 2.    

# Q2

## Answer

## Discussion

# Q3

## Answer

## Discussion

# References

* Reference 1, <https://github.com/anwala/teaching-web-science/tree/main/fall-2023/week-3/twitter-scraper#example-3-post-a-tweet>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
