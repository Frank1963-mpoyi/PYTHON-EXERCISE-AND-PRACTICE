'''
# while loop GUESSING GAME 
#-------------------------
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1

    if guess == secret_number:
        print("you won !")
        break #this will break the loop because we find the good answer
else:
    print('Sorry, you failed !') # a while loop can also have a else part like if statement
    # if the user guess 3 times and failed the condition will fall in Else statement

'''

command = " "

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("car started .....")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print(""" 
        start - to start the car
        stop - to stop the car
        quit - to quit
        
        """)
    else:
        print("Sorry i dont understand that")