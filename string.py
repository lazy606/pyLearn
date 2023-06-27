# python转义字符
print("Hello \v World")  # 纵向制表符
print("google runoob taobao\r123456")  # 回车将\r后面的内容转移到字符串开头
print("Hello \f World!")  # 换页

import time  # 百分比进度条简单实现

for i in range(101):
    print("\r{:3}%".format(i), end=" ")
    time.sleep(0.05)

# Python字符串运算符
'''
[:]截取字符串中的一部分，遵循左闭右开原则
%表示格式化字符
'''

# Python字符串格式化
'''
Python支持格式化字符串的输出，尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串%s的字符串中，字符串格式化使用与C中sprintf函数一样的语法
'''
print("我叫 %s 今年 %d岁！" % ("小明", 10))

'''
%p用十六进制格式化变量的地址
'''

# Python三引号
'''
三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符串。
'''
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )
也可以使用换行符 [ \n ]
"""
print(para_str)

# f-string
'''
f-string称之为字面量格式化字符串，是新的格式化字符串的语法
f-string格式化字符串以f卡头，后面跟着字符串，字符串中的表达式用大括号{}包起来，它会将变量或者表达式计算后的值替换进去
'''
name = "Runoob"
f"Hello {name}"  # 使用变量
f"{1 + 2}"  # 使用表达式
w = {"name": "Runoob", "url": "www.runoob.com"}
f"{w['name']}: {w['url']}"

'''
在Python3.8版本中可以使用=符号来拼接表达式运算的结果
'''
x = 1
print(f'{x + 1}')
print(f"{x+1=}")

# Unicode字符串

# Python字符串内建函数
