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



*If you want to include code in your report, you can insert a screenshot (if it's legible), or you can copy/paste the code into a fenced code block.*

```python
#!/usr/local/bin/python3
# testargs.py

import sys

print ("{} is the name of the script." . format(sys.argv[0]))
print ("There are {} arguments: {}" . format(len(sys.argv), str(sys.argv)))

for ind, arg in enumerate(sys.argv):
    print ("[{}]: {} {}".format(ind,arg,sys.argv[ind]))
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
