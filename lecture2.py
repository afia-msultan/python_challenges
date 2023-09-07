###################
## EXAMPLE: strings
###################
hi = "hello there" # enclose in quotation marks or single quotes
name = "ana"
greet = hi + name # concatenate strings
print(greet)  # prints without space
greeting = hi + " " + name # insert space
print(greeting)  # will now print with space
silly = hi + (" " + name)*3     # will print with space and name three times
print(silly)

####################
## EXAMPLE: output
####################
x = 1
print(x)
x_str = str(x) # casting into string
print("my fav number is", x, ".", "x=", x) # using comma: space automatically added
print("my fav number is", x_str + "." + "x=" + x_str) # where plus sign is used: no space
print("my fav number is" + x_str + "." + "x=" + x_str) # plus sign is used nowhere so no space is added anywhere


####################
## EXAMPLE: input
####################
text = input("Type anything... ") # user input will be string by default always - casting needs to be done if other types wanted to be inputted
print(5*text) # user input will become a string and in this case will be printed 5 times
num = int(input("Type a number... ")) # here the user input will become an integer due to casting
print(5*num) # will print the value of 5 multiplied by the int given by user


####################
## EXAMPLE: conditionals/branching
####################
x = float(input("Enter a number for x: ")) # single equal is assignment
y = float(input("Enter a number for y: "))
if x == y:  # equality test; not assignment
    print("x and y are equal")
    if y != 0: # y is not equal to zero; inequality test
        print("therefore, x / y is", x/y)
elif x < y:  # x is less than y
    print("x is smaller")
elif x > y: # x is greater than y
    print("y is smaller")
print("thanks!")



####################
## EXAMPLE: remainder
####################
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")


####################
## EXAMPLE: while loops
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that.
## Hint: use a counter
####################
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")
# stuck in the above loop as long as the user keeps inputting right; once left is entered you will be out of the loop and the code below it will be executed


n = 0
while n < 5: # will continue to loop as long as n is less than 5
    print(n)
    n = n+1  # increase the value of n each time


####################
## EXAMPLE: for loops
####################
for n in range(5): # another way to do what is done in while loop above; more efficient
    print(n)
    # will automatically move on to the next number up until 5 but not including 5

mysum = 0
for i in range(10):
    mysum += i
print(mysum) # sum  of #s from 0 to 9

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i  # first time through loop, mysum = 5
    if mysum == 5: # this will become true first time through loop
       break  # will break out of the loop on the first value since first value is 5
       # mysum += 1         # will not execute this code
print(mysum) # final output will be 5



####################
## EXAMPLE: perfect squares
####################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


####################
## TEST YOURSELF!
## Modify the perfect squares example to print
## imaginary perfect sqrts if given a negative num.
####################