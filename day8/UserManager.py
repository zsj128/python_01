from DBHelper import DBHelper

class UserManager:
    
    def __init__(self,db):
        self.db=db

    def create_user_table(self):
        sql="create table if not exists users(" \
        "id int primary key," \
        "username varchar(50) not null," \
        "email varchar(50) not null" \
        ")"
        self.db.execute(sql)

    def add_user(self,user):
        sql="insert into users(id,username,email) values(%s,%s,%s)"
        self.db.execute(sql,(user['id'],user['username'],user['email']))

    def get_user_by_id(self,id):
        sql="select * from users where id=%s"
        return self.db.query(sql,(id,))
    
    def updata_user_email(self,id,email):
        sql="update users set email=%s where id=%s"
        self.db.execute(sql,(email,id))

    def delete_user(self,id):
        sql="delete from users where id=%s"
        self.db.execute(sql,(id,))

if __name__=='__main__':
    
    db=DBHelper('company')
    u=UserManager(db)

    u.create_user_table()

    u.add_user({'id':1,'username':'张三','email':'22@qq.com'})
    u.add_user({'id':2,'username':'张四','email':'21@qq.com'})
    print(u.get_user_by_id(1))
    print(u.get_user_by_id(2))

    u.updata_user_email(1,'33@qq.com')
    print(u.get_user_by_id(1))

    db.close()