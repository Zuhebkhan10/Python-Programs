#how can we create class
class customer:
    bank_name="SBI"
    branch="Begumpet"
    Ifsc="SBI0002192"
    state="Telangana"

# how can we create an object attributes
    def __init__(self,name,balance,account_number,address):
        self.name=name
        self.balance=balance
        self.account=account_number
        self.address=address

# create a method to welcome a customer in to bank
    def welcome(self):
        return (f"Hello {self.name} Welcome to {self.bank_name} visit the branch {self.branch},and state in {self.state}")

# creat a method to check the balance.
    def check_balance(self):
        return (f"Hello {self.name} Your current balance is {self.balance}/-")

#create a method to deposit the amount into customer account
    def deposit(self,amount):
        self.amount=self.balance+amount
        return (f"""Your transaction is successfull 
your account has been credited with {amount} Your updated balance is {self.balance}""")

        #create a method to withdraw the amount from your amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            return (f"""Your transaction is successfull
Your acoount has been debited with {amount} Your updated balance is {self.balance}""")
        else:
            return(f"Insufficient funds please check your balance")


# Create an object
c1=customer("Shahzain",20000,340001211,"Sohawal")
c2=customer("Arham",35000,459986892,"Hyderabad")

#access the class attributes
# print(c1.bank_name)
# print(c2.Ifsc)

#access the object attributes
print(c1.balance)
print(c1.address)

print(c2.balance)
print(c2.address)

# access the method
print(c1.welcome())
print(c2.welcome())

print(c1.check_balance())
print(c2.check_balance())

print(c1.deposit(10000))
print(c2.deposit(5000))

print(c1.withdraw(15000))
print(c2.withdraw(20000))

# Interview quzyy
#step1: create class and create object
#step2: create class and object attributes and access it
#step3: define the methods inside the class and access the methods