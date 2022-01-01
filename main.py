import art

print(art.logo)

def add (n1,n2):
  return (n1+n2)

def subtraction (n1,n2):
  return (n1-n2)

def multiplication(n1,n2):
  return (n1*n2)

def division(n1,n2):
  return (n1/n2)

operations = {
"+":add,
"-":subtraction,
"*":multiplication,
"/":division
}
def calculation():
  num1 = float(input("What's the first number?: "))

  should_continue = True

  while(should_continue):

    next_number = float(input("What's the next number?: "))
    for operator in operations:
      print(operator)
    choice = input("Pick an operation from the line above :")
    answer = operations[choice](num1,next_number)
    print(f"{num1}{choice}{next_number} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: \n").lower() =="y":
      num1=answer

    else:
        should_continue = False
        calculation()

calculation()

