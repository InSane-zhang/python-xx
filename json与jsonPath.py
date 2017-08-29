# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:00:24 2017

@author: pc
"""
#json 的解析库
import json
import jsonpath

import urllib.request

url = "http://www.lagou.com/lbs/getALLCitySearchLabels.json"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

request = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(request)
#取出json文件里的内容，返回的格式为字符串
html = response.read().decode('utf-8')

#把json形式字符串转换为pyhon形式的unicode字符串
unicodestr = json.loads(html)

city_list = jsonpath.jsonpath(unicodestr,"$..name")

for item in city_list:
    print (item)
    

array = json.dumps(city_list,ensure_ascii = False)


with open ("lagou.json","w") as f:
    f.write(array.encode('utf-8'))
    
    