# Python数据结构

# 将列表当做堆栈用
'''
使用append()和pop()方法
'''

# 将列表当作队列用
'''
可以把列表当作队列用，但是拿列表用作这样的目的效率不高，在列表的最后添加或者弹出元素速度苦熬，而在列表里插入或者从头弹出速度却不快
'''
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()

# del语句
'''
使用del语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用pop()返回一个值不同。可以用del语句从列表中删除一个切割或者请看整个列表
'''

# 字典遍历技巧
'''
在字典中遍历是，关键字和对应的值可以使用items()方法解读出来
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

'''
在序列遍历中，索引位置和对应值可以使用enumerate()同时得到
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

'''
同时遍历两个或更多序列可以使用zip()组合
'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
