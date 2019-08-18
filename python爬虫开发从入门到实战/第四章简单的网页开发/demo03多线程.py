#!/usr/bin/python3

#  单线程  计算 0-9 的平方
# for i in  range(10):
#     print(i * i)




#  多线程  计算 0-9 的平方
from multiprocessing.dummy import Pool

def cal_power(num):
    return num*num;

pool =Pool(3)
nuns = [x for x in range(10)]
result =pool.map(cal_power,nuns)
print(result)







