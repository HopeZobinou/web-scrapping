import sys
import requests
from bs4 import BeautifulSoup

def print_pdf_links(uri):
    response = requests.get(uri) #HTTP GET request to the uri
    soup = BeautifulSoup(response.text, 'html.parser') #Collects all the html info from the URI

    for link in soup.find_all('a', href = True): #Find all anchor tags that have an href attribute
        href = link['href']
            
        #If the link ends in .pdf, then we get the final uri
        #and the length of the pdf
        if href.lower().endswith('.pdf'):
            final_uri = requests.head(href, allow_redirects = True).url
            content_length = int(requests.head(final_uri).headers.get('Content-Length', 0))

            print("URI: ", uri)
            print("Final URI: ", final_uri)
            print("Content Length: ", content_length, "bytes")
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("2 arguments are required, the file name and link.")
        sys.exit(1)

    uri = sys.argv[1]
    print_pdf_links(uri)
