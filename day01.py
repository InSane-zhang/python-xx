import urllib.request

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}

request = urllib.request.Request("http://www.baidu.com/",headers = headers)

response = urllib.request.urlopen(request)

print (response.read().decode('utf-8'))

print (response.getcode())

print(response.info())