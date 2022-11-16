import pymysql

db=pymysql.connect(host='localhost',
                   user='root',
                   password='12345678',
                   database='demo2',
                   cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query='create table amma(name varchar(10) primary key,age int(25))'
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()

