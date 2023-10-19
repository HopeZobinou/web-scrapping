# HW2 - Report
### Hope Zobinou  
### DATA 440, Fall 2023 
### 10/10/2023

# Q1: Collect URIs from Tweets
Extract 1000 unique links from tweets in Twitter. 

Main steps:

Create a special Twitter account
Write a Python program that collects English-language tweets that contain links. See Collecting Tweets.
Write a Python program that extracts the links shared in tweets. See Extracting Links from Tweets.
Resolve all URIs to their final target URI (i.e., the one that responds with a 200). See Resolve URIs to Final Target URI.
Save only unique final URIs (no repeats). See Save Only Unique URIs.
if after this step, you don't have 1000 unique URIs, go back and gather more until you are able to get at least 1000 unique URIs
Save this collection of 1000 unique links in a file and upload it to your repo in GitHub -- we'll use it again in HW3

## Answer 

The example figure below shows the 1000 unique Twitter links.

![q1_links](https://github.com/HopeZobinou/data440/assets/81893993/fd0cf5e2-cf09-4dd5-93e4-c0f29ac91448)

Below is the code that helped me do it 

```python
import gzip
import json
import requests

from playwright.sync_api import sync_playwright
from scrape_twitter import get_auth_twitter_pg
from scrape_twitter_v2 import stream_tweets
from util import write_tweets_to_jsonl_file

if __name__ == "__main__":
    final_links = []
    unique_links = []

    with sync_playwright() as playwright:
        browser_dets = get_auth_twitter_pg(playwright) #Opens the browser and navigates through twitter

        if( len(browser_dets) != 0 ):
            tweets = stream_tweets(browser_dets, 'Biden', max_tweets = 100) #Collects tweets w/ URIs from search

        for i in tweets: #Gets the final URI from each link
            r = requests.get(i)
            final_links.append(r.url)  

        [unique_links.append(x) for x in final_links if x not in unique_links] #Gets the unique links

        print('unique links:')

        for k in unique_links: #Prints the links
            print(k)   
```

## Discussion
Getting that many links was time-consuming and hard to understand at first. For my program, I based it on Professor Nwala's work from 
class. Reference 1 & 2. The functions to get the tweets are from him. For some reason, I couldn't get the write json function to work 
so I made the program collect the links in a list and print them to the screen. After that, I copied the links that weren't video/audio
related or links that linked to twitter and pasted them into Notepad++. In Notepad++, I got rid of the duplicate links.

# References

*Reference 1, <https://github.com/anwala/teaching-web-science/tree/main/fall-2023/week-3/twitter-scraper#example-2-extract-tweets-from-search>
*Reference 2, <https://github.com/anwala/teaching-web-science/blob/main/fall-2023/week-3/twitter-scraper/process_tweets.py>
