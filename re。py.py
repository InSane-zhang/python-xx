https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=






"type":"11"
"interval_id":"100:90"
""action"":"",
"start":"0"
"limit":"1"





"Host":"zhibo.renren.com",
"Proxy-Connection":"keep-alive",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cookie":"anonymid=j5gsyymghb4wlz; depovince=GW; _r01_=1; ick_login=2fe13ce9-f34d-4fb1-b187-8334ed8bcd36; JSESSIONID=abc78NGvjGnLX7BXYYV1v; t=53a19e211c4653f4bc5294a75c5aa7fc7; societyguester=53a19e211c4653f4bc5294a75c5aa7fc7; id=948732617; xnsid=90339340; jebecookies=91711c1c-93b4-4b90-b43f-9172f63cfea4|||||; ch_id=10016; wp_fold=0",
"DNT":"1",





python 中re模块有两种方式：

pattern = re.compile("\d")


pattern.match("需要匹配的内容") 从起始位置开始往后查找，返回第一个符合规则的 只匹配一次
pattern.search() 从任意位置开始往后查找，返回第一个符合规则的 只匹配一次
pattern.findall() 所有的全部匹配，返回列表
pattern.finditer() 
pattern.spilt() 分割字符串，返回列表
pattern.sub() 替换



match(str,begin,end)
search(str,begin,end)
findall(str,begin,end)
spilt(str,count)




re.I 表示胡聂大小写

re.S 全文匹配