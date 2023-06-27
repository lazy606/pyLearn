# 输出格式美化
'''
python有两种输出值的方式：表达式语句和print()函数
第三种方式是使用文件对象的write()方法，标准输出文件可以采用sys.stdout引用
如果希望将输出的形式更加多样化，可以使用str.format()函数来格式化
如果你希望将输出的值转成字符串，可以使用repr()或者str()函数来实现
    str():函数返回一个用户易读的表达式
    repr(): 产生一个解释器易读的表达形式，可以转义字符串中的特殊字符串，参数可以是Python的任何对象
print(): Prints the values to a stream, or to sys.stdout by default
'''
s = "Hello, Runoob"
print(str(s))
print(repr(s))

'''
括号及其里面的字符将会被format()中的参数替换
在括号中的数字用于指向传入对象在format()中的位置
如果在format()中使用了关键字参数，那么它们的值会指向使用该名字的参数
!a、!s、!r等可以用于在格式化某个值之前对其进行转换
可选项:和格式标识符可以跟着字段名。这就允许更好的格式化
在:后传入一个整数，可以在保证该域至少有这么多的宽度
'''
import math

print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

'''
如果有一个很长的格式化字符串，不想将它分开，那么在格式化时通过变量名而非位置会更方便
最简单的就是传入一个字典，然后使用[]来访问键值
'''
table = {"Google": 1, "Runoob": 2, "Taobao": 3}
print("Runoob: {0[Runoob]:d;Google: {0[Google]:d}; Taoabo: {0[Taobao]:d}".format(table))

# 旧字符串格式化
print('常量 PI 的值近似为：%5.3f。' % math.pi)

# 读取键盘输入
'''
Python提供了input()内置函数从标准输入读入一行文本，默认的标准输入时键盘
'''
str = input("请输入：")

# 读和写文件
'''
open()将会返回一个file对象，基本语法格式如下：
    open(filenaem, mode)
'''
f = open("./foo.txt", "w")

f.write("Python是一个非常好的语言。\n是的,的确非常好\n")

f.close()  # 关闭打开的文件

# 文件对象的方法
'''
f.read()
为了读取一个文件的内容，调用f.read(size),这将读取一定数目的数据，然后作为字符串或者字节对象返回
size是一个可选的数字类型的参数。当size被忽略或者为负，那么该文件的所有内容都将被读取并且返回
'''

'''
f.readline()
会从文件中读取单独的一行。换行符为'\n'。如果返回一个空字符串，说明已经读取到最后一行。
'''

'''
f.readlines()
f.readlines()将返回该文件包含的所有行，如果设置可选参数sizehint则读取指定长度的字节，并且将这些字节按行分割
'''

f = open("foo.txt", "r")

str = f.readlines()
print(str)

f.close()

'''
另一种方式是迭代一个文件对象然后读取每一行
'''
f = open("foo.txt", "r")

for line in f:
    print(line, end='')

f.close()

'''
f.write()
将string写入到文件中，然后返回写入的字符数
如果要写入一些不是字符串的东西，那么将需要先进行转换
'''

'''
f.tell()返回文件对象当前所处的位置，它是从文件开头算起的字节数
'''

'''
f.seek()
如果要改变文件指针当前的位置，可以使用f.seek(offset, from_what)函数
from_what的值，如果是0标识开头，如果是1标识当前位置，2标识文件的结尾，如：
    · seek(x, 0)从起始位置开始移动x个字符
'''

'''
f.close()
在文本文件中(那些打开文件的模式下没有b的)，只会相对于文件其实位置进行定位
当你处理完一个文件后，调用f.close()来关闭文件并释放系统的资源，如果在调用该文件则会抛出异常
'''

'''
当处理一个文件对象是，使用with关键字是非常好的方式，
在结束后他会帮你正确关闭文件，相对try-finally语句也要简短(with实现？)
'''
with open('/tmp/foo.txt', 'r') as f:
    read_data = f.read()
f.close()

# pickle模块
'''
python的pickle模块实现了基本数据序列和反序列化
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
通过pickle模块的反序列化操作我们能从文件中创建上一次程序保存的对象
'''

'''
序列化（Serialization）是指将数据结构或对象转换为一种特定格式的字节序列，以便于存储、传输或在不同系统之间进行交换。序列化后的数据可以被保存到文件或通过网络发送，以便稍后重新创建原始对象。
序列化的过程涉及将数据结构或对象转换为线性化的字节序列。这个过程包括将数据的状态（值和属性）转换为字节表示，并将其写入文件或传输给其他系统。常见的序列化格式包括JSON、XML、pickle等。
反序列化（Deserialization）是指将序列化后的字节序列重新转换为原始的数据结构或对象。反序列化过程将字节序列解析为数据的状态，并创建相应的数据结构或对象。
通过序列化和反序列化，可以在不同的系统或平台之间共享数据，实现数据持久化、数据传输和远程通信等功能。序列化和反序列化在许多应用中非常重要，例如在网络通信、分布式系统、缓存、对象持久化等领域都有广泛的应用。
'''

'''
是的，通常情况下，在序列化过程中，只会存储对象的属性值，而不存储属性名。
序列化的目标是将对象转换为字节序列，以便于存储、传输或在不同系统之间进行交换。属性名通常被视为对象的结构信息，而不是对象的状态信息。在序列化的过程中，主要关注对象的状态，即属性的值，而不是属性的名称。
序列化过程中，根据所使用的序列化协议或格式，会将对象的属性值提取出来，并将其转换为字节序列。这样可以在反序列化时，根据特定的规则将字节序列解析为原始对象，并为其恢复属性值。
但需要注意的是，某些序列化协议或格式，如JSON，可能会在序列化时记录属性名和属性值的键值对。这取决于所使用的具体序列化方式和选项。但一般情况下，在典型的二进制序列化格式中，只存储属性值而不存储属性名。
'''

'''
在反序列化过程中，虽然属性名通常不会被直接存储在字节序列中，但在某些序列化协议或格式中，会使用一些附加信息来帮助恢复对象的属性。

以下是一些常见的方法，用于在反序列化时恢复对象的属性：

1. 协议/格式规范：许多序列化协议或格式会规定一些约定，用于指示属性的顺序或标识。例如，某些二进制格式可能使用属性的索引或位置来确定属性的顺序，从而帮助恢复对象。
2. 类型信息：某些序列化格式会在序列化时记录对象的类型信息，包括对象所属的类或其类名。反序列化时，可以使用这些类型信息来创建对象的实例，并根据属性值的顺序或其他标识恢复对象的属性。
3. 额外的元数据：有些序列化格式可能会在字节序列中包含一些额外的元数据，例如属性名的映射或描述。这些元数据可以帮助在反序列化时关联属性值与其对应的属性名，以便正确地设置对象的属性。
需要注意的是，这些方法的具体实现方式取决于所使用的序列化协议或格式。不同的序列化方式可能具有不同的机制来恢复对象的属性。因此，在进行反序列化时，需要使用相应的反序列化方法和选项，以确保正确地恢复对象的属性和状态。
'''

'''
基本接口:
pickle.dump(obj, file [,protocol])
有了pickle对象就能对file以读写的形式打开
x = pickle.load(file)
从file中读取一个字符串，并将它重构为原来的python对象
file类文件对象，有read()和readline接口
'''
import pickle  # 使用pickle模块将数据对象保存到文件

data_1 = {
    "a": [1, 2.0, 3, 4 + 6j],
    "b": ("string", u"Unicode string"),
    "c": None
}

self_ref_list = [1, 2, 3]

self_ref_list.append(self_ref_list)

output = open("data.pkl", "wb")

# pickle dictionary using protocol 0
pickle.dump(data_1, output)

# Pickle the list using the highest protocol available. -1是什么含义
pickle.dump(self_ref_list, output, -1)

output.close()

import pprint, pickle

# 使用pickle模块从文件中重构python对象
pkl_file = open("data.pkl", "rb")

data_1 = pickle.load(pkl_file)
pprint.pprint(data_1)

pkl_file.close()
