"""
列表测试
    -python的6个序列中最常用的一个
"""
list1 = ['lyz', 'yjj', 'stu1', 'stu2']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('访问列表操作-----------------------')
print('list1:', list1)  # 输出整个列表
print('list1[0]:', list1[0])  # 输出list1的第一个元素
print('list2[1:3]:', list2[1:3])  # 输出list2的第2到第3个数
print('list1[0][1]：', list1[0][1])  # 输出list1的第1个元素的第2元素
print('list1[2:]：', list1[2:])  # 输出list1的第3个元素及之后的元素
print('list2[1:7:2]', list2[1:7:2])  # list2从第二个到第七个隔2输出
print('list2[-2]', list2[-2])  # list2倒数第二个元素
print('更新列表操作-----------------------')
list1[0] = '哈哈哈'
print(list1)
print('删除列表操作---del-----------------')
del list1[0]
print(list1)
list1[0] = 'lyz'
print(list1)
print('列表脚本操作符--------------------')
'''
输出n遍    *n
列表相加    +
是否在列表中  in
迭代遍历    for x in list:
'''
list1_len = len(list1)  # 获取长度 len()
print(list1_len)
print('list1*2：', list2 * 2)  # 输出两遍    *2
print('list1 + list2：', list1 + list2)  # 两个列表相加    +
x = 30
if x in list2:  # 判断是否在列表中  in
    print('{}在list2中'.format(x))
else:
    print('{}不在list2中'.format(x))
for a in list2:     # 迭代遍历
    print(a)
print('列表函数--------------------')
'''
len()       列表元素个数
max()       列表最大元素
min()       列表最小元素
list()      将元组转化为列表
'''
list3 = [1, 2, 6, 90, 4, 1]
print(max(list3))
print('列表方法--------------------')
'''
序号	方法
1	list.append(obj)    在列表末尾添加新的对象
2	list.count(obj)     统计某个元素在列表中出现的次数
3	list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj) 将对象插入列表
6	list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)    移除列表中某个值的第一个匹配项
8	list.reverse()      反向列表中元素
9	list.sort( key=None, reverse=False) 对原列表进行排序
10	list.clear()        清空列表
11	list.copy()         复制列表
'''
list3.append(4)
print(list3.count(4))