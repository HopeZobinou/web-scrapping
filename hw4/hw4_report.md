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

Below is the code I used to get the mean, standard deviation, and the median. Also an image of the output.

```python
import pandas as pd
import numpy as np      
import matplotlib.pyplot as plt 
import seaborn as sns

fb_friends = pd.read_csv('c:/Users/hopez/Documents/Data440/Homework4/friend_count.csv')

fb_friends.describe()
```

![mean_stdd_median](https://github.com/HopeZobinou/data440/assets/81893993/c67539a5-e606-46ee-937a-8f2b8caf7c4e)

The friendship paradox does hold for this user (nwala) but it holds for the others.
Below is the code I used to make the graph and the graph itself.

```python
fb_friends['USER'] = range(1,99)
fb_friends.sort_values(by = ' FRIENDCOUNT', ascending = False)
plt.figure(figsize = [8,6])
x = fb_friends['USER']
y = fb_friends[' FRIENDCOUNT']
xlabel = 'Users'
ylabel = 'Number of Friends'

sns.scatterplot(x = x, y = y)

plt.xlabel(xlabel, fontsize = 16, labelpad = 15)
plt.ylabel(ylabel, fontsize = 16, labelpad = 20)

plt.savefig('hw4q1p2.png')
plt.show()
```

![hw4q1p2](https://github.com/HopeZobinou/data440/assets/81893993/aaa965bc-cca4-463f-91c4-1ad14b57a819)


## Discussion
The friendship paradox states that you have fewer friends than your friends. Prof. Nwala has 98 friends which is lower than the average number of friends his friends have (543). The paradox holds for the others because the graph shows that the majority of the friends on Prof. Nwala's friend list are below that blue average line including Prof. Nwala (His point is marked black)-Reference 1. 


# References

* Insert Reference 1, <https://stackoverflow.com/questions/12043672/how-to-take-draw-an-average-line-for-a-scatter-plot>
