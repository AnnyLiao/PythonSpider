#encoding=utf-8
import urllib.request
from html.parser import HTMLParser
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
text_file = open("tagsCna.txt", "r",encoding='utf8')
lines = text_file.readlines()

try:
	for a in range(0,len(lines)):
		try:
			s = 'http://www.cna.com.tw'+lines[a]
			data = urllib.request.urlopen('http://www.cna.com.tw'+lines[a])
			content = data.read().decode('utf_8')
			data.close()

			class myparser(HTMLParser):
				def __init__(self):
					HTMLParser.__init__(self)
					self.part = 0
					self.title = []
					self.cont=[]
					self.stack = []
				def handle_data(self, data):
	
					if self.stack[-3:] == ["div","section","p"]:
						self.cont.append(data)
		
					if self.stack[-2:] == ["div","h1"]:
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

			f=open('cnanews/'+t+'-0'+str(a)+'.txt', 'w', newline='')
			for x in Parser.title:
				f.write(x+'\n')
			for i in Parser.cont:
				f.write(i)
			f.write('\n'+s)
		except:
			print('編碼有問題')
		
except:
		#pass
	
	print('')

print(len(lines))
'''for x in range(0,5):
	if x==0:
		print(Parser.detailed[x]+Parser.title[x])
	else:
		print(Parser.detailed[x]+Parser.C_D[x-1])
		
Parser.cont.remove('總評分:')
print('\n劇情介紹：')'''