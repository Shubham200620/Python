# taking user input
a=input('Enter first number:')
b=input('Enter Second number:')

if a.isdigit() and b.isdigit():
    num1=int(a)
    num2=int(b)
    operator=input('Enter operator (+, - , * , / , % , ** , //) :')
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '%':
        print(num1 % num2)
    elif operator == '**':
        print(num1 ** num2)
    elif operator == '//':
        print(num1 // num2)
    else:
        print("Invalid Operator : Please select valid operator")
else:
    print("You have entered invalid number!")

    
