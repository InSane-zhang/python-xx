# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:35:15 2017

@author: pc
"""

import urllib.request

#创建一个httpHandler处理器对象，支持处理http的请求

#在HTTPHandler增加参数“debuglevel = 1”将会自动打开debug log 模式
#程序在执行的时候回打印收发包的信息
http_handler = urllib.request.HTTPHandler(debuglevel = 1)

#调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象。
opener = urllib.request.build_opener(http_handler)

request = urllib.request.Request("http://www.baidu.com/")

#不采用URLopen（request）方式进行打开
#原先 response = urllib.request.urlopen(request)
response =opener.open(request)

#print (response.read().decode('utf-8'))


