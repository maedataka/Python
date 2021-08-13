class Account(object):
    
    account_number = -1
    
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        Account.account_number += 1
        
    def withdraw(self, price):
        if self.balance >= price:
            self.balance -= price
            print(f"講座名：{self.name}, 口座番号：{Account.account_number},残高：{self.balance}")
        else:
            print("残高不足です！！")
        
    def deposit(self, price):
        self.balance += price
        print(f"講座名：{self.name}, 口座番号：{Account.account_number},残高：{self.balance}")
        
        
john = Account(0, "john")
john.deposit(10)
john.withdraw(100)
john.deposit(10000)
john.withdraw(1000)
        
        