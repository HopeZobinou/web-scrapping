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

### Q2. Get TimeMaps for Each URI

Obtain the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs from Q1 using the ODU Memento Aggregator, [MemGator](https://github.com/oduwsdl/MemGator).

Finally, upload the TimeMaps to your GitHub repo -- you'll also use these for Q3.  Put them in a separate folder, not the same folder as your report.

## Answer

Below is the code used to make the time maps for each URI.

```python
import requests
import json
import subprocess
import sys

def file_to_list(file_path):
    file_path = file_path
    links = []

    # Open the file in read mode and read its lines
    # Puts every line in the file into a list.
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    links = [item.strip() for item in links] #Removes the \n

    if not file.closed:
        file.close()

    return links

def to_time_maps(links):
    links = links
    for link in links:
        try:
            # Run MemGator to get the TimeMap JSON and store the result in a file
            output_file = f"{link.replace('://', '_').replace('/', '_').replace('?', '_').replace('#', '_').replace('%','_').replace('&','_').replace('{','_').replace('}','_').replace('<','_').replace('>','_').replace('*','_').replace('$', '_').replace('!','_').replace(':','_').replace('@','_').replace('+','_').replace('|','_').replace('=','_')}_timemap.json"
            subprocess.run(["c:/Users/hopez/Documents/Data440/Homework2/memgator-windows-amd64","-f", "json", link], stdout = open(output_file, "w"), text=True, check=True)
            print(f"TimeMap JSON for {link} has been saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running MemGator for {link}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    #Path to the txt file "c:/Users/hopez/Documents/Data440/Homework2/twitter_links.txt" 

    if len(sys.argv) != 2:
        print("2 arguments are required, the file name and path to the links.")
        sys.exit(1)

    links = file_to_list(sys.argv[1])

    to_time_maps(links[0:1000]) #000-999
```

## Discussion

At first, I had all the links on a txt file and in order for me to get time maps from them I had to store them into a list on Python and perform the time map commands on each individual element in said list. I created a function that opens the txt file and appends an empty list with each line on the txt file. Next, I created a function that iterates over a list and performs memgator on each element. Since memgator only works on the command line I used the subprocess library to perform command line arguments in the python script—reference 3. I was only able to obtain 976 time maps. The missing time maps are due to the link just not working with memgator, a timeout error, or that link being a git link. The folder labeled time_maps contains 974 time maps. I had to remove 2 due to them being too big to upload.

### Q3. Analyze Mementos Per URI-R.

Use the TimeMaps you saved in Q2 to analyze how well the URIs you collected in Q1 are archived. Create a table showing how many URI-Rs have certain number of mementos.  For example

|Mementos | URI-Rs |
|---------:|--------:|
|   0     |  750   |
|   1     |  100   |
|   7     |   50   |
|   12     |   25   |
|   19     |   25   |
|   24     |  20  |
|   30     |   27   |
|  57     |    3   |

*Q: What URI-Rs had the most mementos?  Did that surprise you?*

## Answer

|Mementos | URI-Rs |
|---------:|--------:|
|   0     |  500   |

# References

*Reference 1, <https://github.com/anwala/teaching-web-science/tree/main/fall-2023/week-3/twitter-scraper#example-2-extract-tweets-from-search>
*Reference 2, <https://github.com/anwala/teaching-web-science/blob/main/fall-2023/week-3/twitter-scraper/process_tweets.py>
*Reference 3, <https://stackoverflow.com/questions/450285/executing-command-line-programs-from-within-python>
