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
    soup = BeautifulSoup(html_content, 'html.parser')
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



        '''
        if html_content != None:
            og_html_filename = os.path.join(raw_html_dir, f"{filename}_original.html") #Adds the hashed file name to the directory for the raw html data
            save_to_file(html_content, og_html_filename) #Saves the content to the raw html folder

            txt_content = strip_html(html_content) #Strips the html file and gathers just text

            txt_content_filename = os.path.join(proccessed_html_dir, f"{filename}_text_content.txt")
            save_to_file(txt_content, txt_content_filename)

            uri_to_hash[uri] = filename #Adding to the uri to hash map dictionary
'''
    #Saves the hash mapping to a file
    mapping_filename = os.path.join(reg_path, "uri_to_hash_mapping.txt")
    with open(mapping_filename, "w", encoding="utf-8") as mapping_file:
        for uri, hash_value in uri_to_hash.items():
            mapping_file.write(f"{uri} => {hash_value}\n")


    print(f"Downloaded and processed {len(uris)} URIs.")


