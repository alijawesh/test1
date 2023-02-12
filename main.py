from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

url = 'https://markets.ft.com/data/funds/tearsheet/historical?s=DK0060697548:DKK'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', class_='mod-ui-table')
rows = table.find_all('tr')
df = pd.DataFrame(columns=['issue_id', 'Dato', 'Close'])
issue_id = 1000
for issue_id, row in enumerate(rows[1:]):
    columns = row.find_all('td')
    date_string = columns[0].get_text()
    my_new_date = date_string[-17:]
    date_1 = datetime.strptime(my_new_date, '%a, %b %d, %Y')
    formatted_date_1 = date_1.strftime('%d-%m-%Y')
    Close = columns[1].get_text()

    df.loc[len(df)] = [issue_id, formatted_date_1, Close]

df.to_csv("Test1.csv", index=False)
print(df)
