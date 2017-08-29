# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:09:25 2017

@author: pc
"""


import urllib.request

url = "http://www.renren.com/347914813/profile"

headers = {
  
    "Host":"www.renren.com",
    "Proxy-Connection":"keep-alive",
    "Cache-Control":"max-age=0",
    #"Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"anonymid=j5gsyymghb4wlz; depovince=GW; _r01_=1; ick_login=2fe13ce9-f34d-4fb1-b187-8334ed8bcd36; JSESSIONID=abc78NGvjGnLX7BXYYV1v; t=53a19e211c4653f4bc5294a75c5aa7fc7; societyguester=53a19e211c4653f4bc5294a75c5aa7fc7; id=948732617; xnsid=90339340; jebecookies=91711c1c-93b4-4b90-b43f-9172f63cfea4|||||; ch_id=10016; wp_fold=0",
    "DNT":"1",

        
        }

request = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))