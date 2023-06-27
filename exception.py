# 错误和异常
'''
Python有两种错误很容易判断：语法错误和异常，要保持一个接纳谦虚的态度，不要抵触
'''

# 语法错误

# 异常
'''
即使语法是正确的，但是他在运行的时候，也可能发生错误。运行期间检测的错误称为异常
'''

# 异常处理
'''
首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。

如果没有异常发生，忽略 except 子句，try 子句执行后结束。

如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。

如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
'''

'''
一个try语句可能包含多个except子句，分别用来处理不同的特定的异常。最多只有一个分支会被执行，
处理程序将只针对对应的try子句中的异常进行处理，而不是其他try的处理程序中的异常
一个except子句可以同时处理多个异常，这些异常被放在一个括号里成为一个元组

except (RuntimeError, TypeError, NameError):
    pass
'''

'''
最后一个except子句可以忽略异常的名称，它将被当作通配符使用，使用这种方法将异常输出然后抛出
'''

# try/except...else
'''
try/except语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后
else子句将再try子句没有发生任何异常的时候执行

使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。
'''

# try-finally语句
'''
finally语句是无论是否发生异常都将执行最后的代码
'''

# 抛出异常
'''
python使用raise语句抛出一个指定的异常。
语法格式如下：
raise [Exception[,args [, traceback]]]
'''

'''
raise唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者是异常的类（也就是Exception的子类）
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的raise语句就可以再次把它抛出。
'''

# 用户自定义异常
'''
可以通过创建一个新的异常类来拥有自己的异常，异常类继承字Exception类，可以直接继承，或者间接继承
'''

'''
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
   
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
   
My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'

try就是用来捕获器代码块中raise的异常，最后抛出的异常由解释器捕获
'''

'''
当创建一个模块有可能抛出多种不同的异常是，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误创建不同的子类
'''

# 定义清理行为
'''
使用finally子句定义清理行为
如果一个异常再try子句里(或者再except和else子句里被抛出)，而又没有任何的except把它截住，那么这恶鬼异常会 在finally子句执行后 被抛出
'''

# 预定义的清理行为
'''
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它，那么这个标准的清理行为就会执行
关键字with语句就可以保证注入文件子类的对象在使用完之后一定会正确的执行他的清理方法
'''

# with关键字
'''
Python中的with语句用于异常处理，封装了try...exception...finally编码方式，提高了易用性
'''

'''
file = open('./test_runoob.txt', 'w')
file.write('hello world !')
file.close()
以上代码如果在调用 write 的过程中，出现了异常，则 close 方法将无法被执行，因此资源就会一直被该程序占用而无法被释放。 接下来我们呢可以使用 try…except…finally 来改进代码：
使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。
'''

'''
with 语句实现原理建立在上下文管理器之上。
上下文管理器是一个实现 __enter__ 和 __exit__ 方法的类。
使用 with 语句确保在嵌套块的末尾调用 __exit__ 方法。
'''
