import mysql.connector
import time
import datetime
from pyquery import PyQuery as pq
import jieba
import jieba.analyse

Time = time.time()
t = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d')


user = 'root'
pwd  = 'cycuim1016'
host = '127.0.0.1'
db   = 'test'



cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()
now = str(t)

cursor.execute("SELECT `id` FROM `weblink` WHERE `Date`= '%s' LIMIT %d" % (now,1))

for n in cursor:
	firstid = n[0]




#--Udn reply
def Udn(r, p, n, l):
	countP = 0
	countN = 0
	q = pq(r)
	fb = q("span._5mdd").text()
	U = q("dl.disl dt span").text()
	rt = q('h2#story_art_title').text()

	replay = fb.split()
	Ur = U.split()
	wordlist = []
	for x in replay:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)
	for x in Ur:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)

	for x in wordlist:
		try:
			if p.index(x):
				
				countP += 1
		except:
			pass

	for x in wordlist:
		try:
			if n.index(x):
				
				countN += 1
		except:
			pass

	
	positive = int((countP/(countP+countN))*100)
	negtive = int((countN/(countP+countN))*100)
	summary = str(positive)+';'+str(negtive)
	ID = str(l)

	query = "UPDATE weblink SET Title = %s, PN_Comment = %s WHERE id = %s "
	data = (rt, summary, ID)
	cursor.execute(query, data)
	cnx.commit()


#--China reply
def China(r, p, n, l):
	countP = 0
	countN = 0
	q = pq(r)
	fb = q("div.post-message p").text()
	rt = q('header h1').text()
	replay = fb.split()
	wordlist = []
	for x in replay:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)

	for x in wordlist:
		try:
			if p.index(x):
				
				countP += 1
		except:
			pass

	for x in wordlist:
		try:
			if n.index(x):
				
				countN += 1
		except:
			pass
	positive = int((countP/(countP+countN))*100)
	negtive = int((countN/(countP+countN))*100)
	summary = str(positive)+';'+str(negtive)
	ID = str(l)

	query = "UPDATE weblink SET Title = %s, PN_Comment = %s WHERE id = %s "
	data = (rt, summary, ID)
	cursor.execute(query, data)
	cnx.commit()


#--Ltn reply
def Ltn(r, p, n, l):
	countP = 0
	countN = 0
	q = pq(r)
	fb = q("span._5mdd").text()
	rt = q("h1").text()
	replay = fb.split()
	wordlist = []
	for x in replay:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)

	for x in wordlist:
		try:
			if p.index(x):
				
				countP += 1
		except:
			pass

	for x in wordlist:
		try:
			if n.index(x):
				
				countN += 1
		except:
			pass
	positive = int((countP/(countP+countN))*100)
	negtive = int((countN/(countP+countN))*100)
	summary = str(positive)+';'+str(negtive)
	ID = str(l)

	query = "UPDATE weblink SET Title = %s, PN_Comment = %s WHERE id = %s "
	data = (rt, summary, ID)
	cursor.execute(query, data)
	cnx.commit()


#--Etoday reply
def Etoday(r, p, n, l):
	countP = 0
	countN = 0
	q = pq(r)
	fb = q("span._5mdd").text()
	rt = q("h2").text()
	replay = fb.split()
	wordlist = []
	for x in replay:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)

	for x in wordlist:
		try:
			if p.index(x):
				
				countP += 1
		except:
			pass

	for x in wordlist:
		try:
			if n.index(x):
				
				countN += 1
		except:
			pass
	positive = int((countP/(countP+countN))*100)
	negtive = int((countN/(countP+countN))*100)
	summary = str(positive)+';'+str(negtive)
	ID = str(l)

	query = "UPDATE weblink SET Title = %s, PN_Comment = %s WHERE id = %s "
	data = (rt, summary, ID)
	cursor.execute(query, data)
	cnx.commit()


#--Apple reply
def Apl(r, p, n, l):
	countP = 0
	countN = 0
	q = pq(r)
	fb = q("span._5mdd").text()
	rt = q("h1#h1").text()
	replay = fb.split()
	wordlist = []
	for x in replay:
		words = jieba.cut(x, cut_all=False)
		for y in words:
			wordlist.append(y)

	for x in wordlist:
		try:
			if p.index(x):
				
				countP += 1
		except:
			pass

	for x in wordlist:
		try:
			if n.index(x):
				
				countN += 1
		except:
			pass
	positive = int((countP/(countP+countN))*100)
	negtive = int((countN/(countP+countN))*100)
	summary = str(positive)+';'+str(negtive)
	ID = str(l)

	query = "UPDATE weblink SET Title = %s, PN_Comment = %s WHERE id = %s "
	data = (rt, summary, ID)
	cursor.execute(query, data)
	cnx.commit()


#-----------------------------------------------------------------------------
poslist = []
neglist = []
pos = open("sentiment_dictionary/posdict-2.txt", "r",encoding='utf8')
neg = open("sentiment_dictionary/negdict-2.txt", "r",encoding='utf8')
posdict = pos.readlines()
negdict = neg.readlines()
for x in posdict:
	poslist.append(x[:len(x)-1])

for x in negdict:
	neglist.append(x[:len(x)-1])


#text_file = open("Url/"+t+"_Url.txt", "r",encoding='utf8')
text_file = open("Url/"+t+'_Url.txt', "r",encoding='utf8')
lines = text_file.readlines()


for l in range(len(lines)):
	try:
		reply_file = open('reply/' + t + '_' + str(l) + '.txt', 'r', encoding = 'utf8')
		r = reply_file.read()
	
		if '*UDN*' in r :
			print(l)
			Udn(r, poslist, neglist,(l+int(firstid)))
			

		if 'post-list' in r:
			print(l)
			China(r, poslist, neglist,(l+int(firstid)))

		if '*LTN*' in r:
			print(l)
			Ltn(r, poslist, neglist,(l+int(firstid)))

		if 'etoday' in r:
			print(l)
			Etoday(r, poslist, neglist,(l+int(firstid)))

		if '*APL*' in r:
			print(l)
			Apl(r, poslist, neglist,(l+int(firstid)))
	except:
		pass

jieba.set_dictionary('dict.txt.big')
jieba.analyse.set_stop_words("stop_words.txt")

