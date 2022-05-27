# Main Program
# Focus on organisation, acts as marshaller
# Don't doesn't do processing, find someone else to do it

import Bank as b

bank = b.bank()
choice = 0

while choice != 3:
  print("Welcome to Bank!")
  print("1. New Bank Account\n2. Login Bank Account")
  choice = int(input("What would you like to do? "))

  if choice == 1:
    bank.newAccount()
  elif choice == 2:
    bank.login()
  elif choice == 3:
    print("SHUT DOWN")
    choice = 3