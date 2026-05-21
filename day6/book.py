class Book:
    def __init__(self,bookname,author,prices):
        self.bookname=bookname
        self.author=author
        self.prices=prices
    def show_info(self):
        print(f'书名：{self.bookname}，作者：{self.author}，价格：{self.prices}')
    
b=Book('bookname','李四',56)
b.show_info()