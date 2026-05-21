import pymysql
try:
    conn=pymysql.connect(
        host="localhost",user='root',
        password='Aa@1233211234567',db='company'
    )
    cursor=conn.cursor()
    sql=" delete from employees where emp_name=%s "
    prarams=('钱九')
    cursor.execute(sql,prarams)
    conn.commit()
    print('操作成功')
except pymysql.MySQLError as e:
    print(f'错误：{e}')
finally:
    cursor.close()
    conn.close()