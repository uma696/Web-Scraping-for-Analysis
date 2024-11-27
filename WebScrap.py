print("**WEB SCRAPING FOR DATA ANALYSIS")
import requests
#Beautiful Soup automatically converts incoming records to Unicode and outgoing forms to UTF-8.
from bs4 import BeautifulSoup as bs

url = "https://quotes.toscrape.com/page/4/"
page_to_scrape= requests.get(url,verify=False)

#Prints the status of the request as response, 200 if success
print(page_to_scrape)

##The HTML content of the response is parsed using BeautifulSoup and stored in the variable soup.
soup=bs(page_to_scrape.text, "html.parser")
#parse tree = a parse tree: a toolkit for studying a document and removing what you need

#Prints the title of the web scraping page
print(soup.title)

#Find all class - This class will find the given tag 'span' and 'small' with the given attribute by class name 'text' and 'author' respectively
required_text = soup.find_all("span",class_="text")
required_author = soup.find_all("small",class_="author")

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
for text,author in zip(required_text,required_author) :
    Text= text.get_text()
    Author= author.get_text()
    print({Text : Author})




