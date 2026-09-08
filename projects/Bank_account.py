class Account:
    def __init__(self, acc_no, acc_bal, acc_name):
        self.acc_name = acc_name
        self.acc_bal = acc_bal
        self.acc_no = acc_no
        self.acc_transaction = []

    def deposit(self, amount):
        if amount > 0:    
            self.acc_bal += amount
            print(f"deposited {amount} . New Balance {self.acc_bal}")
            self.acc_transaction.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.acc_bal:    
            self.acc_bal -= amount
            print(f"withdrew {amount} . New Balance {self.acc_bal}")  
            self.acc_transactions.append(("withraw", amount))
        else:
            print("Insufficient funds or invalid amount.")     

    def get_balance(self):
         return self.acc_bal
    def History(self):
         return self.acc_transaction
           

acc1 = Account(12321, 10000, "stark")
acc1.deposit(int(input("Enter amount You want to deposit: ")))
acc1.withdraw(int(input("Enter amount You want to withdraw: ")))
print(acc1.get_balance())
print(acc1.History())