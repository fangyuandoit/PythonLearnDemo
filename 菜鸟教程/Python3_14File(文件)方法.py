# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
# 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
'''
'''
file = open("C:\\Users\\fang\Desktop\\demo1.txt", "w")
file.write("asd")
file.close()
'''
'''
file = open("C:\\Users\\fang\Desktop\\demo1.txt", "r")
read = file.read()
print(read)
'''

'''
file = open("C:\\Users\\fang\Desktop\\demo1.txt", "r")
readlines = file.readlines()
iter__ = readlines.__iter__()
for x in iter__:
    print(x)
file.close()
'''

file = open("C:\\Users\\fang\Desktop\\demo.txt", "r")
print(file.read())


'''
1	
file.close()

关闭文件。关闭后文件不能再进行读写操作。

2	
file.flush()

刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3	
file.fileno()

返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4	
file.isatty()

如果文件连接到一个终端设备返回 True，否则返回 False。

5	
file.next()

返回文件下一行。

6	
file.read([size])

从文件读取指定的字节数，如果未给定或为负则读取所有。

7	
file.readline([size])

读取整行，包括 "\n" 字符。

8	
file.readlines([sizeint])

读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9	
file.seek(offset[, whence])

设置文件当前位置

10	
file.tell()

返回文件当前位置。

11	
file.truncate([size])

从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

12	
file.write(str)

将字符串写入文件，返回的是写入的字符长度。

13	
file.writelines(sequence)

向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''
