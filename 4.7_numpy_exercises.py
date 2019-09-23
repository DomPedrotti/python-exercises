import numpy as np 
#Use the following code for the questions below:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\n\nOur first Array, a, is {a}")

# How many negative numbers are there?
a_negatives = a[a < 0]
print("There are {} negative numbers\n".format(len(a_negatives)))

# How many positive numbers are there?
a_positives = a[a > 0]
print("There are {} positive numbers\n".format(len(a_positives)))

# How many even positive numbers are there?
a_pos_evens = a[(a > 0) & (a%2 == 0)]
print("There are {} positive, even numbers\n".format(len(a_pos_evens)))

# If you were to add 3 to each data point, how many positive numbers would there be?
a_plus_3 = a + 3
a_plus_3_positives = a_plus_3[a_plus_3 > 0]
print("If we add 3, there are {} positive numbers\n".format(len(a_plus_3_positives)))

# If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2
print("If we squared our array, our mean would change from \n{} to {}\n".format(np.mean(a), np.mean(a_squared)))
print("If we squared our array, our standard deviation would change from \n{} to {}\n".format(np.std(a), np.std(a_squared)))

# A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
centered_a = a - np.mean(a)
print("Our array, after being centered, becomes\n{}\n".format(centered_a))

# Calculate the z-score for each data point. Recall that the z-score is given by:
a_zscore = centered_a/np.std(a)
print("Our Z-Scores for our array are \n{}".format(a_zscore))

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = np.sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = np.min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = np.max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = np.mean(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a ** 2
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 == 1]
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = np.sum(b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = np.min(b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.max(b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

mean_of_b = np.mean(b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.product(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b ** 2

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
b_shape = np.shape(b)

# Exercise 10 - transpose the array b.
b_transpose = np.transpose(b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
one_dimensional_b = np.reshape(b,(1,6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
one_dimensional_b = np.reshape(b,(6,1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\n\nOur next array, c, is \n{c}\n")
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = np.min(c)
max_of_c = np.max(c)
sum_of_c = np.sum(c)
product_of_c = np.product(c)
print("The min, max, sum, and product of c are {}, {}, {}, and {}, respectively\n".format(min_of_c, max_of_c, sum_of_c, product_of_c))

# Exercise 2 - Determine the standard deviation of c.
c_std = np.std(c)
print(f"The standard deviation of c is {c_std}\n")

# Exercise 3 - Determine the variance of c.
c_variance = np.var(c)
print(f"The variance of c is {c_variance}\n")

# Exercise 4 - Print out the shape of the array c
c_shape = np.shape(c)
print(f"The shape of c is {c_shape}\n")

# Exercise 5 - Transpose c and print out transposed result.
c_transpose = np.transpose(c)
print(f"The transpose of c is\n{c_transpose}\n")

# Exercise 6 - Multiply c by the c-Transposed and print the result.
gramian_matrix_c = c * c_transpose
print(f"The Gramian Matrix of c is \n{gramian_matrix_c}\n")

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum_gram_c = np.sum(gramian_matrix_c)
print(f"the sum of the Gramian Matrix of c is {sum_gram_c}\n")

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
product_gram_c = np.product(gramian_matrix_c)
print(f"the product of the Gramian Matrix of c is {product_gram_c}")


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\n\n Our new array, d, is\n{d}\n")
# Exercise 1 - Find the sine of all the numbers in d
sine_d = np.sin(d)
print(f"The Sine of d is\n{sine_d}\n")

# Exercise 2 - Find the cosine of all the numbers in d
cos_d = np.cos(d)
print(f"The Cosine of d is\n{cos_d}\n")

# Exercise 3 - Find the tangent of all the numbers in d
tan_d = np.tan(d)
print(f"The Tangent of d is\n{tan_d}\n")

# Exercise 4 - Find all the negative numbers in d
d_negatives = d[d < 0]
print(f"These are the negatives in d\n{d_negatives}\n")

# Exercise 5 - Find all the positive numbers in d
d_positives = d[d > 0]
print(f"These are the positives in d\n{d_positives}\n")

# Exercise 6 - Return an array of only the unique numbers in d.
d_uniques = np.unique(d)
print(f"These are the unique numbers in d\n{d_uniques}\n")

# Exercise 7 - Determine how many unique numbers there are in d.
print(f"There are {len(d_uniques)} unique numbers in d\n")

# Exercise 8 - Print out the shape of d.
d_shape = np.shape(d)
print(f"The shape of d is {d_shape}\n")

# Exercise 9 - Transpose and then print out the shape of d.
d_transpose = np.transpose(d)
print(f"Here is the transpose of d,\n{d_transpose}\nIt's shape is {np.shape(d_transpose)}\n")

# Exercise 10 - Reshape d into an array of 9 x 2
d_9x2 = np.reshape(d,(9,2))
print(f"d reshaped into a 9x2 matrix is\n{d_9x2}")
