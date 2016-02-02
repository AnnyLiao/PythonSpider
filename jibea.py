#encoding=utf-8
import jieba
import jieba.analyse
import csv
from gensim import corpora, models, similarities
import numpy as np
import pickle,re,sys,os,re,time
from datetime import date, datetime, timedelta
import mysql.connector
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')

jieba.set_dictionary('dict.txt.big')
jieba.analyse.set_stop_words("stop_words.txt")
t3=[]
t4=[]
t5=[]
t6=[]
t7=[]
t8=[]
t9=[]

#----Udn News----
text_file = open("tagsUdn.txt", "r",encoding='utf8')
lines = text_file.readlines()
for i in range(0,len(lines)):
	content = open('udnnews/'+t+'-0'+str(i)+'.txt', 'r').readlines()
	if len(content) == 4:

		tags = jieba.analyse.extract_tags(content[1], topK=3)#取得關鍵字語法

		for word in tags:
			t3.append(word)

		f = open('udnnews/'+t+'-0'+str(i)+'.txt', 'a')
		key = ','.join(tags)
		f.write(key)
		f.close()
	
		
#----China News----
text_file = open("tagsChina.txt", "r",encoding='utf8')
lines = text_file.readlines()
for c in range(0,len(lines)):
	try:
		content2 = open('chinanews/'+t+'-0'+str(c)+'.txt','r').readlines()

		if len(content2) == 4:
		
			tags2 = jieba.analyse.extract_tags(content2[1], topK=3)#取得關鍵字語法

			for word in tags2:
				t6.append(word)

			f = open('chinanews/'+t+'-0'+str(c)+'.txt', 'a')
			key = ','.join(tags2)
			f.write('\n'+key)
			f.close()
	except:
		print('')

		

#---Etoday News----
text_file = open("tagsE.txt", "r",encoding='utf8')
lines = text_file.readlines()
for e in range(0,len(lines)):
	try:
		content3 = open('Enews/'+t+'-0'+str(e)+'.txt','r').read()
	
		tags3 = jieba.analyse.extract_tags(content3, topK=3)#取得關鍵字語法

		for word in tags3:
			t7.append(word)

		f = open('Enews/'+t+'-0'+str(e)+'.txt', 'a')
		key = ','.join(tags3)
		f.write(key)
		f.close()
	except:
		pass
	


#---Ltn News----
text_file = open("tagsLtn.txt", "r",encoding='utf8')
lines = text_file.readlines()
for l in range(0,len(lines)):
	try:
		content3 = open('ltnnews/'+t+'-0'+str(l)+'.txt','r').readlines()
	
		if len(content3) == 2:

			tags3 = jieba.analyse.extract_tags(content3[0], topK=3)#取得關鍵字語法

			for word in tags3:
				t8.append(word)

			f = open('ltnnews/'+t+'-0'+str(l)+'.txt', 'a')
			key = ','.join(tags3)
			f.write(key)
			f.close()
	except:
		print('')

		


#---Apple News----
text_file = open("tagApl/tagsApl"+t+".txt", "r",encoding='utf8')
lines = text_file.readlines()
for a in range(0,len(lines)):
	content3 = open('Aplnews/'+t+'-0'+str(a)+'.txt','r').read()
	

	tags3 = jieba.analyse.extract_tags(content3, topK=3)#取得關鍵字語法


	for word in tags3:
			
		t9.append(word)

	f = open('Aplnews/'+t+'-0'+str(a)+'.txt', 'a')
	key = ','.join(tags3)
	f.write('\n'+key)
	f.close()

		

#---Write into csv file----
f=open('tags2.csv', 'w', encoding='utf8')
writer = csv.writer(f)
#Cna
for x in t3:
	writer.writerow([x,])

#China
for x in t6:
	writer.writerow([x,])

for x in t7:
	writer.writerow([x,])

for x in t8:
	writer.writerow([x,])

for x in t9:
	writer.writerow([x,])


f.close()
	
#---read the csv of keywords---
file = open("tags2.csv", 'r', encoding='utf8')
documents=[]
for line in file.readlines():
	documents.append(line)

stoplist = set('E5 E6'.split())
texts = [[word for word in document.split() if word not in stoplist]for document in documents]

all_tokens = sum(texts, [])

tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) < 10)

texts = [[word for word in text if word not in tokens_once]for text in texts]
all_texts = sum(texts, [])


dictionary = corpora.Dictionary(texts)
s=dictionary.token2id.keys()

for b in s:
	t5.append(b)
print(t5)

#------Write into Mysql-----------
user = 'wenjun'
pwd  = 'wenjun'
host = 'localhost'
db   = 'wenjun'

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()
now = t
for x in t5:
	num = all_texts.count(x)

	add_keyword = ("INSERT INTO keywords "
               "(CATEGORY, COUNT, DATE) "
               "VALUES (%s, %s, %s)")
	data_keyword = (x, num, now)
	cursor.execute(add_keyword, data_keyword)

cnx.commit()
cursor.close()
cnx.close()
print('ok')


