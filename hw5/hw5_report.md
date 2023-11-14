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

Below is an image of the graph.


![before_split](https://github.com/HopeZobinou/data440/assets/81893993/74bc78f9-77fc-4e0f-a567-fbd77bd784da)

## Discussion
After creating the graph with 'G = nx.karate_club_graph()' I remapped the nodes so instead of it being 0-33, it's 1-34. Next, I used the neighbors method to get the list of neighbors for Mr. Hi and John respectively. Once I got both of those lists I used list comprehension to label
each node based on them being in the 2 lists. Some of the nodes didn't get colored so I manually
labeled 17, 25, and 26 based on Slide 92-Reference 1. I labeled node 1 blue for Mr.Hi and node 34 red for John.

# Q2 Use the Girvan-Newman algorithm to illustrate the split
We know the final result of the Karate Club split, which you've colored in Q1. Use the Girvan-Newman algorithm to check if the split could have been predicted by the social interactions expressed by edges. How well does the mathematical model represent reality?  Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partioning algorithm (see Module-07 Social Networks, slides 90-99) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph after each iteration in your report.  

Note: Implement the Girvan-Newman algorithm (See Module-07, slide 91) rather than relying on a built-in function which hide the intermediate steps. Narrate in your report, the workings of the Girvan-Newman algorithm.

*Q: How many iterations did it take to split the graph?* 

## Answer
Below is my implementation of the Girvan-Newman algorithm.

```python
def girvan_newman_algorithm(G):
    G_copy = G.copy()
    connected_components = [list(nx.connected_components(G_copy))] #A list of all the components of the graph

    while G_copy.number_of_edges() > 0 and len(connected_components[-1]) != 2: #While the graph isn't already split in 2
        all_edge_betweenness_values = nx.edge_betweenness_centrality(G_copy) #List of all the edges betweenness values
        max_betweenness = max(all_edge_betweenness_values, key = all_edge_betweenness_values.get) #Gets the max betweenness value

        G_copy.remove_edge(*max_betweenness)
        connected_components.append(list(nx.connected_components(G_copy)))
        nx.draw_spring(G_copy, with_labels = True, node_color = node_colors)
        plt.show()

    return connected_components

G_components_split = girvan_newman_algorithm(G)
```
## Discussion

# Q3

## Answer

## Discussion

# References

*Every report must list the references that you consulted while completing the assignment. If you consulted a webpage, you must include the URL.*

* Reference 1, <https://docs.google.com/presentation/d/1Bey47wfUnBEy4O6j-T2X7y_bT0YNM6CN/edit#slide=id.p92>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
