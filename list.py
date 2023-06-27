# Python列表
'''
序列是Python中最基本的数据结构
Python有6个序列的内置类型，但最常见的是列表和元组
序列都可以进行的操作包括索引，切片，加，乘， 检查成员
Python内置了确定序列长度以及确定最大最小元素的方法

索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2
'''

# 访问列表中的值

# 更新列表
list = ["Google", "Runoob", 1997, 2000]

print("第三个元素为:", list[2])
list[2] = 2001
print("更新后第三个元素为:", list[2])

list.append("Baidu")
print("更新后的列表:", list)

# 删除列表元素,使用del删除，之后使用remove（）方法
print("原始列表:", list)
del list[2]
print("删除第三个元素:", list)

# Python列表操作符
'''
len()求长度
+号用于列表拼接
*号用于重复
in用于判断是否存在
for in []用于迭代
'''

# 列表比较，列表比较需要引入operator模块的eq方法
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a, b):", operator.eq(a, b))
print("operator.eq(c, b):", operator.eq(c, b))

# Python列表内置函数和列表对象方法，函数相当于工具类便于通用，方法是每个类特有的方法
