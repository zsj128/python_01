import pymysql

try:
    conn=pymysql.connect(
        host="localhost",user='root',
        password='Aa@1233211234567',db='company'
    )
    
    cursor=conn.cursor()

    while True:

        print('请输入操作：创建表1|查询2|更新3|删除4|插入多条5|退出6')

        action=input()

        if action=='1':
            cursor.execute("SHOW TABLES LIKE 'user'")
            result=cursor.fetchone()
            if result:
                print('表已存在')
            else:
                cursor.execute("CREATE TABLE user (id INT PRIMARY KEY,username varchar(50),gender enum('男','女'),phone varchar(50));")
                print('表创建成功')
                print('连续输入5条数据')
                for i in range(5):
                    insert_input=input().split(' ')
                    insert_input=tuple(insert_input)
                    sql1="insert into user (id ,username,gender,phone) values (%s,%s,%s,%s)"
                    cursor.execute(sql1,insert_input)
                    conn.commit()
  
        if action=='2':
            sql2="select * from user where gender = '男'"
            cursor.execute(sql2)
            result=cursor.fetchall()
            print(result)
            print('查询成功')

        if action=='3':
            print('请输入手机号')
            phone_input=input()
            print('请输入用户名')
            name_input=input()
            sql3="update user set phone=%s where username=%s "
            cursor.execute(sql3,(phone_input,name_input))
            conn.commit()
            print('更新成功')

        if action=='4':

            sql4="delete from user where id=3"
            cursor.execute(sql4)
            conn.commit()
            print('删除成功')

        if action=='5':

            try:
                cursor.execute("insert into user (id ,username,gender,phone) values (10,'张三','男','138')")
                cursor.execute("insert into user (id ,username,gender,phone) values (11,'李四','男','138')")
                cursor.execute("insert into user (id ,username,gender,phone) values (12,'王五','男','138')")
                conn.commit()
                print('连续插入成功')
            except:
                conn.rollback()
        if action=='6':
            break

except pymysql.MySQLError as e:
    print(f'错误：{e}')
finally:
    cursor.close()
    conn.close() 

