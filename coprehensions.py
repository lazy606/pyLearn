# python推导式
'''
python推导式是一种独特的数据处理方法，可以从一个数据序列狗爱你另一个新的数据序列的结构体
'''

# 列表推导式
'''
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]
或者
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

out_exp_res: 列表生成元素表达式，可以是有返回值的函数
for out_exp in input_list: 迭代input_list将out_exp传入到out_exp_res表达式中
if condition: 条件语句，可以过滤列表中不符合条件的值
'''
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 字典推导式
'''
{key_expr: value_expr for value in collection}
或
{key_expr: value_expr fro value in collection if condition}
'''
list_demo = ['Google', 'Runoob', 'Taobao']
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

# 集合推导式
'''
{expression for item in Sequence }
或
{expression for item in Sequence if conditional}
'''
new_set = {i ** 2 for i in (1, 2, 3)}

# 元组推导式(生成器表达式)
'''
(expression for in item in Sequence)
或
(expression for item in Sequence if conditional)
元组推导式和元组推导式的用法也完全相同，只是元组推导式用()圆括号将各个部分括起来，而列表推导式用是中括号，另外元组推导式返回的结果是一个生产器对象
'''
a = (x for x in range(1, 10))
type(a)
tuple(a)
