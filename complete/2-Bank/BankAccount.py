class bankAccount:

  # Constructor
  def __init__(self, name, initialDeposit):
    self.name = name
    self.balance = initialDeposit

  def deposit(self, depositAmount):
    self.balance += depositAmount
    return f"Deposited ${depositAmount} successfully."

  def withdraw(self, withdrawAmount):
    if self.balance > withdrawAmount:
      self.balance -= withdrawAmount
      return f"Withdrawn ${withdrawAmount} successfully."
    else:
      return "Insufficient funds."

  def checkBalance(self):
    return self.balance