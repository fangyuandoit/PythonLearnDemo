#!/usr/bin/python3
import re

contet="微博密码是:123,qq密码是:456,微信密码是:789,"
list = re.search(":(.*?),", contet)
print(list)
print(list.group(0))  #参数为0 打印匹配的内容和左右符号
print(list.group(1))  # 参数为1  打印真正的匹配内容




