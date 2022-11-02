from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.talemia.sa/en/'
response = requests.get(url)

html_page = BeautifulSoup(response.content, 'html.parser')
all_links = html_page.find_all('a')

def extraxt_link(url, name):
    links = {'link': [], 'category': []}
    for link in all_links:
        href = link['href']
        if href:
            if name in href:
                links['link'].append(href)
                links['category'].append('internal')
            if href [0] == '#':
                links['link'].append(f'{url}{href}')
                links['category'].append('internal')
            if href.split(':')[0] in ['https', 'http'] and not name in href:
                links['link'].append(href)
                links['category'].append('external')
    return links
url = 'https://www.talemia.sa/en/'
name = 'talemia.com'
data = extraxt_link(url, name)

df = pd.DataFrame(data)
print(df)


