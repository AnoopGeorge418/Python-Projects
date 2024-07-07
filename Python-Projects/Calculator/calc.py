def calculator():
    try:
        operations = ['+', '-', '*', '/', '%']
        input1 = float(input('Enter first number: '))
        operator = input(f'Select a operation to perform from {operations}: ')
        input2 = float(input('Enter second number: '))
        
        if operator not in operations:
            raise ValueError('Invalid operator entered.')
        
        if operator == '+':
            addition(input1, input2)
        elif operator == '-':
            subtraction(input1, input2)
        elif operator == '*':
            multiplication(input1, input2)
        elif operator == '/':
            division(input1, input2)
        elif operator == '%':
            modular(input1, input2)
        else:
            print('Make sure to Enter correct operation t0 perform.')
            
    except ValueError:
        print(f'Error: Make Sure you enter numbers ond make sure the operation is from {operations} and try again.')
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
    

def addition(a, b):
    print(f'Result: {a + b}')

def subtraction(a, b):
    print(f'Result: {a - b}')

def multiplication(a, b):
    print(f'Result: {a * b}')

def division(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero.')
    else:
        print(f'Result: {a / b}')

def modular(a, b):
    print(f'Result: {a % b}')
    

def main():
    print('Welcome to the Simple Calculator.')
    calculator()

# Calling main function to run the program    
if __name__ == '__main__':
    main()