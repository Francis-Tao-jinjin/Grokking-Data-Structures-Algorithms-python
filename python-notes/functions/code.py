from functools import partial
import decimal

def multiply(x, y):
    return x * y

def double1(value):
    # 返回另一个函数调用结果
    return multiply(2, value)

# 使用 lambda 表达式
double2 = lambda value: multiply(2, value)

# 使用 partial 函数，将 multiply 函数的第一个参数固定为 2
double3 = partial(multiply, 2)

def f1():
    print(double1(5))  # Output: 10
    print(double2(5))  # Output: 10
    print(double3(5))  # Output: 10

    basetwo = partial(int, base=2)
    print(basetwo('10010'))  # Output: 18
    print(int('10010', base=2))  # Output: 18


# exception mode 
def exception_mode():
    class CreateAccountExeption(Exception):
        """Unable to create a account error"""

    class Account:
        def __init__(self, username, balance):
            self.username = username
            self.balance = balance

        @classmethod
        def create_account_from_string(cls, s):
            try:
                username, balance = s.split()
                # balance = float(balance)
                balance = decimal.Decimal(balance)
            except ValueError:
                raise CreateAccountExeption('input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')

            if balance < 0:
                raise CreateAccountExeption('balance must be non-negative')
            
            return cls(username, balance)
    
    def caculate_total_balance(acounts_data):
        total = 0
        for account_data in acounts_data:
            try:
                account = Account.create_account_from_string(account_data)
            except CreateAccountExeption as e:
                print(f'Error: {e}')
                continue
            total += account.balance
        return total
    
    accounts_data = ['Tom 100', 'Jerry 200', 'Spike -50', 'Tyke 50', 'Roland invalied']
    print(caculate_total_balance(accounts_data))  # Output: 350

#use null object pattern
def null_object_pattern():
    class NullAccount:
        balance = 0
        username = 0

    class Account:
        def __init__(self, username, balance):
            self.username = username
            self.balance = balance

        @classmethod
        def create_account_from_string(cls, s):
            try:
                username, balance = s.split()
                balance = decimal.Decimal(balance)
            except Exception:
                return NullAccount()
            if balance < 0:
                return NullAccount()
            return cls(username, balance)
    
    def caculate_total_balance1(acounts_data):
        total = 0
        for account_data in acounts_data:
            account = Account.create_account_from_string(account_data)
            total += account.balance
        return total

    def caculate_total_balance2(acounts_data):
        return sum(Account.create_account_from_string(account_data).balance for account_data in acounts_data)
    
    accounts_data = ['Tom 100', 'Jerry 200', 'Spike -50', 'Tyke 50', 'Roland invalied']
    print(caculate_total_balance1(accounts_data))  # Output: 350
    print(caculate_total_balance2(accounts_data))  # Output: 350

null_object_pattern()