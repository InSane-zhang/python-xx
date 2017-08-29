# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 01:09:03 2017

@author: pc
"""

import urllib
import urllib.request
from lxml import etree

def loadPage(url):
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(url,headers = headers)
    html = urllib.request.urlopen(request).read()
    content= etree.HTML(html)
    link_list = content.xpath('//div[@class = "threadlist_title pull_left j_th_tit "]/a[@class = "j_th_tit "]/a/@href')
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        loadImage(fulllink)

def loadImage(link):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(link,headers = headers)
    html = urllib.request.urlopen(request).read()
    content = etree.HTML(html)
    link_list = content.xpath('//image[@class = "BDE_Image"]/@src')
    for link in link_list:
        writePage(link)
        
def writePage(link,filename):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(link,headers = headers)
    image = urllib.request.Request(request).read()
    with open (filename,"wb") as f:
        f.write(image)
        filename = link[-10: ]
    
    
    
        
    

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage + 1):
        pn = (page - 1) * 50
        
        fullurl = url + "&&pn=" + str(pn)
        loadPage(fullurl)
    
if __name__ =="__main__":
    
    url = "http://tieba.baidu.com/f?"
    kw = input("请输入贴吧名：")
    beginPage = int(input("起始页"))
    endPage = int(input("截止页"))
    kw = {"kw",kw}
    key = urllib.parse.urlencode(kw).encode('utf-8')
    
    fullurl = url + key
    
    tiebaSpider(fullurl,beginPage,endPage)