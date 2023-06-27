# 变量类型 在python中变量就是变量，它没有类型，我们所说的“类型”是变量所指的内存中对象的类型
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"

# 标准数据类型
'''
不可变数据：Number、String、Tuple（这些数据类型的值不能变）
可变数据：List、Dictionary、Set
'''


# Number（数字）支持int float bool complex
class A:
    pass


class B(A):
    pass


isinstance(A(), A)
type(A()) == A
isinstance(B(), A)
type(B()) == A
'''
python3中，bool是int的子类，True和False可以和数字相加，True==1、False==0会返回True，但可以通过is来判断类型
'''
issubclass(bool, int)
True == 1
False == 0
True + 1
False + 1
# 1 is True
# 0 is False
'''
可以通过del语句删除单个或多个对象
'''
var1 = 1
var2 = 2
var3 = 3
del var1
del var2, var3

# 数值运算
'''
python支持复数，复数有实数部分和虚数部分构成，可以用a+bj，或者complex(a, b)表示，a和b都是浮点数
'''

# String(字符串)
'''
三个'或者"构成的字符串可以做多行字符串也可以做注释
'''
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
'''
与C字符串不同的是，Python字符串不能被改变，比如word[0] = 'm'会导致错误，
这是由于python没有单个字符串导致的，字符穿不能改变，不代表字符变量不能付给其他值
'''

# 布尔类型
'''
布尔类型可以和其他数据类型进行比较，比如数字、字符串等
布尔类型也可以被转换成其他数据类型，比如浮点、整数和字符串
在python中所有非零的数字和非空的字符串、列表、元组等数据都被是为True，只有0、空字符串、空列表、空元组等被视为False
'''

# 列表
'''
和字符串一样，列表同样可以被所有和截取，列表被截取后返回一个包含所需元素的新列表
'''
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tiny_list = [123, 'runoot']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tiny_list * 2)
print(list + tiny_list)  # 连接列表

'''
列表元素是可以改变的
'''
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
a[2:5] = []

'''
Pyton列表截取可以接受第三个参数，参数作用是截取的步长，如果第三个参数为复数表示逆向读取
'''


def reverseWords(input):
    # 通过空格将字符串分隔
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1, 2, 3, 4]
    # inputWords[-1::-1]有三个参数
    # 第一个参数表示最后一个元素
    # 第二个参数为空表示移动到末尾至于是什么末尾看方向
    # 第三个参数为步长，-1表示逆向
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


# Tuple(元组)
'''
tuple与列表相似，不同指出在于元组的元素不能修改。
'''
tuple = ('abcd', 786, 2.23, 'runoob, 70.2')
tiny_tuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tiny_tuple * 2)
print(tuple + tiny_tuple)
'''
可以把字符串看成是一种特殊的元组
'''
'''
虽然tuple的元素不可改变，但是它可以包含可变的对象, 该对象不能替换成其他对象，但是该对象可以改变
'''
'''
构造包含0个或1个的元组比较特殊，所以有一些额外的语法规则
'''
tup1 = ()
tup2 = (20,)  # 一个元素需要在后面添加逗号

# Set(集合)
'''
基本功能是进行成员关系测试和删除重复元素
可以使用{}或者set()函数创建集合，注意：创建一个空集合必须使用set()而不是{},{}用来创建空字典
'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)

if 'Runoob' in sites:
    print("Runoob在集合中")
else:
    print("Runoob不在集合中")

# set可以进行集合运算，起到去重的作用
a = set("abababa")
b = set("acacacad")

print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b不同时存在的元素

# Dictionary(字典)
'''
字典是无序的对象集合，字典是通过键来存取的，而不是通过偏移存取
字典是一个无序的键值对的集合
键必须使用不可变类型
同一个字典中键是唯一的
'''
dict = {}
dict["one"] = "1-菜鸟教程"
dict[2] = "2-菜鸟工具"

tiny_dict = {"name": "runoob", "code": 1, "site": "www.runoob.com"}

print(dict['one'])
print(dict[2])
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())

# bytes类型
'''
bytes类型是不可变的二进制序列
与字符串类型不同的是，bytes类型中的元素是整数值（0到255之间的整数），而不是Unicode字符，即unicode编码中前面的数字
创建bytes对象的方式有多种，最常用的方式是使用b前缀
此外也可以使用bytes()函数将其他类型的对象转换为bytes类型。第一个参数为要转换的对象，第二个是编码方式，默认使用utf-8编码
'''
x = b"hello"
y = x[1:3]
z = x + b"world"
'''
由于bytes类型是不可变的，因此在修改操作时需要创建一个新的bytes对象，即x变量不能修改为其他值
'''
