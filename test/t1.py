import requests

my_datas={
    "query":"java",
    "page":"2",
    "ka":"page-next"
}

my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
}

decode = requests.get("https://www.zhipin.com/c101270100/?query=java&page=2&ka=page-next",headers =my_headers,data=my_datas).content.decode()
print(decode)
