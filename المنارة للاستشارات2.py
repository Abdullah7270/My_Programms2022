# How to extract text from a WebElements - Selenium
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

titles = []
s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

for page in range(1,5):

    driver.get('https://www.manaraa.com/category/4/%D8%AA%D8%B1%D8%AC%D9%85%D8%A9'+str(page)+'.html')


    title = driver.find_elements(By.CSS_SELECTOR, 'div.blog-content > h1> a ')
    for item_title in title:
        titles.append(item_title.text)
        print(item_title.get_attribute('textContent'))

driver.close()











