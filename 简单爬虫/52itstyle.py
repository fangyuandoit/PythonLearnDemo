import uuid

import requests
from bs4 import BeautifulSoup

urls=[]
def addUrl():
    for i  in range(10):
        i = i+1;
        urls.append("https://blog.52itstyle.vip/page/"+str(i)+"/")


def parseHtmlAndDownloadPhoto(urls):
     for u in urls:
         html = requests.get(u).content.decode()
         soup = BeautifulSoup(html, 'html.parser')
         find = soup.find_all(class_='post post-type-normal')
         for a in find:
             photourl = a.find(class_='post-body').find('p').find('img')['src']
             downloadPicture(photourl);

def downloadPicture(photourl):
    html = requests.get(photourl, stream=True)
    file = open('E:\mydata\data'+str(uuid.uuid1())+".png", "wb")
    file.write(html.content)
    file.close()


addUrl()
parseHtmlAndDownloadPhoto(urls)
