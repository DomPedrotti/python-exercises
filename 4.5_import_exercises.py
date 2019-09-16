from itertools import permutations
import json

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
#720
permutation_list = permutations('abc123')
len(list(permutation_list))

#How many different ways can you combine two of the letters from "abcd"?
#12
len(list(permutations('abcd',2)))

#Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
with open('profiles.json') as json_file:
    data = json.load(json_file)

# Total number of users
print('total number of users')
print(len(data))

# Number of active users
print("number of active users")
print(len([i for i in data if i['isActive']])) 

# Number of inactive users
print('number of inactive users')
print(len([i for i in data if not i['isActive']]))

# Grand total of balances for all users
def handle_commas(inpt):
    inpt_list = inpt.split(',')
    return ''.join(inpt_list)
print('grand total of balances for all users')
balances = []
for i in data:
    amount = handle_commas(i['balance'][1:])
    balances.append(float(amount))
print(sum(balances))

# Average balance per user
print('average balance per user')
def average_list(number_list):
    return sum(number_list)/len(number_list)
print(average_list(balances))

# User with the lowest balance
print('user with lowest balance')
for i in data:
    if min(balances) == float(handle_commas(i['balance'][1:])):
        print(i)
#zach's way
#min(data, key=lambda profile: handle_balance(profile['balance')))

# User with the highest balance
print('user with highest balance')
for i in data:
    if max(balances) == float(handle_commas(i['balance'][1:])):
        print(i)

# Most common favorite fruit
print("most common favorite fruit")
fruit_count = {}
for i in data:
    if i['favoriteFruit'] not in fruit_count.keys():
        fruit_count.update({i['favoriteFruit']: 1})
    else:
        fruit_count[i['favoriteFruit']] += 1
print(max(fruit_count))
#zach's way
from collections import Counter
Counter([p['favoriteFruit'] for p in data])
set([p['favoriteFruit'] for p in data])

# Least most common favorite fruit
print('least most common favorite fruit')
print(min(fruit_count)

# Total number of unread messages for all users
print('total number of unread messages for all users')
total_unread_messages = 0
for i in data:
    if ' ' in i['greeting'][-18:-20]:
        total_unread_messages += int(i['greeting'][-18:-17])
    else:
        total_unread_messages += int(i['greeting'][-18:-16])
print(total_unread_messages)

#zach's way
def extract_digits(s):
        return ''.join([c for c in s if c.isdigit()])