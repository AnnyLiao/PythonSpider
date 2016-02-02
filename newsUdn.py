import urllib.request
import urllib
import time
import datetime
from pyquery import PyQuery as pq
Time = time.time()
t = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d')
T = datetime.datetime.fromtimestamp(Time).strftime("%H:%M:%S")

news = []
test=[]

f=open('tagsUdn.txt', 'w', newline='')
file=open('viewsUdn.txt', 'w', newline='')
for n in range(1,3):
	q = pq(url="http://udn.com/news/breaknews/1/1/"+str(n)+".html")
	p = q("div#breaknews_body")
	links= []
	Date = []
	data=[]
	hour = []
	hot = []
	link = p('dl dt a')
	time = p('div.info div.dt')
	time = time.text()
	date = time.split(' ')
	num = p('div.view')
	num = num.text()
	view = num.split(' ')
	for x in link:
		links.append(x.attrib['href'])
		
	for x in date:
		if x == t:
			Date.append(x)
			
	for x in range(0,len(Date)):
		data.append(links[x])
	
	for x in range(1,len(date),2):
		h = date[x]
		hour.append(h[0:2])
	
	for x in range(0,len(view)):
		hot.append(int(view[x]) / (24 - int(hour[x])))
		
	for a in data:
		f.write(a+'\n')
		
	for a in hot:
		file.write(str(a)+'\n')

	print(len(data))

