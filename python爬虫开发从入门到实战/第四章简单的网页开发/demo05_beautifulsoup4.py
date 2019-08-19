#!/usr/bin/python3
import requests
from bs4  import BeautifulSoup

html = requests.get("https://www.cnblogs.com/").content.decode()

soup = BeautifulSoup(html, 'html.parser')
find = soup.find_all(class_='titlelnk')
for a in find:
    print(a.string)
    print(a['href'])
