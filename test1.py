print("字符串测试-----------------------------------")
str="123"           # "" 和 '' 效果一样
str2="abc"
var1=",.?"
print(str)          #输出字符串
print(str2)         #输出字符串
print(var1)         #输出字符串
print(str[0:-1])    #输出第一个到 倒数第二个
print(str[-1])      #输出倒数第一个
print(str*2)        #输出字符串两次
print(str+'hello')  #连接字符串
print("输出测试-----------------------------------")
a='a'
b='b'
print(a)            #换行输出
print(b)
print(a,end='')     #不换行输出
print(b)
print("number数据类型测试-----------------------------------")
ZhengShu = 100          # 整型变量
FuDian   = 1000.0       # 浮点型变量
FuShu    = 3.14j        #复数类型   复数：z=a+bi
BuEr     = True         #布尔类型   flase 0 ；true 1
ZiFuChuan= "runoob"     # 字符串

print(ZhengShu)
print(FuDian)
print(FuShu+1)
print(BuEr)
print(ZiFuChuan)
print("list列表测试----Tuple元组与list列表用法一样，将[]换为()即可。不同处在元组不可改变，list列表可改变")
Liebiao = ['abcd','1234',',.?'];
list=['列表',123];
print(Liebiao)      #输出完整列表
print(Liebiao[0])   #输出列表第一个元素
print(Liebiao[-1])  #输出最后一个元素
print(Liebiao[1:])  #输出从第二个到最后
print(Liebiao*2)    #输出两份
print(Liebiao+list) #两个列表联合
print(Liebiao[0][0])#输出列表第一个元素的第一个字母
print(Liebiao[0::2])#输出从第一个到最后一个，步长为2输出
print("set集合测试-----------------------------------")
student={'小明','小刚','小强','小张','小强'}
print(student)#set不可重复，输出直接去除重复元素
if '小明'in student:
    print("小明在student中")
else:
    print("小明不在student中")
a=set('1234567890一二三四')
b=set('1234567890abcdefg')
print(a-b)  #差集
print(a|b)  #并集
print(a&b)  #交集
print(a^b)  #a,b中不同时存在
print("Dictionary字典测试-----------------------------------")
dict={} #空字典
dict['lyz']="刘言哲"
dict['yjj']='于佳佳'
dilts={'name':'值','age':18}
print(dict['lyz'])  #输出键为lyz的值
print(dict['yjj'])  #输出键为yjj的值
print(dilts.keys()) #输出字典中所有的键
print(dilts.values())   #输出字典中所4有的值
print (dilts)#输出完整的字典
print("运算符测试-----------------------------------")
a=2
b=5
print('a+b=',a+b)  #加法
print('a-b=',a-b)  #减法
print('a*b=',a*b)  #乘法
print('a/b=',a/b)  #除法
print('a%b=',a%b)  #取余
print('a**b=',a**b) #幂
print('a//b=',a//b) #取商的整数部分
print("逻辑运算符测试-----------------------------------")
a=10
if a<100 and a>0:
    print('100>a>0')
else:
    print('a>=100或者a<=0')
print("条件语句测试-----------------------------------")




