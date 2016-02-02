# coding=utf-8
import urllib.request
from html.parser import HTMLParser
from pyquery import PyQuery as pq
import time
import datetime
Time = time.time()
t = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d')
T = datetime.datetime.fromtimestamp(Time).strftime("%H:%M:%S")
f=open('tagApl/tagsApl'+t+'.txt', 'w', encoding = 'utf_8')
count = 0
news = []
for n in range(1,2):
	data = urllib.request.urlopen("http://www.appledaily.com.tw/realtimenews/section/politics/"+str(n))
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

		'''def handle_data(self, data):
			if self.stack[-3:] == ["ul","li","span"]:
				self.day.append(data[0:10])
			self.isNumber = 0'''



		def handle_endtag(self, tag):
			while self.stack:
				item = self.stack.pop()
				if item == tag:
					break
	
	Parser = linkParser()
	Parser.feed(content)
	data=[]
	new = []
	for l in Parser.links:
		if l[14:30] == 'article/politics':
			data.append(l)
	

	for a in data:
		
		f.write(a+'\n')
		
	print(len(data))#總筆數
	
	q = pq(url="http://www.appledaily.com.tw/realtimenews/section/politics/"+str(n)+".aspx")
	period = q("li.rtddt time")
	p = q("li.rtddt h1 font")
	a = p.text()
	period = period.text()
	num = []
	num1 = []
	hot = []
	h = []
	new = a.split(' ')
	time = period.split(' ')
	
	for x in time:
		h.append(int(x[0:2]))

	for x in new:
		if '(' in x:
			s = x.find('(') + 1
			num.append(x[s:len(x)-1])

	for x in num:
		if x.isnumeric():
			num1.append(x)
			
	for x in range(0,len(num1)):
		hot.append(int(num1[x]) / (24 - h[x]))
		
	print(hot)
	f=open('numsApl/numApl'+t+'.txt', 'w', encoding = 'utf_8')
	for x in hot:
		f.write(str(x)+'\n')
	print(len(hot))
