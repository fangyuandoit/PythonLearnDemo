import requests


#直接访问会被拦截
def  useNormalUserAgent():
    url="https://weibo.com/u/6316623611";
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    text = requests.get(url, headers=headers).text
    print(text)


#通过baiduspider能够得到想要的信息
def  useBaiduSpiderlUserAgent():
    # url="https://weibo.com/u/6316623611";
    url="https://weibo.com/p/1005056316623611/follow";
    headers = {
        "User-Agent": "baiduspider",
    }

    text = requests.get(url, headers=headers).text
    print(text)



# useNormalUserAgent()
useBaiduSpiderlUserAgent()

