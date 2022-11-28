import requests
from requests_html import HTMLSession
import pandas as pd

s = HTMLSession()

url = 'https://www.youtube.com/results?search_query=python+for+beginners'

# Greate empty list
data = []

# Sent the request to the server
r = s.get(url)

# Render the javascript page
# If you want more result increase the scrolldown value
r.html.render(sleep=3, timeout=100, keep_page=True, scrolldown=10)

# Find the data elements
container = r.html.find('ytd-video-renderer.style-scope.ytd-item-section-renderer')

# Use for loop to extract all data
for element in container:
    vedio_title = element.find('h3.style-scope.ytd-video-renderer', first=True).text
    vedio_link = 'https://www.youtube.com' + element.find('a#video-title', first=True).attrs['href']
    posted = element.find('#metadata-line > span:nth-child(2)', first=True).text

# Append all data
    data.append([vedio_title, vedio_link, posted])
# Greats pandas data frame to store data
df = pd.DataFrame(data, columns=['Vedio Title', 'Vedio Link', 'Posted'])
df.to_csv('youtube_data.csv', index=False)