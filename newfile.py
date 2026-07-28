#The number game(v1.0)
print("Welcome to the number game!")
import random
number = random.randint(1,10)
score = 0

print("Round 1")

guess = int(input("Guess number [1-10]: "))

if guess == number:
    print("Correct!")
    score += 10
else:
    print("Wrong, the number was ", number)
    
number = random.randint(1,20)
print("Round 2")

guess = int(input("Guess number [1-20] "))

if guess == number:
    print("Correct!")
    score += 10
else:
    print("Wrong the number was ", number)
    
number = random.randint(1,30)
print("Round 3")

guess == int(input("Guess number [1-30] "))

if guess == number:
    print("Correct!")
    score += 10
else:
    print("Wrong the number was ", number)
    
number = random.randint(1,40)
print("Round 4")

guess = int(input("Guess number [1-40] "))

if guess == number:
    print("Correct!")
    score += 10
else:
    print("Wrong the number was ", number)
    
number = random.randint(1,50)
print("Round 5")

guess = int(input("Guess number [1-50] "))

if guess == number:
    print("Correct!")
    score += 10
else:
    print("Wrong the number was ", number)
    
print("GAME OVER!")
print(f"Your final score is", score)