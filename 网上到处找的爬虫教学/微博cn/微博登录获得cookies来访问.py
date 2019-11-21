#没什么特别的东西，登录通过post请求  headers存放登录的请求头   data存放post请求的提交的参数
import requests

#微博登录 weibo.cn 的方法
def login():
    url = "https://passport.weibo.cn/sso/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=",
        "Origin": "https://passport.weibo.cn"
    }

    data = {
        "username": "15828313741",  #需改成自己的登录名字
        "password": "88700915wqq",  #修改成自己的登录密码
        "savestate": "1",
        "ec": "0",
        "pagerefer": "https://weibo.cn/pub/",
        "entry": "mweibo",
    }


    response = requests.post(url, headers=headers, data=data)
    # print(response.content.decode())
    cookies = response.cookies.get_dict()
    # print(cookies)
    # for key in cookies.keys():
    #     print(key, cookies.get(key))

    return cookies;


#微博用cookie的方法获得用户信息
def getUserInfo(cookies):
    url ="https://weibo.cn/infoqchina";
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    content = requests.get(url, headers=headers, cookies=cookies).text
    print(content)


loginCookies = login()
getUserInfo(loginCookies)

