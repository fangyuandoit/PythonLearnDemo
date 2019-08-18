import time
from multiprocessing.dummy import Pool

import requests


def query(url):
    requests.get(url)


start = time.time();

for i in range(50):
    query("https://www.baidu.com")

end = time.time();
print(f"单线程访问--{end-start}")

# 多线程访问
start = time.time();
url_list = []
for i in range(50):
    url_list.append("https://www.baidu.com")

pool = Pool(5)
pool.map(query,url_list)
end = time.time()

print(f"多线程{end-start}")
