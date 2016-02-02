import mysql.connector
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
key = []
keyword = []
dic1 = {}
dic2 = {}
dic3 = {}
link = []
user = 'root'
pwd  = 'cycuim1016'
host = '127.0.0.1'
db   = 'test'

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()
now = str(t)

cursor.execute("SELECT `CATEGORY` FROM `keywords` WHERE `DATE`= '%s'  ORDER BY `COUNT` DESC LIMIT %d" % (now,3))


for r in cursor:
    key.append(''.join(r))
    
k1 = key[0]
k2 = key[1]
k3 = key[2]
print(key)


#----Udn News----
dic1 = {}
dic2 = {}
dic3 = {}
text_file = open("tagsUdn.txt", "r",encoding='utf8')
lines = text_file.readlines()
for i in range(0,len(lines)):
	content = open('Udnnews/'+t+'-0'+str(i)+'.txt', 'r').readlines()
	if len(content) == 5:
		keyword = content[4].split(',')

		for k in keyword:

			if k == k1:
				num = float(content[3])
				dic1.update({num:content[2]})	

			if k == k2:
				num = float(content[3])
				dic2.update({num:content[2]})

			if k == k3:
				num = float(content[3])
				dic3.update({num:content[2]})

def UdnLink(dic,k,d):
	temp = []
	link = []
	for key in sorted(dic.keys(),reverse = True):
		temp.append(dic[key])
	
	if len(temp) < 2:
		for x in range(0,len(temp)):
			Link = temp[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('聯合新聞網', k, Link, d)
			cursor.execute(add_keyword, data_keyword)
	else:
	
		for t in range(0,2):
			link.append(temp[t])
		for l in link:
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('聯合新聞網', k, l, d)
			cursor.execute(add_keyword, data_keyword)

		cnx.commit()
	
UdnLink(dic1,k1,t)
UdnLink(dic2,k2,t)
UdnLink(dic3,k3,t)
print('Udnok')		

#----China News----
dic1 = {}
dic2 = {}
dic3 = {}
text_file = open("tagsChina.txt", "r",encoding='utf8')
lines = text_file.readlines()
for i in range(0,len(lines)):
	try:
		content = open('chinanews/'+t+'-0'+str(i)+'.txt', 'r').readlines()
		if len(content) == 5:
			count = 0
			keyword = content[4].split(',')
			for k in keyword:
				if k == k1:
					num = float(content[3])
					dic1.update({num:content[2]})
					
				if k == k2:
					num2 = float(content[3])
					dic2.update({num2:content[2]})

				if k == k3:
					num3 = float(content[3])
					dic3.update({num3:content[2]})			
	except:
		print('lost')
		
		
def ChinaLink(dic,k,d):
	temp = []
	link = []
	for key in sorted(dic.keys(),reverse = True):
		temp.append(dic[key])
	
	if len(temp) < 2:
		for x in range(0,len(temp)):
			Link = temp[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('中時電子報', k, Link, d)
			cursor.execute(add_keyword, data_keyword)
	else:
	
		for t in range(0,2):
			link.append(temp[t])
		for l in link:
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('中時電子報', k, l, d)
			cursor.execute(add_keyword, data_keyword)

		cnx.commit()

ChinaLink(dic1,k1,t)
ChinaLink(dic2,k2,t)
ChinaLink(dic3,k3,t)
print('Chinaok')


#----Ltn News----
L1 = []
L2 = []
L3 = []
text_file = open("tagsLtn.txt", "r",encoding='utf8')
lines = text_file.readlines()
for i in range(0,len(lines)):
	try:
		content = open('ltnnews/'+t+'-0'+str(i)+'.txt', 'r').readlines()
		if len(content) == 3:
			keyword = content[2].split(',')

			for k in keyword:
				if k == k1:
					if content[1] not in L1:
						L1.append(content[1])
				if k == k2:
					if content[1] not in L2:
						L2.append(content[1])
				if k == k3:
					if content[1] not in L3:
						L3.append(content[1])
					
	except:
		pass
def LLink(L,k,d):
	if len(L) < 2:
		for x in range(0,len(L)):
			Link = L[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('自由時報', k, Link, d)
			cursor.execute(add_keyword, data_keyword)
	else:
		for x in range(0,2):
			Link = L[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('自由時報', k, Link, d)
			cursor.execute(add_keyword, data_keyword)

		cnx.commit()

LLink(L1,k1,t)
LLink(L2,k2,t)
LLink(L3,k3,t)
print('Lok')


#---Etoday News---
text_file = open("tagsE.txt", "r",encoding='utf8')
lines = text_file.readlines()
keyword = []
L1 = []
L2 = []
L3 = []
for e in range(0,len(lines)):
	try:
		content3 = open('Enews/'+t+'-0'+str(e)+'.txt','r').readlines()
		if len(content3) > 0:
		
			keyword = content3[len(content3)-1].split(',')
			for k in keyword:

				if k == k1:
					L1.append(content3[len(content3)-2])
				if k == k2:
					L2.append(content3[len(content3)-2])
				if k == k3:
					L3.append(content3[len(content3)-2])
	except:
		pass
	
def ELink(L,k,d):
	if len(L) < 2:
		for x in range(0,len(L)):
			Link = L[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('東森新聞雲', k, Link, d)
			cursor.execute(add_keyword, data_keyword)
	else:
		for x in range(0,2):
			Link = L[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('東森新聞雲', k, Link, d)
			cursor.execute(add_keyword, data_keyword)

		cnx.commit()

ELink(L1,k1,t)
ELink(L2,k2,t)
ELink(L3,k3,t)
print('Eok')




#---Apple---
text_file = open("tagApl/tagsApl"+t+".txt", "r",encoding='utf8')
num_file = open("numsApl/numApl"+t+".txt", "r",encoding='utf8')
lines = text_file.readlines()
num = num_file.readlines()
keyword = []
dic1 = {}
dic2 = {}
dic3 = {}
for e in range(0,len(lines)):
	content3 = open('Aplnews/'+t+'-0'+str(e)+'.txt','r').readlines()
	if len(content3) > 2:
		keyword = content3[len(content3)-1].split(',')
		
		for k in keyword:
			if k == k1:
				n = num[e]
				dic1.update({float(n):'http://www.appledaily.com.tw'+lines[e]})	
			if k == k2:
				n = num[e]
				dic2.update({float(n):'http://www.appledaily.com.tw'+lines[e]})	
			if k == k3:
				n = num[e]
				dic3.update({float(n):'http://www.appledaily.com.tw'+lines[e]})	
def AplLink(dic,k,d):
	temp = []
	link = []
	
	for key in sorted(dic.keys(),reverse = True):
		temp.append(dic[key])
	
	if len(temp) < 2:
		for x in range(0,len(temp)):
			Link = temp[x]
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('蘋果日報', k, Link, d)
			cursor.execute(add_keyword, data_keyword)
	else:
		for t in range(0,2):
			link.append(temp[t])
			
		for l in link:
			add_keyword = ("INSERT INTO weblink "
					"(Web, Keyword, Links, Date) "
					"VALUES (%s, %s, %s, %s)")
			data_keyword = ('蘋果日報', k, l, d)
			cursor.execute(add_keyword, data_keyword)

		cnx.commit()

AplLink(dic1,k1,t)
AplLink(dic2,k2,t)
AplLink(dic3,k3,t)
print('Aplok')
cursor.close()
cnx.close()