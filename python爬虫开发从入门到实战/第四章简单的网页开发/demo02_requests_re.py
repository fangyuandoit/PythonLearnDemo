#!/usr/bin/python3

import requests;
import  re;

html = requests.get("https://www.baidu.com").content.decode()

#提取标题
groups= re.search('title>(.*?)<', html, re.S)
print(groups.group(0))
print(groups.group(1))


#提取正文
list = re.findall("p>(.*?)<", html, re.S)
print(list)



