from pydataset import data
import pandas as pd 
import numpy as np
from env import user, password, host

# Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
mpg = data('mpg')

# On average, which manufacturer has the best miles per gallon? Honda
mpg['avg_milage'] = (mpg.hwy+mpg.cty)/2
top_mileage = mpg.groupby('manufacturer').avg_milage.mean().sort_values().tail(1)
# How many different manufacturers are there? 15
num_distinct_manufacturers = len(mpg.groupby('manufacturer'))
# How many different models are there? 38
num_models = len(mpg.groupby('model'))
# Do automatic or manual cars have better miles per gallon?
mpg['simple_trans'] = mpg.trans.apply(lambda x: 'manual' if 'manual' in x else 'auto')
manual_vs_auto_mpg = mpg.groupby('simple_trans').avg_milage.mean()

#Joining and Merging
# Copy the users and roles dataframes from the examples above. What do you think a right join would look like? An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

right_join = users.merge(roles, how = 'right', left_on = 'role_id', right_on = 'id')
outer_join = users.merge(roles, how = 'outer', left_on = 'role_id', right_on = 'id')
no_foreign_key_join = users.drop(columns = ['role_id']).merge(roles)

#Getting data from SQL databases

# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
def get_db_url(db_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
# Use your function to obtain a connection to the employees database.
url = get_db_url('employees')
query = 'select * from departments'
departments = pd.read_sql(query, url)
# Once you have successfully run a query:
    # Intentionally make a typo in the database url. What kind of error message do you see? "Access denied for user 'bayes_816'@'%' to database 'employee'")
url = get_db_url('employee')
query = 'select * from departments'
departments = pd.read_sql(query, url)
    # Intentionally make an error in your SQL query. What does the error message look like? "Table 'employees.department' doesn't exist"
url = get_db_url('employees')
query = 'select * from department'
departments = pd.read_sql(query, url)
# Read the employees and titles tables into two separate dataframes
emp_qry = 'select * from employees'
tit_qry = 'select * from titles'
employees = pd.read_sql(emp_qry, url)
titles = pd.read_sql(tit_qry, url)
# Visualize the number of employees with each title.
emp_titles= employees[['emp_no','first_name','last_name',]] .merge(titles[['emp_no','title']], on = 'emp_no')
print(emp_titles.groupby('title').count())
# Join the employees and titles dataframes together.
# Visualize how frequently employees change titles.
            #look as how many titles employees held
# For each title, find the hire date of the employee that was hired most recently with that title.
emp_titles[['title','hire_date']].groupby('title').max() 
# Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)
query = '''select emp_no, dept_name as dept, select title, dept_name as dept 
from `departments` as d 
join `dept_emp` as jun 
using(dept_no) 
join titles 
using(emp_no)
where titles.`to_date` > now(); 
'''
dept_tits = pd.read_sql(query, url)  
pd.crosstab(dept_tits.dept, dept_tits.title)  

# Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:
url = get_db_url('chipotle')
df = pd.read_sql('select * from orders', url)                
# What is the total price for each order?
df.item_price = df.item_price.str.replace('$','').apply(float)    
order_price = df[['order_id','item_price']].groupby('order_id').sum()      
# What are the most popular 3 items?
df.groupby('item_name').count().sort_values('id').tail(3)    
# Which item has produced the most revenue?
df[['item_name','item_price']].groupby('item_name').sum().sort_values().tail(1)
