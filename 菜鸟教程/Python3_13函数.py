'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

## 定义函数
def hello() :
   print("Hello World!")


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)

# 调用函数
hello();

print_welcome("Runoob")

w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
