
'''
Mysql Conn連接類
'''

import MySQLdb

class DBConn:

conn = None

#建立和資料庫系統的連接
def connect(self):
self.conn = MySQLdb.connect(host="localhost",port=3306,user="house", passwd="house" ,db="house",charset="utf8")

#獲取操作游標
def cursor(self):
try:
return self.conn.cursor()
except (AttributeError, MySQLdb.OperationalError):
self.connect()
return self.conn.cursor()

def commit(self):
return self.conn.commit()

#關閉連接
def close(self):
return self.conn.close()