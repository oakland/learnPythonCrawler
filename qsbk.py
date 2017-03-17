# -*- coding: utf-8 -*-

# 1. 抓取页面
# 2. 匹配 patter，找到所有的 item
# 3. 打印所有的 item

import urllib2
import re

page = 1
url = "http://qiushibaike.com/hot/page/" + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = { "User-Agent" : user_agent }
pattern = re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	# print response.read()
	content = response.read().decode("utf-8")
	items = re.findall(pattern, content)
	for item in items:
		print item
except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason