

#爬取java吧的前几页页帖子标题
import re

import requests

urls =[]

headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

def addUrls(urls):
 #   url ="http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=100"
     for  i in range(0,100,50):
         urls.append("http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=" + str(i))



def   parseHtml(urls):
    for url in urls:
        html = requests.get(url, headers=headers).content.decode()
        #通过正则取标题
        groups = re.findall('<a rel="noreferrer" href="/p/\d*" title="(.*?)" target="_blank" class="j_th_tit ">', html, re.S)

        # groups = re.search('title=\"(.*?)\" target=\"_blank\" class=\"j_th_tit \">', html, re.S)
        for g in groups:
            print(g)

addUrls(urls)
parseHtml(urls)
