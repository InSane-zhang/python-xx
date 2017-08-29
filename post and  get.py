# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 22:43:45 2017

@author: pc
"""

import urllib.parse
import urllib.request
headers = {


"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Accept":"application/json, text/javascript, */*; q=0.01",
"X-Requested-With":"XMLHttpRequest",
"Accept-Language":"zh-CN,zh;q=0.8",

}
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'

key = input("shuru:")
formdata = {
        "type" : "AUTO",
        "i" : key,
        "doctype" : "json",
        "xmlVersion" : "1.8",
        "keyfrom" : "fanyi.web",
        "ue" : "UTF-8",
        "action" : "FY_BY_CLICKBUTTON",
        "typoResult" : "true"
    }
        
#可能出现要求是字节码的问题 加上.encode（codiing = 'utf-8'）没问题     
data = urllib.parse.urlencode(formdata).encode(encoding='UTF-8')

request = urllib.request.Request(url,data = data,headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))




