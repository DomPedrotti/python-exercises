from pydataset import data
import pandas as pd
import numpy as np 


#Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas','Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# Create a column named passing_english that indicates whether each student has a passing grade in reading.
df['passing_english'] = df.english > 70

# Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by = 'passing_english')

# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by = ['passing_english', 'name'])

# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by = ['passing_english', 'english'])

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['grade'] = (df['math']+df['english']+df['reading'])/3

# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')

# How many rows and columns are there?
row_columns = mpg.shape

# What are the data types of each column?
column_types = mpg.dtypes

# Summarize the dataframe with .info and .describe
mpg_info = mpg.info
mpg_describe = mpg.describe()

# Rename the cty column to city.
mpg = mpg.rename(columns = {'cty': 'city'})

# Rename the hwy column to highway.

mpg = mpg.rename(columns = {'hwy' : 'highway'})
# Do any cars have better city mileage than highway mileage?
mpg[mpg['city'] > mpg['highway']]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = mpg['highway']- mpg['city']
# Which car (or cars) has the highest mileage difference?
max_mileage_diff_num = mpg['mileage_difference'].max()
max_mileage_diff_row = mpg[mpg['mileage_difference'] == max_mileage_diff_num]
# Which compact class car has the lowest highway mileage? The best?
compact_class = mpg[mpg['class'] == 'compact']
most_compact = compact_class['highway'].max()
least_compact = compact_class['highway'].min()
most_compact_rows = compact_class[compact_class['highway'] == most_compact]
least_compact_rows = compact_class[compact_class['highway'] == least_compact]


# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg['highway'] + mpg['city'])/2

# Which dodge car has the best average mileage? The worst?
dodges = mpg[mpg.manufacturer == 'dodge']
most_dodge = dodges.average_mileage.max()
least_dodge = dodges.average_mileage.min()
most_dodge_rows = dodges[dodges.average_mileage == most_dodge]
least_dodge_rows = dodges[dodges.average_mileage == least_dodge]

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mam = data('Mammals')
# How many rows and columns are there?
mam_shape = mam.shape

# What are the data types?
mam_types = mam.dtypes

# Summarize the dataframe with .info and .describe
mam.info
mam_descrption = mam.describe()
# What is the the weight of the fastest animal?
top_speed = mam.speed.max()
top_speed_row = mam[mam.speed == top_speed]
# What is the overal percentage of specials?
count_special = mam.specials.sum()
portion_specials = count_special / mam.specials.count()
percent_specials = portion_specials * 100

# How many animals are hoppers that are above the median speed? What percentage is this?
hoppers = mam[mam.hoppers]
median_speed = mam.speed.median()
num_fast_hoppers = hoppers[hoppers.speed >= median_speed].shape[0]
