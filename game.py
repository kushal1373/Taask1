#this is a  random number guessing game

import random
num=int(input("enter a number for the upper limit:"))
random_number=random.randint(1,num)
guess=int(input(f"input a number between 1 and {num}:"))
   
while guess != random_number:  
 if guess < random_number:
    print("your guess was low")
    guess=int(input(f"try again. input a number between 1 and {num}:"))

 elif guess > random_number:
    print("your guess was high")
    guess=int(input(f"try again. input a number between 1 and {num}:"))
 
print(f"congrats!your guess {random_number} was correct!")