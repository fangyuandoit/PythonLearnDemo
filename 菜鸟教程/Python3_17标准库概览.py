import math
import os
import glob
from urllib.request import urlopen

print(os.getcwd())  # # 返回当前的工作目录

print( glob.glob('*.py'))

print( math.cos(math.pi / 4))


for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)
