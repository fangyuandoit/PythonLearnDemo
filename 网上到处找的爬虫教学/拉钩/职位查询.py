import requests

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1028755976.1554993411; user_trace_token=20190411223637-36a23bd6-5c67-11e9-935a-5254005c3644; LGUID=20190411223637-36a24074-5c67-11e9-935a-5254005c3644; _gid=GA1.2.1838022782.1567260119; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567260119; LGSID=20190831220158-e60d7a21-cbf7-11e9-8df6-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D06jOitBT82jAQfM44aoEJO8Bsb6lNBt4jCunO6lPGRS%26wd%3D%26eqid%3De104d34c001f63e4000000065d6a7dd1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E6%88%90%E9%83%BD; JSESSIONID=ABAAABAAAGEAAJHF4FECF7A6DDEE516BB2C52F864EEFDD3; _ga=GA1.3.1028755976.1554993411; _gat=1; OUTFOX_SEARCH_USER_ID_NCOO=77616463.6288403; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ce805718e411-08debf2d875a9c-7122633d-220000-16ce805718f2ae%22%2C%22%24device_id%22%3A%2216ce805718e411-08debf2d875a9c-7122633d-220000-16ce805718f2ae%22%7D; sajssdk_2015_cross_new_user=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567260772; X_HTTP_TOKEN=fc16b87e9f8251e417706276516cc1197ae16c8807; LGRID=20190831221251-6af8b114-cbf9-11e9-8df6-525400f775ce; ___rl__test__cookies=1567260777935',
    'Pragma': 'no-cache',
    'Referer': 'https://m.lagou.com/search.html',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',

}



url ='https://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=java&pageNo=1&pageSize=15'

html = requests.get(url=url,   headers=headers).content.decode()
print(html)