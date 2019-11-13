'''
#Python3中有可变对象和不可变对象.

直接上定义：
可变对象：当有需要改变对象内部的值的时候，这个对象的id不发生变化。

不可变对象：当有需要改变对象内部的值的时候，这个对象的id会发生变化。

可变对象
可变对象包括：字典(dict), 集合(set), 列表(list). 此可变对象会与浅拷贝和深拷贝有很大的联系， 后续会继续更新。

不可变对象
不可变对象包含 整型(int), 字符串(string), 浮点型(float), 元组(tuple)

五个场景看清不可变对象在python中的端倪：

场景1: int值比较小时，值一样的变量id就一样，值变化id就变化。
'''

#可变对象
#------------------------------------

#dict
# print('--------------test for dict --------------')
# dic = {'a': 1, 'b': 2, 'c': 3}
# dik = {'a': 1, 'b': 2, 'c': 3}
# print(id(dic))
# print(id(dik))
# dic['c'] = 5
# print(id(dic))
# dic = {'a': 1, 'b': 2, 'c': 3}
# print(id(dic))
#
# #list
# print('--------------test for list --------------')
# ml = [1,2,3]
# ms = [1,2,3]
# print(id(ml))
# print(id(ms))
# ml[0] = 5
# print(id(ml))
# ml = [1,2,3]
# print(id(ml))
#
# #set
# print('--------------test for set --------------')
# ms = {1, 2, 3, 4}
# print(id(ms))
# ms.add(5)
# print(id(ms))
# ms = {1, 2, 3, 4, 5}
# print(id(ms))

#不可变对象
#int
print('--------------test for int --------------')
#int值比较小时， 值一样id就一样
a = 5
c = a
print(id(a))
print(id(c))
a = 3
print(id(a))
b = 3
print(id(b))
#int值比较大时， 值一样id也不一样
a = 5000000**3
print(id(a))
a = 3000000**3
print(id(a))
b = 5000000**3
print(id(b))

#float
print('--------------test for float --------------')
a = 5.757687786761267656785767845757687786761267656785767845
print(id(a))
a = 3.216870878645678641565167866757687786761267656785767845
print(id(a))
b = 5.757687786761267656785767845757687786761267656785767845
print(id(b))

#string
print('--------------test for float --------------')
s = 'fuc'
print(id(s))
s += 'k'
b = 'fuck'
print(id(s))
print(id(b))
c = 'fuck'
print(id(c))

s = 'fuck me hard'
b = 'fuck me hard'
print(id(s))
print(id(b))
s += ' please'
print(id(s))

#tuple
print('--------------test for tuple --------------')
t = (1, 2, 3)
q = (1, 2, 3)
print(id(t))
print(id(q))
