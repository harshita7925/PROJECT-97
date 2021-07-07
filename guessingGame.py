import random

number=random.randint(1,9)

playerName=input("Hello, what's your name?")
numberOfChances=0
print('OK'+playerName+'I am guessing a number between 1 and 9:')

while numberOfChances < 5:
     guess=int(input("Enter your guess:"))
     numberOfChances+=1
     if guess == number:
        print("Congrats YOU WON")
        break
     
     elif guess < number:
        print('Your guess is too low')
    
     else:
        print('Your guess is too high')

if not numberOfChances < 5:
    print("YOU LOSE!!"+"The number is"+number)