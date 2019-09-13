#Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.
def is_two(inpt):
    return float(inpt) == 2

is_two = lambda x: x == 2
#Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel(inpt):
    return inpt.lower() in ['a', 'e', 'i', 'o','u']

is_vowel = lambda x: x.lower() in ['a', 'e', 'i', 'o','u']
#Define a function named is_consonant. It should return True if the passed string is a 
# consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(inpt):
    return inpt.lower() not in ['a', 'e', 'i', 'o','u']

is_consonant = lambda x: x.lower() not in ['a', 'e', 'i', 'o','u']
#Define a function named calculate_tip. It should accept a tip percentage (a number between
#  0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percentage, bill_total):
    return float(bill_total) * float(percentage)

#Define a function named apply_discount. It should accept a original price, and a discount 
# percentage, and return the price after the discount is applied.
def apply_discount(discount, new_price):
    return new_price * (1 - discount)

#Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.
def handle_commas(inpt):
    inpt_list = inpt.split(',')
    return ''.join(inpt_list)

#Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).
def get_letter_grade(number_grade):
    if number_grade >= 90:
        return 'A'
    elif number_grade >= 80:
        return 'B'
    elif number_grade >= 70:
        return 'C'
    elif number_grade >= 60:
        return 'D'
    else:
        return 'F'
    
#Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.
def remove_vowels(inpt):
    return_string = ''
    for character in inpt:
        if character not in ['a', 'e', 'i', 'o', 'u']:
            return_string += character
    return return_string

# Define a function named normalize_name. It should accept a string and return a valid 
# python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
def normalize_name(inpt):
    '''
    takes input and returns normalized name

    normalize_name('Name')
    >>> 'name'

    normalize_name('First Name')
    >>> 'first_name'

    normalize_name('% Completed')
    >>> 'completed'
    '''
    work_in_progress = ''
    #return_name = ''
    for i in inpt:
        if i.isalpha() or i == ' ':
            work_in_progress += i.lower()
    while not work_in_progress[0].isalpha():
        work_in_progress = work_in_progress[1:]
    while not work_in_progress[-1].isalpha():
        work_in_progress = work_in_progress[:-1]
    # for i in work_in_progress:
    #     if i != ' ':
    #         return_name += i
    #     else:
    #         return_name += '_'
    return_name = work_in_progress.replace(' ', '_')
    return return_name
print(normalize_name('% Completed'))

#Write a function named cumsum that accepts a list of numbers and returns a list that is 
# the cumulative sum of the numbers in the list.
def cumsum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] += sum(numbers[i-1:i])
    return numbers
#Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 

def twelveto24(time):
    if time[-2:] == 'am' and time[:-5] != '12':
        return time[:-2]
    elif time[-2:] == 'am' and time[:-5] == '12':
        return '00' + time[-5:-2]
    elif time[-2:] == 'pm' and time[:-5] == '12':
        return time[:-2]
    else:
        time = str(int(time[:-5]) + 12) + time[-5:-2]
        return time
#Bonus write a function that does the opposite.
def militarytostandard(time):
    if int(time[:-3]) >= 13:
        return str(int(time[:-3])-12) + time[-3:] + 'pm'
    elif int(time[:-3]) == 12:
        return time + 'pm'
    elif int(time[:-3]) >= 1:
        return time + 'am'
    else:
        return str(int(time[:-3]) + 12) + time[-3:] + 'am'
#Create a function named col_index. It should accept a spreadsheet column name, and return 
# the index number of the column.
def col_index(column_name):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = 0
    for i in range(1,len(column_name)+1):
        index += (alpha.index(column_name[-i].lower())+1 )* (26 ** (i-1))
    return index
