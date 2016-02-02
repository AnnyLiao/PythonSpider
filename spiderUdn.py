#encoding=utf-8
import urllib.request
import urllib
import time
import datetime
from pyquery import PyQuery as pq
from html.parser import HTMLParser
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
text_file = open("tagsUdn.txt", "r",encoding='utf8')
view_file = open("viewsUdn.txt", "r",encoding='utf8')
lines = text_file.readlines()
views = view_file.readlines()


for a in range(0,len(lines)):
	try:
	
		s = 'http://udn.com'+lines[a]
		data = urllib.request.urlopen('http://udn.com'+lines[a])
		content = data.read().decode('utf_8')
		data.close()
		q = pq(content)
		content = q("div#story_body_content p")
		title = q("div#story_body_content h2")
		content = content.text()
		title = title.text()
		f=open('udnnews/'+t+'-0'+str(a)+'.txt', 'w')
	
		f.write(title+'\n')
		f.write(content)
		f.write('\n'+s)
		f.write(views[a])
	except:
		print(a)
	


#print(len(lines))
