
from multiprocessing.dummy import Pool
import requests
import  re
import requests
from bs4  import BeautifulSoup

# 根据av号 爬取源码，然后正则获得cid号码。通过cid 调用接口获得弹幕

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

#传入av 获得cid号码
def getcidByAa(avNumber):
     url  = "https://www.bilibili.com/video/av" + str(avNumber)
     html = requests.get(url,headers=head).content.decode()
     groups = re.search('cid=(.*?)&aid=', html, re.S)
     # print(groups.group(0))
     return  groups.group(1)



#根据cid 爬取接口获得弹幕
def  printDanmu(cid):
    url  = "https://comment.bilibili.com/"+str(cid)+".xml"
    html = requests.get(url,headers=head).content.decode()
    soup = BeautifulSoup(html, 'html.parser')
    find = soup.find_all('d')
    for a in find:
        print(a.string)




av =64441665
cid = getcidByAa(av)
# cid=111883231
print(cid)
printDanmu(cid)


