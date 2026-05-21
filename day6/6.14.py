class BankAccount:
    def __init__(self,account_id,name,password,balance=0):
        self.account_id=account_id
        self.name=name
        self.__balance=balance
        self.__password=password
    def show_balace(self,input_word):
        if input_word==self.__password:
            print(f"资金总额:{self.__balance}")
        else:
            print("密码错误")
    def deposit(self,input_num1,input_word):
        if input_word==self.__password:
            self.__balance+=input_num1
        else:
            print("密码错误")
    def withdraw(self,input_num2,input_word):
        if input_word==self.__password:
            if self.__balance>=input_num2:
                self._BankAccount__balance-=input_num2
            else:
                print("余额不足")
        else:
            print("密码错误")
    def change_password(self,now_word,input_word):
        if now_word==self._BankAccount__password:
            self._BankAccount__password=input_word
        else:
            print("旧密码输入错误")
    def interest(self,input_word):
        if input_word==self.__password:
            print(f'年利息为：{self._BankAccount__balance*0.015}')
        else:
            print("密码错误")

b=BankAccount(123,'name','password')

while True:
    print("选择操作：开户1|查询余额2|存款3|取款4|修改密码5|计算年利息6|退出7")
    action=input()
    if action=='7':
        break
    if action=='1':
        print("输入账户名称：")
        name=input()
        while True:
            print("输入账户密码：")
            password=input()
            if any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
                break
            else:
                print("密码过于简单，重新输入密码")
        print("输入账户初始金额（可不输入）：")
        balance=input()
        if balance=='':
            balance=0
        else:
            balance=float(balance)
        b.name=name
        b._BankAccount__password=password
        b._BankAccount__balance=balance
        b.account_id=124
    if b.account_id!=124:
        print("请先开户")
    else:
        if action=='2':
            print("输入密码：")
            password2=input()
            b.show_balace(password2)
        if action=='3':
            print("输入密码：")
            password3=input()
            print("输入存入的金额：")
            input_prices=float(input())
            b.deposit(input_prices,password2)
        if action=='4':
            print("输入密码：")
            password4=input()
            print("输入取出的金额：")
            output_prices=float(input())
            b.withdraw(output_prices,password4)
        if action=='5':
            print("输入旧密码：")
            password5=input()
            while True:
                print("输入新密码：")
                new_password=input()
                if any(c.isdigit() for c in new_password) and any(c.isalpha() for c in new_password):
                    break
                else:
                    print("密码过于简单，重新输入密码")
            b.change_password(password5,new_password)
        if action=='6':
            print("输入密码：")
            password6=input()
            b.interest(password6)
        
        