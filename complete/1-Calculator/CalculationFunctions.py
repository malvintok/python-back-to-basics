# Functions
def add(num1, num2):
  result = num1 + num2
  return result

def subtract(num1, num2):
  result = num1 - num2
  return result

def multiply(num1, num2):
  result = num1 * num2
  return result

def divide(num1, num2):
  result = num1 / num2
  return result

# Inputs
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Which calculation do you want to do? ")) # String
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# Processes
if choice == 1:
  result = add(num1, num2)
elif choice == 2:
  result = subtract(num1, num2)
elif choice == 3:
  result = multiply(num1, num2)
elif choice == 4:
  result = divide(num1, num2)

# Output
print(f"Your result is {result}!")