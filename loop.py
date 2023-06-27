# while循环
'''
Python中没有do...while循环
'''

# 无限循环

# while循环使用else语句
'''
如果while后面的条件语句为false，则执行else语句
'''
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")  # 这个语句块有什么含义？

# 简单语句组
'''
类似于if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
'''
flag = 1
while (flag): print("欢迎访问菜鸟教程")
print("Good bye!")

# for语句
'''
for循环可以遍历任何可迭代对象
'''
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

# for...else
'''
在Python中，for...else语句用于在循环结束后执行一段代码，
如果在循环的过程中遇到了break语句则会中断循环这不会执行else子句，这样就使得else也是循环语句块的一部分而不是整个程序的
'''

# range()函数用于生成数列

# break和continue即else语句

# pass语句
'''
Python的空语句是pass， 是为了保持程序结构的完整性
'''
