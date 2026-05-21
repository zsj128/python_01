import pymysql

class DBHelper:

    def __init__(self,db):
        self.conn=pymysql.connect(
            host="localhost",user='root',
            password='Aa@1233211234567',
            database=db,charset='utf8mb4'
        )
        self.cursor=self.conn.cursor()

    def query(self,sql,params=None):
        self.cursor.execute(sql,params or ())
        return self.cursor.fetchall()
    
    def execute(self,sql,params=None):
        try:    
            self.cursor.execute(sql,params or ())
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
    
    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__=='__main__':
    db=DBHelper('company')
    print(db.query('select * from employees'))
    db.close()



