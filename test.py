import urllib2
from bs4 import BeautifulSoup

page_num = 1
url = "https://mm.taobao.com/json/request_top_list.htm?page=1" + str(page_num)
request = urllib2.Request(url)
response = urllib2.urlopen(request)

# print response.read()
soup = BeautifulSoup(response.read(), 'lxml')
print soup.a