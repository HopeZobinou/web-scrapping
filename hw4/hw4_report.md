# HW4 - Report
### Hope Zobinou
### DATA 440, Fall 2023
### 11/2/2023

# Q1 Friendship Paradox on Facebook
Determine if the friendship paradox holds for a user's Facebook account.

*Q: What is the mean, standard deviation, and median of the number of friends that the user's friends have?*  

Create a graph of the number of friends (y-axis) and the friends themselves (x-axis), sorted by number of friends. The friends don't need to be labeled
on the x-axis: 1, 2, 3,..., n should be sufficient. Include the user in the graph in the appropriate sorted position (count the number of their friends) and label as *U*.

*Q: Does the friendship paradox hold for this user and their friends on Facebook?*


## Answer
The mean is 542.673469, the standard deviation is 539.433739, and the median is 396.

Below is the code I used to get the mean, standard deviation, and the median.

```python
import pandas as pd
import numpy as np      
import matplotlib.pyplot as plt 
import seaborn as sns

fb_friends = pd.read_csv('c:/Users/hopez/Documents/Data440/Homework4/friend_count.csv')

fb_friends.describe()
```

![mean_stdd_median](https://github.com/HopeZobinou/data440/assets/81893993/c67539a5-e606-46ee-937a-8f2b8caf7c4e)

|Week|Date|Topic|
|:---|:---|:---|
|1|Sep 1, 3|Introduction, What's Vis and Why Do It?|
|2|Sep 8, 10|Data and Data Cleaning|
|3|Sep 15, 17|Marks and Channels|



## Discussion

# References

* Insert Reference 1, <https://www.example.com>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
