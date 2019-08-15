#!/usr/bin/python3

import requests

# content = requests.get("https://www.baidu.com").content.decode()
# print(content)

c = requests.get("https://www.baidu.com");
print(c)
print(c.status_code)
print(c.content)
print(c.content.decode())


data={
    "key1":"value1",
    "key2":"value2"
}
requests.post("http",data=data).content.decode();

#如果需要发送json格式
requests.post("http",json=data).content.decode()

