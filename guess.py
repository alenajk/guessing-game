import random 
round=1

name=raw_input("Hello, what is your name?")
print name + ", I'm thinking of a number between 1 and 100."
print "Try to guess my number."

secret_number=random.randrange(1,101)

while True:
    while True:
        try:
            guess=int(raw_input("Whats your guess?"))
            break
        except ValueError:
            print "Not a valid number, please try again."
    if int(guess)<1 or int(guess)>100:
        print "Out of range, try again."
    elif int(guess) > secret_number:
        print "Guess lower"
        round+=1
    elif int(guess) < secret_number:
        print "Guess higher"
        round+=1
    else:
        print "You got it! You found my number in %d tries" % round
        break