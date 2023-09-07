cube = int(input("Enter a number - positive or negative - perfect cube or non-perfect cube: "))
abs_cube = abs(cube)

epsilon = 0.01
num_guesses = 0
low = 0
high = abs_cube
guess = (high + low)/2.0

while abs(guess**3 - abs_cube) >= epsilon:
    if guess**3 < abs_cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1

print('num_guesses =', num_guesses)

if cube < 0:
    print((guess * -1), 'is close to the cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)