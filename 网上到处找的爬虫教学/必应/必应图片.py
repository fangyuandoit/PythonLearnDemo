import requests

from bs4  import BeautifulSoup

url ="http://bing.plmeizi.com/?page=1"

html = requests.get(url).content.decode()


soup = BeautifulSoup(html, 'html.parser')
find = soup.find_all(class_='clearfix')

for f in find:
  aHrefs = f.find_all('a')
  for a in aHrefs:
      print(a.find('img')['alt'])
      print(a.find('img').get('src'))
      print("------------")


