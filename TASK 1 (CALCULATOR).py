def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  
  num1 = float(input("enter the first number:"))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("enter the second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice=input("enter 'y' to continue or'new' to start a new calculation or 'exit' to exit the calculation :").lower()

    if choice == 'y':
      num1 = answer
    elif choice=="new" :
      should_continue = False
      
      calculator()
    else:
      should_continue = False
      print("Thanks")
      

calculator()
