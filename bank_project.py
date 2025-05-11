class Customer:
    def __init__(self, Name, Age, Customer_id):
        self.Name = Name
        self.Age = Age
        self.Customer_id = Customer_id
        print("Welcome", self.Name, "to our Bank")
        print("\nHere are your personal Details:\nName:", self.Name, "\nAge:", self.Age, "\nCustomer_id:", self.Customer_id)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("\nYour balance is Rs", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("\nYou deposited Rs", amount)
        print("Your total balance is: Rs", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou have Withdrawn Rs", amount)
            print("Your total balance is: Rs", self.balance)
        else:
            print("Insufficient Balance")

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        print(f"\nWelcome to {self.name} Bank!")
        print(self.customers)

    def add_customer(self, customer):
        self.customers.append(customer)
        print(self.customers.append(customer))

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.Customer_id == customer_id:
                print(f"\n Customer Found: {customer.Name},Age:{customer.Age}")
                return customer
        return None

# Example Usage

bank = Bank("Python Bank")

customer1 = Customer("Ram", 18, 100)
customer2 = Customer("Hanuman", 16, 102)
customer2 = Customer("Luffy", 17, 105)

bank.add_customer(customer1)
bank.add_customer(customer2)
bank.find_customer(102)
found=Bank.find_customer(102)
print(found)

account1 = BankAccount(12345, 200000)
account1.deposit(10000)
account1.withdraw(2000)


