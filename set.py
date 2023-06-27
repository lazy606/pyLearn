# Python3集合
'''
可以使用{}或者set()函数创建集合，注意:创建一个空集合必须使用set()而不是{}，因为{}是用来创建一个空字典的
'''

# 添加元素
this_set = {"Google", "Runoob", "Taobao"}  # s.add()
this_set.add("Facebook")
print(this_set)

this_set.update({1, 3})  # s.update()
this_set.update([1, 4], [5, 6])

# 移除元素
'''
s.reomve("Taobao")
s.discard("Facebook")
s.pop() 随机删除一个元素
'''
