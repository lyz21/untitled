"""
元组测试
    -元组与列表基本类似，但是元组不可更改，列表可更改
    -空元组创建  tup1=()
"""
print('创建元组----------------------------')
tup1 = ('stu1', 'stu2', 'stu3', 'stu4')  # String类型元组
tup2 = (1, 2, 3, 4, 5, 6, 7, 8)  # 整型类型元组
tup3 = 'user1', 'user2', 'user3', 'user4'  # 不需要括号也可以
tup4 = (1,)  # 如果元组内只有一个元素，需要在后面加上','，否则会当成整型处理
print('输出元组----------------------------')
print('元组1：', tup1)
print('元组2：', tup2)
print('元组3：', tup3)
print('元组4：', tup4)
print('元组2的第2到4个元素：', tup2[1:4])
print('元组2的第1个元素：', tup2[0])
print('连接元组----------------------------')
tup5 = tup1 + tup2
print(tup5)
print('删除元组----------------------------')
# 列表可删除其中某个元素，元组只能删除整个元组
# del tup4  #先注释掉，会报错
print(tup4)
print('元组运算符----------------------------')
'''
len()   元素个数
+       连接
*       复制
in      元素是否存在
for x in tup : print(x) 迭代
'''
a = 10
if a in tup2:
    print('{}在元组tup2中'.format(a))
else:
    print('{}不在元组tup2中'.format(a))
print('tup5:')
for x in tup5:
    print(x)
print('元组内置函数----------------------------')
'''
len()   元素个数
max()   元组中元素最大值
min()   最小元素
tuple() 列表转元组
'''
print('tup2:', tup2)
print('len(tup2):', len(tup2))
print('max(tup2):', max(tup2))
print('min(tup2):', min(tup2))
