import requests
import pandas as pd

data = []
url = 'https://www.forbes.com/billionaires/page-data/index/page-data.json'

r = requests.get(url)
json_data = r.json()

for item in json_data['result']['pageContext']['tableData']:
    try:
        rank = item['rank']
    except:
        rank = ''
    try:
        name = item['personName']
    except:
        name = ''
    try:
        age = item['age']
    except:
        age = ''
    try:
        country = item['country']
    except:
        country = ''
    try:
        state = item['state']
    except:
        state = ''
    try:
        city = item['city']
    except:
        city = ''
    try:
        source = item['source']
    except:
        source = ''
    try:
        industries = item['industries']
    except:
        industries = ''
    try:
        year = item['year']
    except:
        year = ''
    try:
        month = item['month']
    except:
        month = ''
    try:
        title = item['title']
    except:
        title = ''
    try:
        netWorth = item['netWorth']
    except:
        netWorth = ''

    dic = {
        'Rank': rank,
        'Name': name,
        'age': age,
        'Country': country,
        'State': state,
        'City': city,
        'Source' : source,
        'Industries': industries,
        'Year': year,
        'Month': month,
        'Title': title,
        'NetWorth': netWorth

    }
    data.append(dic)
df = pd.DataFrame(data)
df.to_csv('billionaries.csv', index=False)
print('finished')