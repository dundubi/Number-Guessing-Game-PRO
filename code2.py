import random

print("Number Guessing Game")
print("Guess a Number between 1 to 9")

usernum1 = int(input("Enter your first number"))
usernum2 = int(input("Enter your second number"))
num = random.randint(usernum1,usernum2)
chances = 5
num2 = num/2

while (chances != 0):
    usernum = int(input("Enter your Guess"))

    if (usernum==num):
        print("Excellent👌👌👌, Your guess was correct!!!")
        break
    else:
        print("Your guess was wrong...Try Again😔😔😔")
        chances = chances-1
    if (num < num2):
        print("Hint: The random number is less than ", num2)
    else:
        print("Hint: The random number is greater than or equal to ", num2)