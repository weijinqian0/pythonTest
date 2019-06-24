'''
列表：标志、基本操作(创建，append( )，pop( ) ,del( ), 拷贝）、列表相关方法
'''
list1 = [1, 2, 3, 4]
print(list1)
list2 = ['abc'] + list1
print(list2)
# 添加到最后面
list1.append('aaa')
print(list1)
# 默认pop最后一个
list1.pop()
print(list1)

# 删除元素
list1.remove(1)
print(list1)

# 拷贝,是深拷贝 证明全部拷贝成功了
print(list1)
list3 = list1.copy()
list3.remove(4)
print(list3)
print(list1)

'''
元组：标志、基本操作（创建及不可变性）

'''
# 元组是通过通过圆括号设置的
t1 = ('abc', '1', 2)
print(type(t1))

print(t1[0])
# 不可更改 会抛异常
# t1[0] = '124'

# 元组可遍历
y = [x for x in t1]
print(type(y))

print(y)

# 元组转换列表

z = list(t1)
print(type(z))

print(type(tuple(list1)))

'''
string字符串：定义及基本操作（+，*，读取方式）、字符串相关方法、字符串格式化问题
'''

str = '123456'
print(str + '111')
print(str * 3)
print(str[0])
# 访问和list一样
print(str[:])
print(str[2:])
print(str[:5])
print(str[-1:])
print(str[:-1])
print(str[:5:2])
print(str[-5:-2])

# 字符串常用函数

str1 = 'abcd:1'
print(str1.capitalize())
print(str1.upper())
print(str.startswith('ab'))
print(str.endswith('cc'))

# 无参数
str = 'Hello {}'
print(str.format('world', '!'))


# 索引参数
str = 'I {0} {1} {0} {1}'
str.format('love', 'you')
'I love you love you'

# 关键字参数
str = 'I {a} {b}'
print(str.format(a = 'love', b = 'you'))
