user_input= input('Enter a number')

if user_input.isdigit():
    num= int(user_input)
    print("You have entered a Valid Number:", num)
else:
    print("Invalid Input!, Please enter a number")
