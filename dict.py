# Python3字典
'''
字典的键必须唯一且必须是不可变的，如字符串、数字，对象不行因为对象是可变的（与字典的设计密切相关）
(有没有可能python解释器中都是对象，即解释器是面向对象的，python语言本身自由度较高)
'''

# 访问字典里的值
tiny_dic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tiny_dict['Name']:", tiny_dic['Name'])
print("tiny_dict['Age']:", tiny_dic['Age'])

# 修改字典

# 删除字典元素

del tiny_dic['Name']  # 删除键'Name'
tiny_dic.clear()  # 清空字典
del tiny_dic  # 删除字典

print("tiny_dict['Name']:", tiny_dic['Name'])
print("tiny_dict['Age']:", tiny_dic['Age'])

# 字典特性
'''
字典值可以是任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行
'''
tiny_dic = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}  # 不允许同一个键出现两次，创建是如果同一个键被赋值两次，后一个值就会被记住
print("tiny_dict['Name']:", tiny_dic['Name'])

tiny_dic = {['Name']: 'Runoob', 'Age': 7}
print("tiny_dic['Name']:", tiny_dic['Name'])  # 键必须是不可变，所以可以用数字、字符串或者元组充当，而用列表就不行

# 字典内置函数和方法
'''
len计算字典元素个数，即键的总数
str输出字典可以打印
'''

# Python字典的视图对象
'''
dict.keys()、dict.values()、dict.items()返回的都是视图对象，提供字典实体的动态视图，这就意味着字典改变，视图也会跟着改变，视图对象不是列表，'
    不支持索引，但可以使用list()来转换列表,我们不能对视图对象进行修改，因为字典的视图对象都是只读的
'''
