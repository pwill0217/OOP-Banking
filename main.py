class Account():

    def __init__(self,name,balance=100,):
        self.balance = balance
        self.name = name
    def deposit(self,depst):
        self.balance = self.balance +depst
        print(f'{depst} was added to the balance')
        #this method sets up the ability to deposit an amount

    def withdraw(self,wthdrw):
        if self.balance >= wthdrw:
            self.balance = self.balance - wthdrw
            print('Withdrawal has been processed')
        else:
            print('Not enough funds!')
        #this method allows for you to be able to deposit an amount from the users account
    def __str__(self):
        return f'Name: {self.name} \nBalance: {self.balance}'
    #this method allows the program to return the name of the user and the balance of the user
a = Account('Will', 100)
print(a)
print(a.deposit(400))
print(a)
print(a.withdraw(400))
print(a)

