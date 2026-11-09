import os
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def percentage (a,b):
    return a * b / 100

symbols_dict = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' : divide,
    '%' : percentage,
    
}
def calculator():
    num1 = float(input("enter  number : "))
    for symbol in symbols_dict:
        print(symbol)
    continue_calc = True 
    while continue_calc:
        symbol = input("enter operation : ")
        num2 = float(input("enter  number : "))
        calci_function = symbols_dict[symbol]
        output = calci_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {output}")
        should_continue = input(f"Enter 'y' to continue the {output} or 'new' to start new calculation or 'n' to exit : ")
        if should_continue == 'y':
            num1 = output
        elif should_continue == 'new': 
            continue_calc = False
            os.system('cls')
            calculator()
        else:
            continue_calc = False
            print("stopped the calculation")
calculator()