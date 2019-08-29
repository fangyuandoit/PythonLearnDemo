# import js2py as js2py
# import requests
#
# context = js2py.EvalJs()
#
#
# def  make_sign(query):
#     # js逆向获取sign的值
#     # 读取js文件
#     with open("a.js", "r", encoding="utf-8") as f:
#         # 添加至上下文
#         context.execute(f.read())
#
#     # 调用js中的函数生成sign
#     sign = context.a(query)
#     # 将sign加入到data中
#     return sign
#
# def make_data(query, sign):
#     data = {
#         "query": query,
#         "from": "en",
#         "to": "zh",
#         "transtype": "translang",
#         "simple_means_flag": 3,
#         "token": "a0dc1da85115658c9d15c531f77b0b17",
#         "sign": sign
#     }
#     return data
#
# headers = {
#             "User-Agent": "ozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36",
#             "Referer": "https://fanyi.baidu.com/",
#             "Cookie": "BAIDUID=B71CBE271F5649AF7071783EF06E6B1D:FG=1; BIDUPSID=B71CBE271F5649AF7071783EF06E6B1D; PSTM=1533963538; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; OUTFOX_SEARCH_USER_ID_NCOO=1467054029.667049; pgv_pvi=2560223232; BDRCVFR[feWj1Vr5u3D]=aeXf-1x8UdYcs; H_PS_PSSID=26525_1443_21088_29523_29518_29721_29567_29220; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1567002611,1567084721; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1566999482,1567084722; delPer=0; PSINO=6; __yjsv5_shitong=1.0_7_d0aca9eeddda11b304447412859bd137f167_300_1567086846195_171.221.52.149_f1d01c16; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567088285; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1567088285; yjs_js_security_passport=5a3e21485bb8aba56515522bec375f70257bec60_1567088290_js; ___rl__test__cookies=1567088290835"
# }
#
# def get_content(data):
#     # 发送请求获取响应
#     response = requests.post(
#         url="https://fanyi.baidu.com/basetrans",
#         headers=headers,
#         data=data
#     )
#     print(response.content.decode())
#     return response.json()["trans"][0]["dst"]
#
#
# query = "love"
# # sign = make_sign(query)
# sign =198772.518981
# data = make_data(query, sign)
#
# content = get_content(data)
# print(content)
#
#
#
#
