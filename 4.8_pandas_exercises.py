import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Use pandas to create a Series from the following data:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
# Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()
# Run the code necessary to produce only the unique fruit names.
fruits.unique()
# Determine how many times each value occurs in the series.
fruits.value_counts()
# Determine the most frequently occurring fruit name from the series.
fruits.describe()[2] #or
fruits.value_counts().idxmax()
# Determine the least frequently occurring fruit name from the series.
fruits.value_counts()[fruits.value_counts() == 1]
# Write the code to get the longest string from the fruits series.
longest_fruit = fruits.str.len().max()
fruits[fruits.apply(len) == longest_fruit]
# Find the fruit(s) with 5 or more letters in the name.
len_over_5_mask = fruits.apply(len) >= 5
fruits[len_over_5_mask]
# Capitalize all the fruit strings in the series.
fruits.str.upper()
# Count the letter "a" in all the fruits (use string vectorization)
def count_a(x):
    counter = 0
    for i in x:
        if i == 'a':
            counter += 1
    return counter
counted_a = fruits.apply(count_a)
list(zip(fruits.unique(),counted_a))
# Output the number of vowels in each and every fruit.
def count_vowels(x):
    counter = 0
    for i in x:
        if i in 'aeiou':
            counter += 1
    return counter
fruits.apply(count_vowels)
# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits[fruits.apply(lambda x: x.count('o') > 1)]
# Write the code to get only the fruits containing "berry" in the name
mask = fruits.apply(lambda x: 'berry' in x)
fruits[mask]
# Write the code to get only the fruits containing "apple" in the name
mask = fruits.apply(lambda x: 'apple' in x)
fruits[mask]
# Which fruit has the highest amount of vowels?
most_vowels = fruits.apply(count_vowels).max()
mask = fruits.apply(count_vowels) == most_vowels
fruits[mask]





a = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
#a = a.apply(lambda n: float(n.replace(',','').replace('$','')))
a_float = a.str.replace(',','').str.replace('$','').astype(float)
#a = a.str.replace('$','')
#a = a.astype(float)

# print(a_float)
# print(a.max())  
# print(a.min())

# a_bins = pd.cut(a, [0,1250000, 2500000, 3750000, 5000000])
# print(a_bins.value_counts())
#print(a_bins)
#print(a.value_counts(bins = 4))



#hist_plot = a_bins.value_counts()

#hist_plot.plot.hist( bins = 4)
#plt.show()


#Use pandas to create a Series from the following exam scores:
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
# What is the minimum exam score? The max, mean, median?
exam_scores.describe()
exam_scores.median()

# Plot a histogram of the scores.
exam_scores.plot.hist()
# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
letter_scores = pd.cut(exam_scores, bins = [0,60,70,80,90,100], labels = ['f','d','c','b','a'])

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
curve_amount = 100-exam_scores.max()
curved_scores = curve_amount+ exam_scores

#Use pandas to create a Series from the following string:
chars = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
# What is the most frequently occuring letter? Least frequently occuring?
char_counts = chars.value_counts()
max_freq_num = char_counts.max()
min_freq_num = char_counts.min()
max_freq_num = char_counts.max()
max_freq_char = char_counts[char_counts == max_freq_num]
min_freq_char = char_counts[char_counts == min_freq_num]
# How many vowels are in the list?
char_count_keys = pd.Series(char_counts.keys())
is_vowel_mask = np.array(char_count_keys.apply(lambda x: True if x in 'aeiou' else False))
sum_vowels = char_counts[is_vowel_mask].sum()
# How many consonants are in the list?
char_counts.sum()-sum_vowels
# Create a series that has all of the same letters, but uppercased
upper_chars = chars.str.upper()
# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
char_counts.head(6).plot.bar()
plt.show()