import requests
from bs4 import BeautifulSoup

url = "https://prohikes.tech"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.text
print(f"Title of the webpage: {title}")
