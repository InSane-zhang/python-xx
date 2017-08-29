# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:04:14 2017

@author: pc
"""
import json
import urllib.request
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/2/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

request = urllib.request.Request(url,headers = headers)
html = urllib.request.urlopen(request).read()

text = etree.HTML(html)

node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')

items = {}
for node in node_list:
    #xpath 返回的是列表，所有用索引方法取出
    username = node.xpath('./div/a/@title')[0]
    
    image = node.xpath('.//div[@class="thumb"]/@src')
    
    content = node.xpath('.//div[@class="content"]/span')[0].text
    #text 取出段子的内容
    zan = node.xpath('.//i')[0].text
    
    comments = node.xpath('.//i')[1].text
    
    items = {
            "username":username,
            "image":image,
            "content":content,
            "zan":zan,
            "comments":comments                     
            }
    
    with open ("qiushi.json","a") as f:
        f.write(json.dumps(items,ensure_ascii = False) +"\n")