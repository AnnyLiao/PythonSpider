import urllib.request
from html.parser import HTMLParser
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime(' %Y/%m/%d')
f=open('tagsChina.txt', 'w', newline='')
for n in range(1,5):
	data = urllib.request.urlopen("http://www.chinatimes.com/realtimenews/260407?page="+str(n))
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
	
			if self.stack[-5:] == ["div","ul",'li','h2','a'] :
				self.links.append(dict(attrs)['href'])

		def handle_data(self, data):
			if self.stack[-5:] == ["div","ul",'li','div','time']:
				self.day.append(data)
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
		if Parser.day[d] == t:
			data.append(Parser.links[d])

	for a in range(0,len(data)):
		f.write(data[a]+'\n')

