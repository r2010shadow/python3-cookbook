#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 返回多个值的函数
Desc : 
"""

#7.4 返回多个值的函数
def myfun():
    return 1,2,3
a,b,c = myfun()
print(a,'', b,'',c)  #尽管 myfun() 看上去返回了多个值，实际上是先创建了一个元组然后返回的

a = (1,2)
b = 1,2
print(a, '',b)  #实际上我们使用的是逗号来生成一个元组，而不是用括号

x = myfun()
print(x)   #这个变量值就是函数返回的那个元组本身
