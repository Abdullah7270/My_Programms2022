import re

from bs4 import BeautifulSoup
import urllib.request
import requests

html_page = urllib.request.urlopen('https://www.talemia.sa/ar/annualreports')
soup = BeautifulSoup(html_page, 'html.parser')

links = []


#print(len(all_links))

for link in soup.select('a', attrs={'href'}):
    #print(link.get('href'))
     links.append(link.get('href'))
print(links)



