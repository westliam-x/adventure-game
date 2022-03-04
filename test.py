import random

trange= input("Typea a range: ")

if trange.isdigit():
    trange=int(trange)

    if trange<=0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("Type a number next time.")
    quit()

random_number = random.randint(0,trange)
guesses=0
while True:
     guesses+=1
     user_guess= input("Make a guess: ")
     if user_guess.isdigit():
        user_guess=int(user_guess)
     else:
            print("Type a number next time.")
            continue

     if user_guess==random_number:
        print("You got it")
        break
     elif user_guess>random_number:
            print("You are above the number!")
     else:
            print("You are below the number")

print("you got it in", guesses, "guesses")
