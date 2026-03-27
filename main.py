import random

lowest = 1
highest = 100

print("Welcome To Python Number Guessing Game!!")
print()
answer = random.randint(lowest, highest)
is_running = True
guesses = 0

while is_running :
    guess = input(f"Make Your Guess!!(Guess A Number Between {lowest} and {highest}) : ")

    if guess.isdigit() :
        guess = int(guess)
        guesses += 1


        if guess > highest or guess < lowest :
            print("Out Of Range!!")
           # print(f"Guess A Number Between {lowest} and {highest}) : ")
        elif guess == answer :
                print(f"Yayy! You Guessed It Right, The Number was {answer}")
                print(f"You Took {guesses} guesses!")
                break
        elif guess > answer :
             print("Nahh! Try Again, Go Lowerr!!")
               
        elif guess < answer :
            print("Nahh! Try Again, Go Higher!!")
       

    else :
        print("Wrong Format! Try Again!!")


