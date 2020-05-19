import random
num = random.randint(1, 100)
user_input = int(input("Guess the number between 1 and 100: "))
while user_input != num:
    if user_input > num:
        print("The number you have guessed is greater than the chosen number")
    elif user_input < num:
        print("The number you have guessed is less than the chosen number")
    user_input = int(input("Guess the number again : "))
print("Congrats you have guessed it right!")
