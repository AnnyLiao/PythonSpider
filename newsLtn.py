import urllib.request
from html.parser import HTMLParser

import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
f=open('tagsLtn.txt', 'w', newline='')
count = 0
news = []
for n in range(1,6):
	data = urllib.request.urlopen("http://news.ltn.com.tw/list/politics?page="+str(n))
	content = data.read().decode('utf_8')
	data.close()
	class linkParser(HTMLParser):
		def __init__(self):
			HTMLParser.__init__(self)
			self.links = []
			self.isNumber = 0
			self.stack = []
			self.day = []
			

		
		def handle_starttag(self, tag, attrs):
			self.stack.append(tag)
			
			if self.stack[-4:] == ["div","ul",'li','a'] :
				self.links.append(dict(attrs)['href'])

		def handle_data(self, data):
			if self.stack[-3:] == ["ul","li","span"]:
				self.day.append(data[0:10])
			self.isNumber = 0



		def handle_endtag(self, tag):
			while self.stack:
				item = self.stack.pop()
				if item == tag:
					break
	
	Parser = linkParser()
	Parser.feed(content)
	data=[]
	
	for l in Parser.links:
		if l[6:14] == 'politics':
			news.append(l)
	
	
	for d in range(0,len(Parser.day)):
		if Parser.day[d] == t:
			data.append(news[d])
			
			

	for a in range(0,len(data)):
		f.write(data[a]+'\n')
		
	print(len(data))#總筆數
