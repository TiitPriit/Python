#Web scraping on tehnika, mille abil saab automaatselt andmeid veebilehtedelt koguda ja analüüsida. See võimaldab teil automatiseerida andmete kogumise protsessi ja saada juurdepääsu andmetele, mis ei ole otse kättesaadavad API-de või muude meetoditega.

#Web scraping-u tegevuse eetilisuse ja viisakuse reeglid on seotud sellega, kuidas te andmeid kogute ja kasutate. Näiteks on ebaetiline kasutada web scraping-ut, et varastada teiste veebilehtede andmeid või segada teiste veebilehtede tööd. Samuti on oluline järgida veebilehtede tingimusi ja privaatsustingimusi, kui te andmeid kogute.

import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title?groups=top_250&sort=user_rating'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')

for container in movie_containers:
    name = container.h3.a.text
    rating = container.strong.text
    if float(rating) > 8.0:
        print(name, rating)
