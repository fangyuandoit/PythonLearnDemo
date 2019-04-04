#!/usr/bin/python3
import re

contet="微博密码是:123,qq密码是:456,微信密码是:789,"
list = re.findall(":(.*?),", contet)
print(list)

