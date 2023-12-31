# Report
### Hope Zobinou
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

a) First, load this URI https://httpbin.org/user-agent directly in your browser and take a screenshot. The resulting webpage should show the "User-Agent" HTTP request header that your web browser sends to the web server.

b) In a single curl command, issue a HEAD HTTP request for the URI, https://t.co/KSHFYLmmB0. Show the HTTP response headers, follow any redirects, and change the User-Agent HTTP request field to "DATA 440." Show the command you issued and the result of your execution on the command line. (Either take a screenshot of your terminal or copy/paste into a code segment.)

Briefly explain the results you get for each of these steps.

## Answer

*Below is my browser when I entered the URI.*

![q2a](https://github.com/HopeZobinou/data440/assets/81893993/f11cead6-4ad3-49f3-acbe-4fd126018b25)

Below I made a head request and changed the user agent field in one line.

![q2bp1](https://github.com/HopeZobinou/data440/assets/81893993/deed661a-cd4a-470b-ae3a-1c277cc0c4e5)

Below is a picture of the output after the redirection command.

![q2bp2](https://github.com/HopeZobinou/data440/assets/81893993/c477ae22-4da1-44c8-afa1-06a8f92cb8b7)



## Discussion

*I went to reference 1 to figure out how to change the user agent field. The -I stands for head and the -L stands for following redirections.*
The page was redirected once. You can tell because there is only one 3xx-level response. 

# Q3

Write a Python program to find links to PDFs in a webpage.

Your program must do the following:
* take the URI of a webpage as a command-line argument
* extract all the links from the page
* for each link, request the URI and use the `Content-Type` HTTP response header to determine if the link references a PDF file 
* for all links that reference a PDF file, print the original URI (found in the parent HTML page), the final URI (after any redirects), and the number of bytes in the PDF file. (Hint: `Content-Length` HTTP response header)

Show that the program works on 3 different URIs, one of which must be https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html, which contains 8 links to PDFs.
  
## Answer

Below is the results of the code running with the https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html link.

![q3p1](https://github.com/HopeZobinou/data440/assets/81893993/4c122b83-242a-4a20-8bf9-651cff467e14)

Below is the result of the code running with the https://cristianofanelli.com/teaching/ link.

![q3p2](https://github.com/HopeZobinou/data440/assets/81893993/9b54a735-cc12-4b7d-a688-d12beef72bde)


Below is the result of the code running with the https://swensonlab.weebly.com/pubs.html link.

![q3p3](https://github.com/HopeZobinou/data440/assets/81893993/8a2a5d47-160b-466e-8917-ecdfe3f38827)



## Discussion

When making the program I just had an order in mind and replicated it with the code. Make an 
http get request on the user's uri, make a soup object, goes through every link in the soup object to find anchor tags, check if the link ends in pdf, get the final uri, get the content length, and print the results. The making soup object and performing its methods come from Professor's ipynb on scraping imdb Reference 2.

# References

* Reference 1, https://phoenixnap.com/kb/curl-user-agent
* Reference 2, https://github.com/anwala/teaching-web-science/blob/main/fall-2023/week-3/data_440_02_f23_mod_03_web_scraping_imdb.ipynb
