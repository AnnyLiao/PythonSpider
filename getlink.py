import mysql.connector
import time
import datetime
t = time.time()
t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
key = []
user = 'root'
pwd  = 'cycuim1016'
host = '127.0.0.1'
db   = 'test'

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()


cursor.execute("SELECT `Links` FROM `weblink` WHERE `Date`= '%s'" % (t))

for r in cursor:
    key.append(''.join(r))
f=open('Url/'+t+'_Url.txt', 'w', encoding = 'utf_8')	

for r in key:
	
	f.write(r)
	
cursor.close()
cnx.close()