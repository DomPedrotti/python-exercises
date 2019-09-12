# 1)Conditional Basics
    # prompt the user for a day of the week, print out whether the day is Monday or not
    # prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("Pick a day of the week \n").lower()
output = ""
if day == 'monday':
    output += "that's Monday!"
else:
    output += "That's not Monday"
if day in ('saturday','sunday'):
    output += " and it's on the weekend"
elif day in ('monday', 'tuesday','wednesday','thursday','friday'):
    output += " and it's a weekday"
else:
    output += " infact, it's not a day of the week at all"
print(output)
    # create variables and make up values for
        # the number of hours worked in one week
        # the hourly rate
        # how much the week's paycheck will be
number_hours_worked = 80
hourly_rate = 30
paycheck_amount = number_hours_worked * hourly_rate
    # write the python code that calculates the weekly paycheck. You get paid time and a half if you work more 
    # than 40 hours
overtime_pay = 0
if number_hours_worked > 40:
    overtime_pay = (number_hours_worked-40) * (hourly_rate/2)
paycheck_amount = number_hours_worked * hourly_rate + overtime_pay


# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new 
# line.
twos = 0
while twos <= 100:
    print(twos)
    twos += 2
# Alter your loop to count backwards by 5's from 100 to -10.
minus_fives = 100
while minus_fives >= -10:
    print(minus_fives)
    minus_fives -= 5
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less 
# than 1,000,000.
squares = 2
while squares <= 1000000:
    print squares 
    squares = squares ** 2
#Write a loop that uses print to create the output shown below.
for x in range(100,0, -5):
    print x

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that 
# number.
number = input("gimme a number:\n")
for i in range(1,11):
    print(f'{number} X {i} = {float(number)*i}')
# Create a for loop that uses print to create the output shown below.
for i in range(1,10):
    print(i * str(i))
#break and continue

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the 
# user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and 
# the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
number = 0
while number not in range(1,50,2):
    while True:
        try:
            number = int(input('gimme an odd number between 1 and 50\n'))
            break
        except(ValueError):
            contunue
print(f'Number to skip is: {number}')
for i in range (1,50,2):
    if i != number:
        print(f'Here is an odd number: {i}')
    else:
        print(f'Yikes! Skipping number: {number}')
#The input function can be used to prompt for input and use that input in your python code. Prompt the user to 
# enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the 
# value the user entered is a valid number, also note that the input function returns a string, so you'll need 
# to convert this to a numeric type.)
while True:
    number = input("enter a positive number:\n  ")
    if number.isdigit() and int(number) > 0:
        break
for i in range(1,int(number)+1):
    print(i)
#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers 
# from the number the user entered down to 1.
while True:
    number = input("enter a positive integer:\n  ")
    if number.isdigit() and int(number) > 0:
        break
for i in range(int(number),0,-1):
    print(i)

#fizzbuzz
for i in range(1,101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)
#Display a table of powers.
number = input("enter an integer")
print("|number    |squared   |cubed     |")
print("|----------|----------|----------|")
for i in range(1,int(number)+1):
    blank_space_number = (10-len(str(i))) * ' '
    blank_space_square = (10 -len(str(i**2))) * " "
    blank_space_cube = (10 -len(str(i**3))) * " "
    print("|" + str(i) + blank_space_number + "|" + str(i**2) + blank_space_square + "|" + str(i**3) + blank_space_cube + "|")