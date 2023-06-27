# 迭代器
'''
迭代器是一个可以记住遍历位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器不会后退。
迭代器有两个基本方法：iter()和next()
字符串、列表和元组对象都可以用于创建迭代器对象
'''
list = [1, 2, 3, 4]
it = iter(list)  # 访问者模式，不管什么结构获取器迭代器，然后使用next访问，迭代器能记住当前访问的位置
print(next(it))

'''
迭代器对象可以使用常规的for语句进行遍历
'''
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")
'''
也可以使用next()函数
'''

import sys

list = [1, 2, 3, 4]
it = iter(list)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 创建一个迭代器
'''
把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__()
如果了解面向对象编程，就知道一个类都有一个构造函数，Python的构造函数为__init__(),他会在对象初始化时候执行
__iter__()方法返回一个特殊的迭代器对象，这个对象实现了__next__()方法并通过StopIteration标识迭代完成
__next__()方法会返回下一个迭代对象
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# StopIteration
'''
StopIteration异常用于标识迭代的完成，防止出现无限循环的情况，在__next__()方法中我们可以设置在完成指定循环次数后触发StopIteration一场结束迭代
迭代器是针对于特定类中数据结构而设计的遍历对象
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
    print(x)

# 生成器
'''
在Python中，使用了yield的函数被称为生成器
跟普通函数不同的是，生成器是一个返回迭代器的函数（调用__iter__()方法），只能用于迭代操作，更简单点的理解生成器就是一个迭代器
在调用生成器的过程中，每次遇到yiedl时函数会暂停保存当前所有的运行信息，返回yield的值，并在下一次执行next（）方法时从当前位置继续运行
调用一个生成器函数返回的是一个迭代器对象
'''
import sys


def fabonacci(n):  # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b, = b, a + b
        counter += 1


f = fabonacci(10)  # f是一个迭代器，有生成器返回生成,所以就是yield关键字就是返回一个保存当前函数运行状态的迭代器对象，函数执行也停止，具体实现不纠结
# 关键在于返回的迭代器是如何实现的

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
