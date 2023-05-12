low = 0
high = 100
guess = (low + high) // 2
num_guesses = 0
target = 10

while guess != target:
    num_guesses += 1
    print("Is your number", guess, "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate the guess is correct. > ")
    
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        print("I guessed your number in", num_guesses, "guesses!")
        break
    else:
        print("Sorry, I didn't understand your response.")
        
    guess = (low + high) // 2