import base64
import random
import re
import time

# 获取13位时间戳
import js2py
import requests
import rsa
from binascii import b2a_hex



def getCurrTimestamp():
        t = time.time()
        currTime = int(round(t * 1000))

#字符串转base64
def string2Base64(sourceMessage):
    encodeByte = base64.b64encode(sourceMessage.encode('utf-8'))
    encodeMessage = str(encodeByte, 'utf-8')
    return encodeMessage;

class MyWeibo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()  # 登录用session
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        self.session.verify = False



    def prelogin(self):
          self.su = string2Base64(self.username)
          url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su={}&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_={}'.format(
             self.su, getCurrTimestamp())
          response = self.session.get(url).content.decode()
          self.nonce = re.findall(r'"nonce":"(.*?)"', response)[0]
          self.pubkey = re.findall(r'"pubkey":"(.*?)"', response)[0]
          self.rsakv = re.findall(r'"rsakv":"(.*?)"', response)[0]
          self.servertime = re.findall(r'"servertime":(.*?),', response)[0]
          return self

    def get_sp(self):
        '''用rsa对明文密码进行加密，加密规则通过阅读js代码得知'''
        publickey = rsa.PublicKey(int(self.pubkey, 16), int('10001', 16))
        message = str(self.servertime) + '\t' + str(self.nonce) + '\n' + str(self.password)
        self.sp = rsa.encrypt(message.encode(), publickey)
        return b2a_hex(self.sp)



    def login(self):
        url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'qrcode_flag': 'false',
            'useticket': '1',
            'pagerefer': 'https://login.sina.com.cn/crossdomain2.php?action=logout&r=https%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
            'vsnf': '1',
            'su': self.su,
            'service': 'miniblog',
            'servertime': str(int(self.servertime) + random.randint(1, 20)),
            'nonce': self.nonce,
            'pwencode': 'rsa2',
            'rsakv': self.rsakv,
            'sp': self.get_sp(),
            'sr': '1536 * 864',
            'encoding': 'UTF - 8',
            'prelt': '35',
            'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META',
        }
        response = self.session.post(url, data=data, allow_redirects=False).text  # 提交账号密码等参数
        redirect_url = re.findall(r'location.replace\("(.*?)"\);', response)[0]  # 微博在提交数据后会跳转，此处获取跳转的url
        result = self.session.get(redirect_url, allow_redirects=False).text  # 请求跳转页面
        ticket, ssosavestate = re.findall(r'ticket=(.*?)&ssosavestate=(.*?)"', result)[0]  # 获取ticket和ssosavestate参数
        uid_url = 'https://passport.weibo.com/wbsso/login?ticket={}&ssosavestate={}&callback=sinaSSOController.doCrossDomainCallBack&scriptId=ssoscript0&client=ssologin.js(v1.4.19)&_={}'.format(
            ticket, ssosavestate, getCurrTimestamp())
        data = self.session.get(uid_url).text  # 请求获取uid
        uid = re.findall(r'"uniqueid":"(.*?)"', data)[0]
        print(uid)
        # home_url = 'https://weibo.com/u/{}/home?wvr=5&lf=reg'.format(uid) #请求首页
        # home_url = "https://weibo.com/xiaogang2099" #请求首页
        # html = self.session.get(home_url)
        # html.encoding = 'utf-8'
        # print(html.text)

        text = requests.get("https://weibo.com/xiaogang2099", cookies=self.session.cookies.get_dict()).text
        print(text)

    def main(self):
        self.prelogin()
        self.get_sp()
        self.login()

        print(self)



if __name__ == '__main__':
    username = 'xx' # 微博账号
    password = 'xx' # 微博密码
    weibo = MyWeibo(username,password)
    weibo.main()