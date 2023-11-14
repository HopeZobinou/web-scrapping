# HW5 - Report
### Hope Zobinou  
### DATA 440, Fall 2023 
### 11/14/23

# Q1. Color nodes based on the final split 

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

Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partitioning algorithm (see Module-07 Social Networks, slides 90-99) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph after each iteration in your report.  

Note: Implement the Girvan-Newman algorithm (See Module-07, slide 91) rather than relying on a built-in function which hide the intermediate steps. Narrate in your report, the workings of the Girvan-Newman algorithm.

*Q: How many iterations did it take to split the graph?* 

## Answer
The mathematical model from the algorithm doesn't 100% represent reality. An algorithm with a formula involved (Compute betweenness centrality for edges) will always have an error associated with it especially since there is a summation in the formula. That is why the final result from the algorithm has a few nodes that are colored purple (belong to Mr.Hi's network) but are connected to John while being disconnected from Mr. Hi. Another reason I can think of is that the formula takes into account how close nodes are to the target. 32, 9, and 3 are closer to John than Mr. Hi. It took 11 iterations to split the graph.

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
Below are images of the graph after each iteration.

![graph_1i](https://github.com/HopeZobinou/data440/assets/81893993/f56e8037-a724-4e11-85d2-ae003f23fd22)
![graph_2i](https://github.com/HopeZobinou/data440/assets/81893993/dcc75eca-5511-410a-a6dc-e24f2bfc3f8b)
![graph_3i](https://github.com/HopeZobinou/data440/assets/81893993/a0b22aa1-3482-41a4-a3eb-20e43954ab61)
![graph_4i](https://github.com/HopeZobinou/data440/assets/81893993/e40deb58-47fc-4ac7-9bdd-a908155248b6)
![graph_5i](https://github.com/HopeZobinou/data440/assets/81893993/b1b2c194-3e9e-41fc-a27d-2a1147860489)
![graph_6i](https://github.com/HopeZobinou/data440/assets/81893993/35483e38-0286-4f9a-9664-a7490135e823)
![graph_7i](https://github.com/HopeZobinou/data440/assets/81893993/f4861001-5924-4abd-be5a-aad047d39abc)
![graph_8i](https://github.com/HopeZobinou/data440/assets/81893993/62b335cd-5a20-47d5-9600-8172bbedb435)
![graph_9i](https://github.com/HopeZobinou/data440/assets/81893993/c0756b12-8421-4088-9f3b-059e8867bebf)
![graph_10i](https://github.com/HopeZobinou/data440/assets/81893993/9395ed03-4965-4358-8ef7-741cee51f5bd)
![graph_11i](https://github.com/HopeZobinou/data440/assets/81893993/728d14a7-4946-4ed2-a1ef-006835d6fccf)


## Discussion
When making the algorithm, I just copied the pseudo-code the professor gave us in the class slide-Reference 2. And I also had to look up the correct methods to use with networkx to get the values I needed. Like to get all the edges betweenness and to remove edges-Reference 3.


# Q3 Compare the actual to the mathematical split
Compare the connected components of the Girvan-Newman split graph (Q2) with the connected components of the actual split Karate club graph (Q1).

*Q: Did all of the same colored nodes end up in the same group?  If not, what is different?*

## Answer
All the same nodes didn't end up in the same group. Nodes 32, 9, and 3 are colored purple for Mr. Hi but are now in John's group at the end of the Girvan-Newman split.

Below are images of the 2 graphs.

![before_split](https://github.com/HopeZobinou/data440/assets/81893993/74bc78f9-77fc-4e0f-a567-fbd77bd784da)
![graph_11i](https://github.com/HopeZobinou/data440/assets/81893993/728d14a7-4946-4ed2-a1ef-006835d6fccf)

## Discussion
The Girvan-Newman graph will most likely be different every time compared to just finding the group connections based on the edges being connected. The formula used to find the summation of all the betweenness is going to have an error associated with it. The error will affect the true results. The results are which edge to remove. The formula takes the node's distance from the target into consideration for betweenness. 

# References

* Reference 1, <https://docs.google.com/presentation/d/1Bey47wfUnBEy4O6j-T2X7y_bT0YNM6CN/edit#slide=id.p92>
* Reference 2, <https://docs.google.com/presentation/d/1Bey47wfUnBEy4O6j-T2X7y_bT0YNM6CN/edit#slide=id.p91>
* Reference 3, <https://networkx.org/documentation/stable/tutorial.html> 
