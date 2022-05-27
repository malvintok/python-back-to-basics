import BankAccount as ba

class bank:
  def __init__(self):
    self.accounts = []

  def newAccount(self):
    name = input("Your account name: ")
    initialDeposit = int(input("Initial deposit: "))
    self.accounts.append(ba.bankAccount(name, initialDeposit))
    accountNumber = len(self.accounts) - 1
    print(f"Your account number is {accountNumber}")

  def login(self):
    accountNumber = int(input("Enter your account number: "))
    account = self.accounts[accountNumber]
    self.bankTransaction(account)

  def bankTransaction(self, account):
    choice = 0
    while choice != 4:
      print(f"Good day {account.name}!")
      print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
      choice = int(input("What would you like to do today? "))
      self.processTransaction(account, choice)
    return
  
  def processTransaction(self, account, choice):
    if choice == 1:
      self.deposit(account)
    elif choice == 2:
      self.withdraw(account)
    elif choice == 3:
      self.checkBalance(account)

  def deposit(self, account):
    depsositAmount = int(input("Deposit amount: "))
    outcome = account.deposit(depsositAmount)
    accountBalance = account.checkBalance()
    print(f"{outcome} Account balance: ${accountBalance}")

  def withdraw(self, account):
    withdrawAmount = int(input("Withdraw amount: "))
    outcome = account.withdraw(withdrawAmount)
    accountBalance = account.checkBalance()
    print(f"{outcome} Account balance: ${accountBalance}")

  def checkBalance(self, account):
    outcome = account.checkBalance()
    print(f"Account Balance: ${outcome}")
