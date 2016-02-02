import urllib.request
from html.parser import HTMLParser
import time
import datetime
t = time.time()
t2 = time.time()

t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
t2 = datetime.datetime.fromtimestamp(t2).strftime('%Y/%m/%d')
f=open('tagsE.txt', 'w', newline='')
for n in range(1,3):
	
	data = urllib.request.urlopen("http://www.ettoday.net/news/news-list-"+t+"-1-"+str(n)+".htm")
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
		
			if self.stack[-3:] == ["div","h3",'a'] :
				self.links.append(dict(attrs)['href'])
			
		def handle_data(self, data):
			if self.stack[-4:] == ["div","div","h3",'span']:
				self.day.append('2016/'+data[1:6])
			self.isNumber = 0

		def handle_endtag(self, tag):
			while self.stack:
				item = self.stack.pop()
				if item == tag:
					break
	
	Parser = linkParser()
	Parser.feed(content)
	data=[]
	

	'''for i in range(0,len(Parser.links)):
		htl=Parser.links[i]
		if htl=='http://www.xinhua.org/':
			print(i)
		if htl=='http://www.nova.com.tw/magazine/':
			print(i)'''

	for d in range(0,len(Parser.day)):
		if Parser.day[d] == t2:
			
			data.append(Parser.links[d])

	for a in range(0,len(data)):

		f.write(data[a]+'\n')

	
	
