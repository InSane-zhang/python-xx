# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:16:37 2017

@author: pc
"""

import urllib 
import urllib.request

url = "http://www.baidu.com/s"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

keyword = input("请输入需要查询的关键字： ")

wd = {"wd":keyword}

wd = urllib.parse.urlencode(wd)

fullurl = url + "?" + wd

request = urllib.request.Request(fullurl,headers = headers)

response = urllib.request.urlopen(request)

print (fullurl)
print (response.read().decode('utf-8'))