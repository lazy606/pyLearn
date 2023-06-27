# 字符串（String）
import sys

str = '123456789'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str * 2)
print(str + '你好')

print('--------------------------------------')

print('hello\nrunoob')
print(r'hello\nrunoob')

# 等待用户输入
input("\n\n按下enter键后退出")

# print输出
x = 'a'
y = 'b'
print(x)
print(y)

print('--------------------')
print(x, end=' ')
print(y, end=' ')
print()

# import与from...import

'''导入sys模块'''
import sys

print('==================================Python import mode============================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\npython路径为', sys.path)

'''导入sys模块的argv，path成员'''
from sys import argv, path

print('=================================pyton from import=============================')
print('path:', path)
