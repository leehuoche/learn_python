#coding=utf-8
import urllib
import re

def get_html_file():
	page=urllib.urlopen("http://tieba.baidu.com/f?kw=%E9%A3%8E%E6%99%AF&fr=wwwt")
	html=page.read()
	return html
h=get_html_file()

def get_title(html):
	reg=r'主题作者.+"'
	Title=re.compile(reg)
	tlist=re.findall(Title,html)
	i=1
	for g in tlist:
		print i
		print g
		i+=1

get_title(h)