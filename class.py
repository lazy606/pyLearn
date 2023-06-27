# 面向对象简介
'''
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
'''

# 类定义
'''
语法格式如下:
class ClassName:
    语句1
    语句2
    ....
'''

# 类对象
'''
类对象支持两种操作：属性引用和实例化
属性引用和Python中所有的属性引用使用一样的标准语法：obj.name
类有一个名为__init__()的特殊方法，该方法在类实例化时会自动调用
'''

# Self代表类的实例而非类
'''
类的方法与普通的函数只有一个特别的区别--他们必须有一个额外的第一个参数名称，按照惯例它名称时self
self不是python关键字，我们把他换成runoob也是可以正常执行的
'''


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


# 类的方法
'''
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
'''

# 继承
'''
类继承语法格式:
class DerivedClassName(BaseClassName):
    语句1
    语句2
    ...
子类会继承父类的属性和方法
BaseClassName实例中基类名必须与派生类定义在一个作用域内。除了类，可以用表达式，积累定义在另一个模块中时非常有用
class DerivedClassName(modname.BaseClassName):
'''


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("{0}说：我{1}岁".format(self.name, self.age))


class student(people):
    grade = ''

    def __init__(self, name, age, weight, grade):
        people.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 方法重写
'''
super() 函数是用于调用父类(超类)的一个方法。
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
'''

# 类属性与方法
'''
类的私有属性
__private_attrs: 两个下划线开头，声明该属性为私有，不能在外部被使用或直接访问。在类的内部的方法中使用self.__private_attrs（这个self相当于Java的this）

类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。

类的私有方法
__private_method:两个下划线开头，声明方法为私有方法，只能在类的内部调用

不要纠结这些语言背后的实现细节只要知道语言怎么使用的即可
'''


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

# 类的专有方法（即Object类的方法）
'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方

现在要学的时告诉解释器怎么做，而不是了解解释器怎么做
'''


# 运算符重载

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
