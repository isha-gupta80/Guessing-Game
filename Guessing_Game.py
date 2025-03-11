import random 
import time
guess = 0
tries = 0

number = random.randint(1,10)

name = input("Howdy,May I know Your Name:")
print("Hello "+name+".")

question = input("Are you Ready to Guess? [y/n]")
         

if question == 'n':
    print("I'm sorry, We'II meet each other next time!")
    exit()
if question == 'y':
    print("I'm thinking of a number between 1 and 10")
    
while not (guess == number):  # OR while guess !=number:
    guess = int(input("what's your guess?"))
    tries = tries + 1
    if guess == number:
        print("Brilliant")
        time.sleep(1)
        print("Congrats,your guess was correct. The number was indeed{}.".format(number))
        time.sleep(1)
        print("It has taken you {} tries".format(tries))
    elif guess < number :
        print("No! Guess Higher")
    elif guess > number :
        print("No! Guess lower")
    
