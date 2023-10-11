# HW2 - Report
### Hope Zobinou
### DATA 440, Fall 2023
### 10/10/2023

# Q1: Collect URIs from Tweets
Extract 1000 unique links from tweets in Twitter. 

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

# Q2

## Answer

## Discussion

# Q3

## Answer

## Discussion


The table below shows a simple table.  

|Week|Date|Topic|
|:---|:---|:---|
|1|Sep 1, 3|Introduction, What's Vis and Why Do It?|
|2|Sep 8, 10|Data and Data Cleaning|
|3|Sep 15, 17|Marks and Channels|

The table below shows an example confusion matrix (you'll see this term later) from <https://en.wikipedia.org/wiki/Confusion_matrix>.

| | |Actual||
|---|---|---|---|
|**Predicted**| |Cat|Dog|
| |Cat|5 (TP)|3 (FP)|
| |Dog|2 (FN)|3 (TN)|

# References

*Every report must list the references that you consulted while completing the assignment. If you consulted a webpage, you must include the URL.*

* Insert Reference 1, <https://www.example.com>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
