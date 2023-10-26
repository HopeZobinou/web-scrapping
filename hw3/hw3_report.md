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

## Discussion


# References

* Insert Reference 1, <https://stackoverflow.com/questions/16206380/python-beautifulsoup-how-to-remove-all-tags-from-an-element>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
