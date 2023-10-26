# HW3 - Report
### Hope Zobinou  
### DATA 440, Fall 2023
### 10/24/2023

# Q1  Data Collection 
Download the HTML content of the 1000 unique URIs you gathered in HW2 and strip out HTML tags (called "boilerplate") so that you are left with the main text content of each webpage.

*Q: How many of your 1000 URIs produced useful text? If that number was less than 1000, did that surprise you?* 


## Answer
Below is the code I used to download the html content and strip the HTML tags

```python
import requests
import hashlib
from boilerpy3 import extractors
from bs4 import BeautifulSoup
import os

def download_html(uri):
    try:
        response = requests.get(uri)

        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f'Failed to download from {uri}: {e}')
        return None
    
def save_to_file(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def create_filename(uri):
    return hashlib.md5(uri.encode('utf-8')).hexdigest()

def strip_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser') #Removes html tags
    return soup.get_text()
    #extractor = extractors.ArticleExtractor() #Full text extractor
    #return extractor.get_content(html_content)

if __name__ == "__main__":
    reg_path = "c:/Users/hopez/Documents/Data440/Homework3"

    all_uris = 'c:/Users/hopez/Documents/Data440/Homework3/twitter_links.txt'
    uri_to_hash = {} #Dictionary that maps the URIs to its hash
    raw_html_dir = "c:/Users/hopez/Documents/Data440/Homework3/raw_html"
    proccessed_html_dir = "c:/Users/hopez/Documents/Data440/Homework3/processed_html"

    with open(all_uris, 'r') as file: #Reads in the file with all the URIs
        uris = file.readlines()

    uris = [item.strip() for item in uris]
    
    #test_uris = uris[0:5]

    #print(type(uris))
    #print(len(uris))
    #print(uris)

    for uri in uris:
        filename = create_filename(uri)
        html_content = download_html(uri)

        if html_content != None:
            og_html_filename = os.path.join(raw_html_dir, f"{filename}_original.html") #Adds the hashed file name to the directory for the raw html data
            save_to_file(html_content, og_html_filename) #Saves the content to the raw html folder
        else:
            continue

        txt_content = strip_html(html_content) #Strips the html file and gathers just text

        txt_content_filename = os.path.join(proccessed_html_dir, f"{filename}_text_content.txt")
        save_to_file(txt_content, txt_content_filename)

        uri_to_hash[uri] = filename #Adding to the uri to hash map dictionary

    #Saves the hash mapping to a file
    mapping_filename = os.path.join(reg_path, "uri_to_hash_mapping.txt")
    with open(mapping_filename, "w", encoding="utf-8") as mapping_file:
        for uri, hash_value in uri_to_hash.items():
            mapping_file.write(f"{uri} => {hash_value}\n")

```
819 of the links produced useful texts. I was not surprised because in my code I skipped saving HTML and striped HTML if they returned none from the download. 

## Discussion
The process of downloading the web pages is similar to hw2. First I had the program read in a file containing all the URIs and put it into a list. Then I iterate through the list and call a bunch of methods on that certain element in the list to get the raw html file, and processed html text file. In the loop, I also have some dictionary work going on to map the hashed file names to the original file name. I used Beautiful Soup instead of boilerpy3 because of some parsing error I couldn't fix-Reference 1.

# Q2 Rank with TF-IDF
Choose a query term (e.g., "coronavirus") that is not a stop word (e.g., "the"), or super-general (e.g., "web"), or in HTML markup (e.g., "http") that is found in at least 10 of your documents.  If the term is present in more than 10 documents, choose any 10 English-language documents from *different domains* from the result set.

Compute TF-IDF values for the query term in each of the 10 documents and create a table with the TF, IDF, and TF-IDF values, as well as the corresponding URIs.

Rank the URIs in decreasing order by TF-IDF values.

## Answer
Below is the code I used to get the word count and target word frequency.

```python
import os

def search_word_in_file(file_path, word):
    file_name = os.path.basename(file_path)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
        word_count = len(text.split())
        word_frequency = text.count(word)
        return file_name, word_count, word_frequency

if __name__ == "__main__":
    #Path: "c:/Users/hopez/Documents/Data440/Homework3"

    folder_path = "c:/Users/hopez/Documents/Data440/Homework3/processed_html"
    word = 'iPhone'

    file_list = []
    word_count_list = []
    word_freq_list = []

    for root, dirs, files in os.walk(folder_path): #Loops through each file in the folder
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                result = search_word_in_file(file_path, word)
                if result[2] > 0:  # Only add files where the word is found
                    file_list.append(result[0])
                    word_count_list.append(result[1])
                    word_freq_list.append(result[2])

    for file_name, word_count, word_frequency in zip(file_list, word_count_list, word_freq_list):
        print(f"File: {file_name}, Word Count: {word_count}, Word Frequency: {word_frequency}")
```

Below is the output of the code.

```console
File: dc17d95de563d971658124bcac8e0244_text_content.txt, Word Count: 1653, Word Frequency: 1
File: dd24516329d71af93be8b85780c48842_text_content.txt, Word Count: 1633, Word Frequency: 1
File: e42e013496d5d343816fdb987f8d7c1f_text_content.txt, Word Count: 540, Word Frequency: 2 
File: e6f75a952a186699cf364c88faac523a_text_content.txt, Word Count: 289, Word Frequency: 3 
File: eaa40af2776d3064cb013040b412f427_text_content.txt, Word Count: 394, Word Frequency: 11
File: ec4ba285be1c8ebd742493355acd4d56_text_content.txt, Word Count: 1417, Word Frequency: 1
File: f05578b176426024c7d5b4776f49bd40_text_content.txt, Word Count: 366, Word Frequency: 4 
File: f263e36753329bb37caac686967a959f_text_content.txt, Word Count: 110, Word Frequency: 1 
File: f4737ffcbc2955da993657a282cfce89_text_content.txt, Word Count: 495, Word Frequency: 2 
File: f6005d6be59374ac17157d11874499f5_text_content.txt, Word Count: 194, Word Frequency: 1 
File: f8b64df5acee28efc62872c3c9b8f5a6_text_content.txt, Word Count: 950, Word Frequency: 1 
File: fcaeecc17bb81a23757e7ddf7ec11e96_text_content.txt, Word Count: 506, Word Frequency: 1 
File: fed09fdf4bef922cd193f6aadafbf6b2_text_content.txt, Word Count: 304, Word Frequency: 3
```

10 Hits for the term "iPhone", ranked by TF-IDF.
|TF-IDF |TF |IDF  |URI
|------:|--:|---:|---
|0.7724|0.0258|29.9392|https://www.idropnews.com/how-to/your-iphone-can-replicate-your-voice-after-15-minutes-of-training/200586/
|


## Discussion


# References

* Insert Reference 1, <https://stackoverflow.com/questions/16206380/python-beautifulsoup-how-to-remove-all-tags-from-an-element>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
