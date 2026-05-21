import pymysql
try:
    conn=pymysql.connect(
        host="localhost",user='root',
        password='Aa@1233211234567',db='company'
    )
    cursor=conn.cursor()
    try:
        cursor.execute("update employees set salary=salary-100 where emp_name='A'")
        cursor.execute("update employees set salary=salary+100 where emp_name='B'")
        conn.commit()
    except:
        conn.rollback()
except pymysql.MySQLError as e:
    print(f'错误：{e}')
finally:
    cursor.close()
    conn.close()