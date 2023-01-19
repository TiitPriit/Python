import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bmw.com/en/models/3-series/sedan/2020/at-a-glance.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

name = soup.find("h1").get_text().strip()
horsepower = soup.find("dd", class_="horsepower").get_text().strip()
torque = soup.find("dd", class_="torque").get_text().strip()

data = {'name': name, 'horsepower': horsepower, 'torque': torque}
df = pd.DataFrame(data, index=[0])
df.to_csv('bmw_data.csv', index=False)
