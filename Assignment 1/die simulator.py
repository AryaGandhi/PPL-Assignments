import random

print("Type y to roll a die and type q to quit")
user_input = "y"
while user_input == "y":
    print(random.randint(1, 6))
    user_input = input("Roll die again?\n")
    if user_input != 'y' and user_input != 'q':
        user_input = input('Invalid input. Enter y or q\n')
