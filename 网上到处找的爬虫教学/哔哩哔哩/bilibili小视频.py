import json

import requests
from bs4 import BeautifulSoup


head ={
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

urls =[]

#添加请求连接
def add_urls(urls):
    for i in range(1,20,10):
        url = "http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset="+str(i)+"&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc"
        urls.append(url)


#分析返回的json数据。然后解析
def parseHtml(urls):
    for url in urls:
        html = requests.get(url,headers = head).content.decode()
        loads = json.loads(html)
        items = loads['data']['items']
        for item in items:
             description = item['item']['description']
             playurl = item['item']['video_playurl']
             print(description)
             print(playurl)


add_urls(urls)
parseHtml(urls)

