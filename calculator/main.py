from art import text2art

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
    print(text2art("calculator"))
    should_acumulate = True

    num1 = float(input("What is the first number: "))

    while should_acumulate:
        
        for symbol in operations:
            print(symbol
                )
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number: "))
        answer = operations[op_symbol](num1, num2)

        print(f'{num1} {op_symbol} {num2} = {answer}')

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")
        if choice.lower() == 'y':
            num1 = answer
        elif choice.lower() == 'n':
            print("Exiting..........")
            should_acumulate = False
            print("\n" * 30)
            calculator()
        else:
            print("Something went wrong!!")
            
calculator()