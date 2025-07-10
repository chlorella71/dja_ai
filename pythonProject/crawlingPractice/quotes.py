import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.select('.quote')
for q in quotes:
    text = q.select_one('.text').text
    author = q.select_one('.author').text
    print(f"{text} — {author}")
