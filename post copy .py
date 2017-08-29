# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:32:02 2017

@author: pc
"""

import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
data = {}
# data['i'] = 'I love FishC.com'
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] ='dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1493538230701'
data['sign'] = '7b50be5ddda95bce3d4b7b9404647cec'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CTRL_ENTER'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

print(html)

"""
target = json.loads(html)
print("翻译结果：%s"%(target['translateResult'][0][0]['tgt']))
"""