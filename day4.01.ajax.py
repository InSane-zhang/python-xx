# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 20:49:59 2017

@author: pc
"""

"""
ajax 方式获取的数据一定是json数据。
拿到json 就是拿到网页的数据了
"""
import urllib
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

formdata = {
        
       
        
        "start":"10",
        "limit":"10"
        
        
        }

data = urllib.parse.urlencode(formdata).encode(encoding='UTF-8')

request = urllib.request.Request(url,data = data,headers = headers)

response = urllib.request.urlopen(request)

#.decode('utf-8')解决页面乱码没有汉字的问题
print(response.read().decode('utf-8'))