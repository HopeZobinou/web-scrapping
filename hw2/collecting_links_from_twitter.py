import gzip
import json
import requests
import sys

from playwright.sync_api import sync_playwright
from scrape_twitter import get_auth_twitter_pg
from scrape_twitter_v2 import stream_tweets
from util import write_tweets_to_jsonl_file

def get_twitter_links(search_term, max_tweets):
    final_links = []
    unique_links = []

    with sync_playwright() as playwright:
        browser_dets = get_auth_twitter_pg(playwright) #Opens the browser and navigates through twitter

        if( len(browser_dets) != 0 ):
            tweets = stream_tweets(browser_dets, search_term, max_tweets) #Collects tweets w/ URIs from search    

        for i in tweets: #Gets the final URI from each link
            r = requests.get(i)
            final_links.append(r.url)   

        [unique_links.append(x) for x in final_links if x not in unique_links] #Gets the unique links  

        print('unique links:') 

        for k in unique_links: #Prints the links
            print(k) 

    return unique_links   

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("2 arguments are required, the file name, search term, max number of tweets.")
        sys.exit(1)

    get_twitter_links(sys.argv[1], sys.argv[2]) 