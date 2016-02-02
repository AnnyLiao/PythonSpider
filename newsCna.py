import urllib.request
import urllib
from html.parser import HTMLParser
import time
import datetime
from pyquery import PyQuery as pq
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d')
news = []
test=[]

f=open('tagsCna.txt', 'w', newline='')
for n in range(1,4):
	q = pq(url="http://www.cna.com.tw/list/aipl-"+str(n)+".aspx")
	p = q("div.article_list")
	links= []
	link = p('li a')
	for x in link:
		links.append(x.attrib['href'])

	data = urllib.request.urlopen("http://www.cna.com.tw/list/aipl-"+str(n)+".aspx")
	content = data.read().decode('utf_8')
	data.close()
	class linkParser(HTMLParser):
		def __init__(self):
			HTMLParser.__init__(self)
			self.links = []
			self.isNumber = 0
			self.stack = []
			self.day = []
			self.test = []
		def handle_starttag(self, tag, attrs):
			self.stack.append(tag)
		
		def handle_data(self, data):
			if self.stack[-4:] == ["ul","li","a","span"]:
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
	
	for d in range(0,len(Parser.day)):
		if Parser.day[d] == t:
			data.append(links[d])

	for a in range(0,len(data)):
		f.write(data[a]+'\n')


	print(len(data))

