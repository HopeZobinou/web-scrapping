# HW1 - Report
### Hope Zobinou
### DATA 440, Fall 2023
### 9/26/2023

# Q1

*Now consider the following links:*
```text
A --> B
B --> C
C --> D
C --> A
C --> G
E --> F
G --> C
G --> H
I --> H
I --> K
L --> D
M --> A
M --> N
N --> D
O --> A
P --> G 
```
*Draw the resulting directed graph (either sketch on paper or use another tool) showing how the nodes are connected to each other.*
For the graph, list the nodes (in alphabetical order) that are each of the following categories:
* SCC: 
* IN: 
* OUT: 
* Tendrils: 
    * indicate if the tendril is reachable from IN or can reach OUT
* Tubes: 
    * explain how the nodes serve as tubes
* Disconnected:

## Answer

Below is the graph and the categories that the nodes go to.

![IMG_7740](https://github.com/HopeZobinou/data440/assets/81893993/5e513436-c124-467d-9f18-11074263c7bd)

## Discussion

*To find the SCC, I looked at the nodes that looked like they had a lot of traffic (in/out links). A, B, and C look like they can reach*
*most of the nodes and most of the nodes can reach them. To find the IN nodes, I looked at the nodes that have out links to the SCC but*
*don't have in links. M, O, and P point to the SCC but have no in links. To find the OUT, I looked for nodes that have in links that trace back from the SCC*
*but no out links. D and H fit this. To find the tendrils, I looked for the nodes that can't be reached from the SCC and can't reach the SCC. L, I, and K all*
*do this. Tubes are nodes that link the INs to the OUTs. Node G and N do these. The disconnected nodes are E and F. These 2 are isolated and only connected*
*to each other by one edge.*

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
