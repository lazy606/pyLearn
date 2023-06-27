# 隐式类型转换
'''
我们对两种不同类型的数据进行运算，较低数据类型就会转换到较高数据类型以避免数据丢失
'''
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

'''
整型和字符串类型运算结果会报错，这种情况下Python无法使用隐式转换
'''

# 显示转换
'''
在显示类型转换中，用户将对象的数据类型转换为所需的数据类型。
'''
num_int = 123
num_str = "456"

print("num_int数据类型为：", type(num_int))
print("类型转换前,num_str数据类型为：", type(num_str))

num_str = int(num_str)
print("类型转换后，num_str数据类型为：", type(num_str))

num_sum = num_int + num_str

print("num_int与num_str相加结果为：", num_sum)
print("sum数据类型为：", type(num_sum))
