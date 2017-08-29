# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:34:30 2017

@author: pc
"""

import urllib.request

import ssl
#忽略ssl安全认证
context = ssl._create_unverified_context()

url = "https://www.12306.cn/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

request = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(request,context = context)

print (response.read().decode('utf-8'))