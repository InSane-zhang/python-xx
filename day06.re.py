# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:46:49 2017

@author: pc
"""

#非结构化数据和结构化数据

import re
"""
pattern = re.compile(r"\d+")

m = pattern.match("aaa123bbb345",3,5)

print (m.group())# m.group 为取值
# end为最后的数字也不能改变结果。


pattern = re.compile(r"([a-z]+) ([a-z]+)"，re.I)

m = pattern.match("hello world hello python ")

print (m.group(0))#表示所有字符串匹配

print (m.group(1))#表示取第一个字符串


m.span()#取字符的list下标


pattern = re.compile(r"\d+")

m = pattern.search(r"aaabbb123456",2,5)

print (m.group())

pattern = re.compile(r"\d?")

m = pattern.findall("hello 123456 789",1,10)

print (m)

"""
pattern = re.compile(r"(\w+) (\w+)")

str  = "hello 123 , hello 456"


m = pattern.sub("hello world",str)

print(m)

m2 = pattern.sub(r"\1,\2",str)
print (m2)

m3 = pattern.sub(r"\2,\1",str)
print (m3)
