

# 多线程访问
import uuid
from datetime import time
from multiprocessing.dummy import Pool

import requests


def query(url):
    # requests.get(url)
     print(url)

url_list = []
for i in range(5):
    url_list.append("https://www.baidu.com")

pool = Pool(1)
pool.map(query,url_list)
