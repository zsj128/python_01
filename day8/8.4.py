import pymysql
try:
    conn=pymysql.connect(
        host="localhost",user='root',
        password='Aa@1233211234567',db='company'
    )
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE salary between 8000 and 10000')
    res=cursor.fetchall()
    print(res)
except pymysql.MySQLError as e:
    print(f'错误：{e}')
finally:
    cursor.close()
    conn.close()