# HW2 - Report
### Hope Zobinou
### DATA 440, Fall 2023
### 10/10/2023

# Q1: Collect URIs from Tweets
Extract 1000 unique links from tweets in Twitter. 

Main steps:
* Create a special Twitter account
* Write a Python program that collects English-language tweets that contain links. See [Collecting Tweets](#collecting-tweets).
* Write a Python program that extracts the links shared in tweets. See [Extracting Links from Tweets](#extracting-links-from-tweets).
* Resolve all URIs to their final target URI (i.e., the one that responds with a 200). See [Resolve URIs to Final Target URI](#resolve-uris-to-final-target-uri).
* Save only unique final URIs (no repeats). See [Save Only Unique URIs](#save-only-unique-uris).
  * if after this step, you don't have 1000 unique URIs, go back and gather more until you are able to get at least 1000 unique URIs
* Save this collection of 1000 unique links in a file and upload it to your repo in GitHub -- we'll use it again in [HW3](/fall-2022/homework/hw3/README.md)

## Answer 

The example figure below shows the 1000 unique Twitter links.



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

## Discussion

*You must provide some discussion of every answer. Discuss how you arrived at the answer and the tools you used. Discuss the implications of your answer.*

# Q2

## Answer

## Discussion

# Q3

## Answer

## Discussion

# References

*Every report must list the references that you consulted while completing the assignment. If you consulted a webpage, you must include the URL.*

* Insert Reference 1, <https://www.example.com>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
