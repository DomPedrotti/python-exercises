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

print(right_join,'\n',outer_join)
print(no_foreign_key_join)