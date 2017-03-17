# -*- coding: utf-8 -*-


# --- POST ---
import urllib2

values = {"username":"jizq","password":"xxxxxx"}
data = urllib2.urlencode(values)
url = "http://www.baidu.com/login"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)

print response.read()


# --- GET ----

values = {"username":"jizq","password":"xxxxxx"}
data = urllib2.urlencode(values)
url = "http://www.baidu.com" + '?' + data
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()