low = int(input("Enter a starting point: "))
high = int(input("Enter an ending point: "))

guess = round((low + high) / 2)
num_guesses = 0

while True:
    print("Is the number", guess, "?")
    response = input("Enter 'c' if the answer is correct, \n'l' if the answer is too low, \nand 'h' if the answer is too high\n").lower()

    if response == 'c':
        print("Thank you for playing!")
        break
    elif response == 'l':
        low = guess
    elif response == 'h':
        high = guess

    guess = round((low + high) / 2)
    num_guesses += 1

print("Number of guesses:", num_guesses)
