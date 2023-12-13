# HW8 - Report
### Hope Zobinou
### DATA 440, Fall 2023
### 12/7/2023

# Q1 - Find Popular Twitter Accounts 
Generate a list of at least 50 popular accounts on Twitter. The accounts must be verified, have 10,000+ followers, and have 5000+ tweets.  For example:
* [`@acnwala`](https://twitter.com/acnwala) - is not verified, ~440 followers, ~3200 tweets - *don't include*
* [`@williamandmary`](https://twitter.com/williamandmary) - verified (blue checkmark), 35,000+ followers, 9,000+ tweets - *could include*  

Generate this information manually by visiting individual account pages. You only need at least 50 popular accounts.

Because we're trying to cluster the accounts based on the text in their tweets, you should choose several sets of accounts that are similar (political, tech, sports, etc.) to see if they'll get clustered together later.

Save the list of accounts (screen_names), one per line, in a text file named `accounts.txt` and upload to your GitHub repo.

*B: What topics/categories do the accounts belong to?  You don't need to specify a grouping for each account, but what general topics/categories will you expect to be revealed by the clustering? Provide a this list before generating your clusters*

## Answer
The accounts I gathered belong to a few different categories. Those are pop culture/hip-hop news accounts, basketball, memes, and video games.   

## Discussion
I obtained these accounts by scrolling down my for you page on Twitter and added the accounts that meet the Professor's requirements. 

# Q2 - Create Account-Term Matrix
Before we can run the clustering code from the PCI book, we have to build an account-term matrix (like the [blog-term matrix](https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/blogdata.txt) in the Module 12 slides). Consider the Twitter accounts equivalent to blogs, and all account tweets, the words of the blog.

Once complete, `generate_tweet_vector.py` will produce two files that you need to upload to your GitHub repo:
* `popular_terms.txt` - the list (one per line) of the 500 most frequent terms in the tweets
* `tweet_term_matrix.txt` - the generated account-term matrix

Once `tweet_term_matrix.txt` has been generated, you can use it in place of `blogdata.txt` in the example code to complete the remaining parts of this assignment.

*A: Explain the general operation of generate_tweet_vector.py and how the tweets are converted to the account-term matrix.*

*B: Explain in detail the code that you added to filter for the 500 most frequent non-stopword terms.*

*C: Do the 500 most frequent terms make sense based on the accounts that you chose?*

## Answer
A: Generate_tweet_vector.py uses tweet_parser which uses scrape_twitter which uses playwright to navigate through each twitter account and collect tweets. Genereate_tweet_vector.py reads a list of accounts and it parses their account to collect a certain amount of tweets for every account on the list. Then It takes the tweets and removes links, tokenizes the tweet, and removes stop words. The words are put in dictionaries that describe their frequency and account usage. The dictionaries and lists are used to create the account-term matrix.   

B: Filtered_counts is a dictionary that collects words that are in sumcounts and wordlist. Wordlist is a list of words that are not stopwords. Then sorted_words sorts the words that were previously filtered out. Popularlist is a list that stores the top 500 of the sorted_words. 

C: Yes

```python
#Loops over key, value pair in the dict 
    filtered_counts = {word: count for word, count in sumcounts.items() if word in wordlist} #Filter out stopwords and keep only words in wordlist

    sorted_words = sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True) #Sort the words by frequency in descending order

    popularlist = [word for word, count in sorted_words[:500]] #Select the top 500 words
```
## Discussion
Since sumcounts holds all the words and frequencies, I used that as the backbone for this code snippet. I used dictionary comprehension to create a dictionary that will hold words and frequencies of sumcount but the stop words are filtered out. "If word in wordlist" is the condition that made it possible. Next I sorted the words from filtered_counts. filtered_counts.items() returns a list of tuples, where each tuple is a key-value pair (word and its count). The lambda part makes sure that it is being sorted by the second element in the tuple (count). Lastly, I stored the results from sorted_words in popularlist. 

# Q3

## Answer

## Discussion

# References

* Reference 1, <>
* Reference 2, <>
