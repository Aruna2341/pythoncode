import pymysql

connection=pymysql.connect(host='localhost',
                   user='root',
                   password='12345678',
                   database='demo2')
                   #cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    #Read a single record
    sql = "select * from accounts"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)


