#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 可接受任意数量参数的函数
Desc : 
"""

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
print(avg(1,2),   avg(1,2,3,4))

import html      # html格式生成函数
def make_element(name, value, **attrs):  #attrs 是一个包含所有被传入进来的关键字参数的字典
    keyvals = [' %s="%s"' % item for item in attrs.items()] 
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element
make_element('item', 'Albatross', size= 'large', quantity = 6)
                            #  size= 'large', quantity = 6 传入的内容原样显示 
                            
                            
def anyargs(*args, **kwargs):  #能同时接受任意数量的位置参数和关键字参数，可以同时 使用 * 和 **
    print(args) # A tuple 
    print(kwargs) # A dict
anyargs('args: 位置参数',99,22,100, ['99','22','100'],kwargs='关键字参数',name='zoo',eye='dark') 

def a(x, *args, y):
    print(x,args,y)
a(0,2,4,8,y=10)

def b(x, *args, y, **kwargs):
    print(x, args, y, kwargs)
b(0,2,4,8,y=10,kwargs='关键字参数')
