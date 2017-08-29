# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib
import urllib.request
from lxml import etree

def loadPage(fullurl,filename):
    print ("正在下载页面" + filename)
    headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(fullurl,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    #用xpath取出每页的链接
    link_list = content.xpath('//div[@class = "threadlist_title pull_left j_th_tit "]/a[@class = "j_th_tit "]/a/@href')
    for link in link_list:
        #组合为每个帖子的链接
        fulllink = "http://tieba.baidu.com/"  + link
        
        loadImage(fulllink)
def loadImage(fulllink):
    headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(fulllink,headers = headers)
    
    html = urllib.request.urlopen(request).read()
    content = etree.HTML(html)
    #用xpath取出每个图片的列表链接集合
    link_list = content.xpath('//image[@class = "BDE_Image"]/@src')
    for link in link_list:
        
        writeImage(link)
    
    
    
def writeImage(link):
    """
    作用：将html内容写入到本地
    link：图片链接
    """
    headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    request = urllib.request.Request(link,headers = headers)
    #从src取出文件数据
    image = urllib.request.urlopen(request).read()
    filename = link[-10: ]
    with open (filename,'wb') as f:
        f.write(image)
    print ("已成功下载" + filename)
    
def tiebaSpider(url,beginPage,endPage):
   
    for page in range(beginPage,endPage + 1):
        pn = (page - 1) * 50
        fullurl = url+ "&&pn=" + str(pn)
    
        loadPage(fullurl)

if __name__ =="__main__":
    
    kw = input("请输入贴吧名:")
    beginPage = int(input("请输入起始页:"))
    endPage = int(input("请输入截止页:"))
    url = "https://tieba.baidu.com/f?"
    kw = {"kw",key}
    
    key = urllib.parse.urlencode(kw).encode('utf-8')
    
    fullurl = url + key
    
    tiebaSpider(fullurl,beginPage,endPage)
    