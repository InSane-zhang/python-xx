# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:49:59 2017

@author: pc
"""

import requests

from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

url = "http://www.sina.com/"

res = requests.get(url,headers = headers)

soup = BeautifulSoup(res.text,'html.parser')

print(soup.prettify())   
                                  
