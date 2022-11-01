from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

titles = []
dates = []
contents = []

for page in range(1,17):
    driver.get('https://www.talemia.sa/ar/news/listall/'+str(page)+'.html'
               ''+str(page)+'.html')

    news = driver.find_elements(By.CSS_SELECTOR, 'h4.media-heading.news-titleall')
    date = driver.find_elements(By.CSS_SELECTOR, 'div.col-md-3.text-left.new-listpage-date')
    content = driver.find_elements(By.CSS_SELECTOR, 'div.col-md-12>p')
    for item_news in news:
        titles.append(item_news.text)
    for item_date in date:
        dates.append(item_date.text)
        #print(item_date.get_attribute('textContent').strip())
    for item_content in content:
        contents.append(item_content.text)

t4edu_news = { 'عنوان الخبر': titles,'تاريخ النشر': dates , 'المحتوى': contents}
df = pd.DataFrame(data=t4edu_news)
df.to_csv('t4edu_output_news.csv')

driver.close()





