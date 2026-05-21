import pymysql
try:
    conn=pymysql.connect(
        host="localhost",user='root',
        password='Aa@1233211234567',db='company'
    )
    cursor=conn.cursor()
    sql="insert into employees (emp_name,salary) values ('钱九','18000')"
    cursor.execute(sql)
    conn.commit()
    print('插入成功')
except pymysql.MySQLError as e:
    print(f'错误：{e}')
finally:
    cursor.close()
    conn.close()