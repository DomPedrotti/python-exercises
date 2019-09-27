from pydataset import data
import pandas as pd 

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
print(manual_vs_auto_mpg.max())