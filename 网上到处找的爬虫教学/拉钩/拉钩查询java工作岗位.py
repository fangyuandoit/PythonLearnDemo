#!/usr/bin/env python3.7

#https://zhuanlan.zhihu.com/p/65081383
import json
import requests
import time




def  getSource(url,datas):
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
    }

    time.sleep(5)
    ses = requests.session()  # 获取session
    ses.headers.update(my_headers)  # 更新
    ses.get(
        "https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=")

    content = ses.post(url=url, data=datas)
    result = content.json()

    return result;



def parseSource(result):
    info = result['content']['positionResult']['result']
    # info_list = []
    for job in info:
        information = []
        information.append(job['positionId'])  # 岗位对应ID
        information.append(job['city'])  # 岗位对应城市
        information.append(job['companyFullName'])  # 公司全名
        information.append(job['companyLabelList'])  # 福利待遇
        information.append(job['district'])  # 工作地点
        information.append(job['education'])  # 学历要求
        information.append(job['firstType'])  # 工作类型
        information.append(job['formatCreateTime'])  # 发布时间
        information.append(job['positionName'])  # 职位名称
        information.append(job['salary'])  # 薪资
        information.append(job['workYear'])  # 工作年限
        # info_list.append(information)
        print(information)



urls =[]
for x in range(1,3):
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
    datas = {
        'first': 'false',
        'pn': x,
        'kd': 'java',
    }

    source = getSource(url, datas)
    parseSource(source)



