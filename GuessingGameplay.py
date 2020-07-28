import random
 
hidden = random.randrange(1, 100)
print(hidden)
 
guess = int(input(" Enter your number: "))
 
if guess == hidden:
    print("You are right")
elif guess < hidden:
    print("You loose")
else:
    print("You loose")
