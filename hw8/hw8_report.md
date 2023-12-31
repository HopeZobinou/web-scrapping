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
Since sumcounts holds all the words and frequencies, I used that as the backbone for this code snippet. I used dictionary comprehension to create a dictionary that will hold words and frequencies of sumcount but the stop words are filtered out-reference 1. "If word in wordlist" is the condition that made it possible. Next I sorted the words from filtered_counts. filtered_counts.items() returns a list of tuples, where each tuple is a key-value pair (word and its count). The lambda part makes sure that it is being sorted by the second element in the tuple (count). Lastly, I stored the results from sorted_words in popularlist. 

# Q3 - Create Dendrogram
Create an ASCII dendrogram *and* a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see Module 12, slides 21, 23).  Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

*A: How well did the hierarchical clustering do in grouping similar accounts together?  Were there any particularly odd groupings?*

## Answer
The hierarchical clustering did a good job of grouping similar accounts together. The only odd grouping I see is charlieintel being grouped with meme twitter accounts. It should be grouped with video game new accounts like valorant, inteledl, fncompreport, and valorintel.

Below is the JPEG dendrogram.
![accountclust](https://github.com/HopeZobinou/data440/assets/81893993/4389b3db-39d3-4fea-b846-1374c10279a0)

## Discussion
I used the code the professor provided to create the dendrogram-reference 2. I read in the twitter matrix file and used the clustering functions. 

# Q4 - Cluster using k-Means
Cluster the accounts using k-Means, using `k`=5,10,20 (see Module 12, slide 34).  For each value of `k`, create a file that lists the accounts in each cluster and upload to your GitHub repo.  

*A: Give a brief explanation of how the k-Means algorithm operates on this data.  What features is the algorithm considering?*

*B: How many iterations were required for each value of `k`?*

*C: Which `k` value created the most reasonable clusters?  For that grouping, characterize the accounts that were clustered into each group.*

## Answer
A: 

B: For k = 5, there were 7 iterations. For k = 10, there were 4 iterations. For k = 20, there were 3 iterations.

C: K = 10 created the most reasonable clusters. Cluster 0 has pop/hiphop culture news accounts, cluster 1 has meme twitter accounts, cluster 2 has nba/basketball accounts, cluster 3 has more popular meme accounts, cluster 4 has nba accounts, cluster 5 has hip hop culture news accounts, cluster 6 has gaming news accounts, cluster 7 has basketball accounts, cluster 8 has a call of duty league news account, and cluster 9 has more popular basketball accounts.

Below is the code I used to get my results.

```python
kclust = kcluster(data, k = 5)

for i in range(5):
    print("Cluster", i , ": " , [accounts[r] for r in kclust[i]])
```

## Discussion
I used the kcluster function to get my results. To print my results I made a for loop that would print out each account name in each cluster. copied the output and pasted it into a txt file. 

# References

* Reference 1, <https://www.freecodecamp.org/news/dictionary-comprehension-in-python-dict-comprehensions-explained/>
* Reference 2, <https://github.com/anwala/teaching-web-science/blob/main/fall-2022/week-12/data_440_03_f22_mod_12_pci_ch_03.ipynb>
