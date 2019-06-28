# dict 创建 定义等方法
Data = {"a": 1, 'b': 2, 'c': 3}
# 可见这个是深拷贝
Data1 = Data.copy()

Data['a'] = 4
print(Data)
print(Data1)

if ('c' in Data):
    print("c is In data")

print(Data.items())

x = Data.pop('a')
print(x)
#  三目表达式
a = 3
b = 4
c = 5
print(a if c != 5 else b)

# 循环遍历
for x in Data:
    print(x)
    print(Data[x])
