print("Hello world")
# 从键盘上输入
# x = input("请从键盘输入")
# print(x)

'''
中括号[ ]：用于定义列表或引用列表、数组、字符串及元组中元素位置
冒号： 用于定义分片、步长。
'''
list = [1, 2, 3, 4, 5]
# 最后一位
print(list[-1])
# 输出2，3
print(list[1:3])
# 从第一位到第三位
print(list[:3])
# 从第一位到倒数第二位
print(list[:-1])
# 从3到1 步长为-1 不包括1
print(list[3:1:-1])

print(list)
print(list[:])
'''
a[:] 是创建 a 的一个副本，这样在代码中对 a[:] 进行操作，就不会改变 a 的值。
而若直接对 a 进行操作，那么 a 的值会受到操作的影响，如 append() 等。
'''
print(list is list[:])

print(dir())

# 会在终端help
# print(help())
'''
import的解释：
import task as task  导入的是一个模块

from math import pi  导入的是特定的函数
'''
'''
pep8介绍：
是一种书写规范，和其他语言差不多  看看源码就好了
'''

'''
基础数据类型
'''
x = 2
str = '123'

pow=2**5

e=3e5
print(x,str,pow,e)

'''
基本运算符

算数运算符

包括

“+”
“-“
“*”
“/“
“%” 取模
“**” 乘方
“//“ 整除
逻辑运算符

包括
“==” 判断两个值是否相等
“!=””<>” 判断两个值是否不相等
“<”
“>”
“>=”
“<=”
赋值运算符

包括
“=”
“+=”
“-=”
“*=”
“/=”
“%=”
“**=”
“/=”
“=”是变量赋值。

a += b 即 a = a + b，其他同理。

位运算符

一些基本的位运算操作。

“&” 与
“|” 或
“^” 异或
“~” 取反
“<<” 左移
“>>” 右移
了解基本逻辑运算的都不用解释。

逻辑运算符

包括

“and”
“or”
“not”
成员运算符

判断是否为成员。

“in”
“not in”
身份运算符

判断两个变量是否指向同一个对象。

“is”
“is not”
'''