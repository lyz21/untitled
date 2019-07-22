"""
函数测试
    - def 函数名 (参数列表)：
        函数体
"""
print("测试1---------------------")


# 定义函数
def printme(str):
    print(str)
    return


# 调用
printme('第一个函数')
print(1111)

print("测试2---------------------")


# 加了*的参数会以元组形式导入
def printlyz(str1, *str):
    print(str1)
    print(str)


printlyz(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('测试3-----------------------')


# 加了**的参数以字典形式导入
def printlyz2(str1, **str2):
    print(str1)
    print(str2)


printlyz2('lyz:', a=1, b=2, c='c')

print('匿名函数-------------------------')
'''
匿名函数
    -lambda
'''
sum = lambda a, b: a + b
print(sum(10, 20))

print('变量作用域-------------------------')
'''
内部作用域想修改外部作用域
    -global
    -nonlocal
'''
# global
num = 10


def fun1():
    global num
    num = 100
    print(num)


fun1()
# nonlocal
def fun2():
    number=10
    def fun21():
        nonlocal number
        number=100
        print(number)
    fun21()

fun2()