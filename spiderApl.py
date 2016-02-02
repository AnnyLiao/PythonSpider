#encoding=utf-8
import urllib.request
import urllib
from html.parser import HTMLParser
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
text_file = open("tagApl/tagsApl"+t+".txt", "r", encoding='utf8')
lines = text_file.readlines()
print(len(lines))

for a in range(0,len(lines)):
	try:
		
		s = lines[a]
		s = s[30:]
		s=urllib.parse.quote(s)
		url = 'http://www.appledaily.com.tw/realtimenews/article/politics/%s'%(s)
		data = urllib.request.urlopen(url)
		content = data.read().decode('utf8')
		data.close()

		class myparser(HTMLParser):
			def __init__(self):
				HTMLParser.__init__(self)
				self.part = 0
				self.title = []
				self.cont=[]
				self.stack = []
			def handle_data(self, data):
	
				if self.stack[-2:] == ["div","p"]:
					self.cont.append(data)
		
				if self.stack[-3:] == ["header","hgroup","h1"]:
					self.title.append(data)
				self.part = 0
	
			def handle_starttag(self, tag, attrs):
	
				self.stack.append(tag)	
		
			def handle_endtag(self, tag):
				while self.stack:
					item = self.stack.pop()
					if item == tag:
						break
            

		Parser = myparser()
		Parser.feed(content)

		f=open('Aplnews/'+t+'-0'+str(a)+'.txt', 'w', newline='')
		for x in Parser.title:
			f.write(x+'\n')
		for i in Parser.cont:
			f.write(i)
		



	except:
		print('編碼')

			
	
	
		

		
