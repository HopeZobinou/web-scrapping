# HW5 - Report
### Hope Zobinou 
### DATA 440, Fall 2023
### 11/14/23

# Q1. Color nodes based on final split 

Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A or Mr. Hi). This should look similar to the graph on slide 92 - all edges should be present, just indicate the nodes in the eventual split by color.

*Q: How many nodes (students) eventually go with John and how many with Mr. Hi?*


## Answer
16 nodes go to John and 16 nodes go to Mr.Hi.
Below is the code snippet used to split the nodes up by their connections.

```python
nodes_connected_to_1 = list(G.neighbors(1))
nodes_connected_to_34 = list(G.neighbors(34))
list_of_nodes = list(G.nodes())
node_colors = ['purple' if node in nodes_connected_to_1 else 'orange' if node in nodes_connected_to_34 else 'purple' 
               if node == list_of_nodes[16] else 'orange' if node == list_of_nodes[25] else 'orange' if node == list_of_nodes[24] else 'grey' for node in G.nodes()]
node_colors[0] = 'blue' #Mr. Hi (1) 16
node_colors[33] = 'red' #John A (34) 16

nx.draw_spring(G, with_labels = True, node_color = node_colors)
plt.show()
```

Above is an image of the graph before the split.


![before_split](https://github.com/HopeZobinou/data440/assets/81893993/74bc78f9-77fc-4e0f-a567-fbd77bd784da)

## Discussion


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
