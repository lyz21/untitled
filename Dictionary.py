"""
字典测试
    -键值对{key1:value1,key2:value2}
    -空字典创建  dict={}
    -1、键不可重复
    -2、键不可变，因此键可以用数字、字符串、元组，不可用列表（列表可变）
"""
print('创建字典--------------------------------------')
dict1 = {'name': 'lyz', 'age': 21, 'class': '12'}

print('访问字典--------------------------------------')
print('dict1的name：', dict1['name'])

print('修改字典--------------------------------------')
dict1['age'] = 22
print('dict1的age：', dict1['age'])

print('删除字典--------------------------------------')
del dict1['class']  # 删除dict1的class
dict1.clear()  # 清空字典
del dict1  # 删除字典

print('内置函数-------------------------------------')
'''
len()   字典元素总数
str()   输出字典
type()  输出类型。若是字典类型则会输出<class 'dict'>
'''
dict1 = {'name': 'lyz', 'age': 21, 'class': '12'}
print('dict1:', dict1)
print('str(dict1):', str(dict1))
print('type():', type(dict1))

print('内置方法-------------------------------------')
'''
1	radiansdict.clear()                 删除字典内所有元素
2	radiansdict.copy()                  返回一个字典的浅复制
3	radiansdict.fromkeys()              创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
5	key in dict                         如果键在字典dict里返回true，否则返回false
6	radiansdict.items()                 以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()                  返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)   和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)           把字典dict2的键/值对更新到dict里
10	radiansdict.values()                返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])                  除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()                           随机返回并删除字典中的一对键和值(一般删除末尾对)。
'''
print('dict1.keys():', dict1.keys())
print('dict1.values():', dict1.values())
print(dict1)
print('dict1.pop():', dict1.pop('class'))
print(dict1)
