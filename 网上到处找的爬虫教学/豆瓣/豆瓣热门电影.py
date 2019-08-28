

# url
import json

import requests

url="https://movie.douban.com/j/search_subjects"

headers={
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

# 循环构建请求参数并且发送请求
for page_offsite in range(0,40,20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_offsite
    }
    text = requests.get(url, headers=headers, params=params).text
    loads = json.loads(text)
    subjects_ = loads['subjects']
    for m in subjects_:
        print(m['title'],m['rate'],m['url'])
   