import random

print("Number Guessing Game")
print("Guess a Number between 1 to 9")

num = random.randint(1,9)
chances = 5

while (chances != 0):
    usernum = int(input("Enter your Number: "))
    if (usernum==num):
        print("Excellent👌👌👌, Your guess was correct!!!")
        break
    else:
        print("Your guess was wrong...Try Again😔😔😔")
        chances = chances-1
if (num < 5):
    print("Hint: The random number is less than 5")
else:
    print("Hint: The random number is greater than or equal to 5")