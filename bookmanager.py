import pymysql
import time

class BookManager:
    # 初始化数据库连接
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",          # 改为自己的MySQL账号
                password="Aa@1233211234567",# 改为自己的MySQL密码
                database="book_db",
                charset="utf8mb4",
                autocommit=False
            )
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            print("✅ 数据库连接成功")
        except Exception as e:
            print("❌ 数据库连接失败：")

    # 日志记录工具
    def write_log(self, msg):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("book_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{now}] {msg}\n")

    def add_book(self, book_id, book_name, author, sort,user_id):
        try:
            sql = "INSERT INTO book(book_id, book_name, author, sort) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(sql, (book_id, book_name, author, sort))
            self.conn.commit()
            print("✅ 图书信息添加成功")
            self.write_log(f"用户{user_id}新增图书：图书编号{book_id}，书名{book_name}，作者{author}，分类{sort}")
        except Exception as e:
            self.conn.rollback()
            print(f"❌ 添加失败！图书编号重复或数据格式错误")

    def show_all_book(self):
        sql = """
        SELECT s.book_id, s.book_name, s.author, s.sort, s.state
        FROM book s
        """
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        if not res:
            print("暂无图书数据！")
            return

        print("\n========== 图书完整信息 ==========")
        for item in res:
            print(f"图书编号：{item['book_id']} | 书名：{item['book_name']} | 作者：{item['author']} | 分类：{item['sort']} | 状态：{item['state']}")
            print("-" * 90)

    def search_book_by_id(self, book_id,user_id):
        sql = """
        SELECT s.book_id, s.book_name, s.author, s.sort, s.state
        FROM book s
        WHERE s.book_id = %s
        """
        self.cursor.execute(sql, book_id)
        res = self.cursor.fetchone()

        if res:
            print("\n========== 图书信息详情 ==========")
            print(f"图书编号：{res['book_id']}")
            print(f"书名：{res['book_name']}")
            print(f"作者：{res['author']}")
            print(f"分类：{res['sort']}")
            print(f"状态：{res['state']}")
            print()
            self.write_log(f"用户{user_id}查询图书信息：图书编号{book_id}")
        else:
            print("❌ 未查询到该图书信息！")

    def update_book_info(self, book_id,new_book_name ,new_author, new_sort,user_id):
        try:
            sql = "UPDATE book SET book_name=%s , author=%s, sort=%s WHERE book_id=%s"
            self.cursor.execute(sql, (new_book_name , new_author, new_sort, book_id))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("✅ 图书信息修改成功")
                self.write_log(f"用户{user_id}修改图书信息：图书编号{book_id}")
            elif self.cursor.rowcount == 0:
                print("图书信息未被修改")
            else:
                print("❌ 未找到该图书")
        except Exception as e:
            self.conn.rollback()
            print(f"❌ 修改失败{e}")

    def delete_book(self, book_id,user_id):
        try:
            sql = "DELETE FROM book WHERE book_id=%s"
            self.cursor.execute(sql, book_id)
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("✅ 该图书信息已全部删除")
                self.write_log(f"用户{user_id}删除图书信息：图书编号{book_id}")
            else:
                print("❌ 未找到该图书")
        except:
            self.conn.rollback()
            print("❌ 删除失败")

    def borrow_book(self,book_name,user_id):
        sql = """
        SELECT s.book_id, s.book_name, s.author, s.sort, s.state
        FROM book s
        WHERE s.book_name = %s
        """
        self.cursor.execute(sql, book_name)
        res = self.cursor.fetchone()

        if res:
            if res['state']=='可借阅':
                sql = "UPDATE book SET state='已借阅' WHERE book_name=%s"
                self.cursor.execute(sql,book_name)
                self.conn.commit()
                print("✅ 图书借阅成功")
                self.write_log(f"{book_name}图书已被用户{user_id}借阅：图书编号{res['book_id']}")
            else:
                print("❌ 该图书已被借阅！")
        else:
            print("❌ 未查询到该图书信息！")

    def return_book(self,book_name,user_id):
        sql = """
        SELECT s.book_id, s.book_name, s.author, s.sort, s.state
        FROM book s
        WHERE s.book_name = %s
        """
        self.cursor.execute(sql, book_name)
        res = self.cursor.fetchone()

        if res:
            try:
                sql = "UPDATE book SET state='可借阅' WHERE book_name=%s"
                self.cursor.execute(sql,book_name)
                self.conn.commit()
                print("✅ 图书归还成功")
                self.write_log(f"用户{user_id}将{book_name}图书已归还：图书编号{res['book_id']}")
            except:
                print("❌ 图书归还失败")
        else:
            print("❌ 未查询到该图书信息！")
        

    def is_users_id(self,users_id):
        sql="SELECT admin_id FROM admin where admin_id=%s"
        self.cursor.execute(sql,users_id)
        self.conn.commit()
        res = self.cursor.fetchall()
        return res

    def is_passwords(self,users_id,passwords):
        sql="SELECT passwords FROM admin where admin_id=%s"
        self.cursor.execute(sql,users_id)
        self.conn.commit()
        res = self.cursor.fetchall()
        if res==[{'passwords':passwords}]:
            self.write_log(f"用户{users_id}已登入")
            return True
        else:
            print("❌ 密码错误")
            return False
        
    def change_password(self,new_passwords,user_id):
        sql="UPDATE admin SET passwords=%s WHERE admin_id=%s"
        self.cursor.execute(sql, (new_passwords, user_id))
        self.conn.commit()
        print("✅ 修改密码成功")


    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("✅ 数据库连接已关闭")

# 主菜单函数
def main():
    sm = BookManager()
    while True:
        user_id=input("请输入管理员用户名（退出输入0）：")
        if user_id=='0':
            break
        elif sm.is_users_id(user_id)==():
            print('管理员用户不存在')
            continue
        else:
            action=input("是否修改密码y/n：")
            if action=='y':
                passwords=input("请输入旧密码：")
                if not sm.is_passwords(user_id,passwords):
                    continue
                else:
                    new_password=input("请输入新密码：")
                    sm.change_password(new_password,user_id)
            passwords=input("请输入登入密码：")
            if not sm.is_passwords(user_id,passwords):
                continue
            else:
                print("✅ 登入成功")
                while True:
                    print("\n======= 图书信息管理系统 =======")
                    print("1. 添加图书信息")
                    print("2. 查看所有图书完整信息")
                    print("3. 按编号查询图书信息")
                    print("4. 修改图书信息")
                    print("5. 借阅图书")
                    print("6. 归还图书")
                    print("7. 删除图书信息")
                    print("0. 退出系统")
                    print("==========================================")

                    choice = input("请输入功能编号：")

                    if choice == "1":
                        book_id = input("请输入图书编号：")
                        book_name = input("请输入书名：")
                        author = input("请输入作者姓名：")
                        sort = input("请输入图书分类：")
                        sm.add_book(book_id,book_name,author,sort,user_id)

                    elif choice == "2":
                        sm.show_all_book()

                    elif choice == "3":
                        book_id = input("请输入查询编号：")
                        sm.search_book_by_id(book_id,user_id)

                    elif choice == "4":
                        book_id = input("请输入要修改的图书编号：")
                        sm.search_book_by_id(book_id,user_id)
                        book_name = input("请输入新的图书名称：")
                        author = input("请输入新的作者名称：")
                        sort = input("请输入新的图书分类：")
                        sm.update_book_info(book_id, book_name, author, sort,user_id)

                    elif choice == "5":
                        book_name = input("请输入要借阅的图书名称：")
                        sm.borrow_book(book_name,user_id)
                    
                    elif choice == "6":
                        book_name = input("请输入要归还的图书名称：")
                        sm.return_book(book_name,user_id)

                    elif choice == "7":
                        book_id = input("请输入要删除的图书id：")
                        action=input("确认是否删除该图书信息y/n：")
                        if action=='y':
                            sm.delete_book(book_id,user_id)
                    elif choice == "0":
                        sm.close()
                        print("👋 系统退出成功，再见！")
                        break

                    else:
                        print("❌ 输入无效，请输入0-6的数字！")
        break

if __name__ == "__main__":
    main()