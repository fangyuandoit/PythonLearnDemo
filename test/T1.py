import js2py
import requests



def stringCookies2Dict(cookies):
    cookiesDic = {}
    for line in cookies.split(";"):
        if line.find("=") != -1:
            name,value = line.strip().split("=")
            cookiesDic[name] = value
    return cookiesDic


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
url ="https://blog.csdn.net/qq_33588730/article/details/103095380"
cookies = "uuid_tt_dd=10_28747072280-1545632014365-712269; dc_session_id=10_1545632014365.804532; __guid=74049089.1403081268518617600.1559203816414.9272; acw_tc=2760820715744057703272424ec1cef9548113c66f1ec7a0de7b695a498736; acw_sc__v2=5dd786a897621af74beb5106ba9be9da7eb974c0; monitor_count=6; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1574405738; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1574405738; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_28747072280-1545632014365-712269; c-login-auto=1; announcement=%257B%2522isLogin%2522%253Afalse%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblogdev.blog.csdn.net%252Farticle%252Fdetails%252F103053996%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; dc_tos=q1cz8s"
text = requests.get(url, headers=headers,cookies = stringCookies2Dict(cookies)).text
print(text)
