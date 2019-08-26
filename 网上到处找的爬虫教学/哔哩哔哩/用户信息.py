import csv
import json
from multiprocessing.dummy import Pool

import requests

#爬取B站前10名用户的基本信息  保存为csv

urls = []

#将用户信息api 添加至列表里面
def Add_urls(urls):
    # url = "https://api.bilibili.com/x/space/acc/info?mid=46131321&jsonp=jsonp"
    for i in range(1,10):
       urls.append("https://api.bilibili.com/x/space/acc/info?mid="+str(i)+"&jsonp=jsonp")


def getsource(url):
     html = requests.get(url).content.decode()
     json_data = json.loads(html)
     data_ = json_data['data']

     name = data_.get("name")
     sex = data_.get("sex")
     face = data_.get("face")
     birthday = data_.get("birthday")

     with open('writecsv.csv', "a", encoding="utf-8", newline='') as f:
         dict_writer = csv.DictWriter(f,fieldnames=["name", "sex", "face", "birthday"])
         dict_writer.writerow({"name": name, "sex": sex, "face":face,"birthday":birthday})



Add_urls(urls)

with open('writecsv.csv', "w", encoding="utf-8", newline='') as f:
    dict_writer = csv.DictWriter(f, fieldnames=["name", "sex", "face", "birthday"])
    dict_writer.writeheader()

pool = Pool(1)
results = pool.map(getsource, urls)

pool.close()
pool.join()