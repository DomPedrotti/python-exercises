#!/usr/bin/env python
# coding: utf-8

# In[159]:


#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

import seaborn as sns


# In[5]:


#Use the iris database to answer the following quesitons:
iris = data('iris')


# In[10]:


iris = pd.DataFrame(iris)
iris.info()


# In[12]:


#What does the distribution of petal lengths look like?
sns.distplot(iris['Petal.Length'])


# In[15]:


#Is there a correlation between petal length and petal width?
sns.relplot(x = 'Petal.Length', y = 'Petal.Width', data = iris)


# In[18]:


#Would it be reasonable to predict species based on sepal width and sepal length?
iris['Sepal_lentowid'] = iris['Sepal.Length']/iris['Sepal.Width']
sns.boxplot(data = iris, x = 'Species', y = 'Sepal_lentowid')

iris.corr()
# In[ ]:


# You could accurately guess teh setosa based on sepal length to width


# In[26]:


#Which features would be best used to predict species?
iris['petal_lentowid'] = iris['Petal.Length']/iris['Petal.Width']
sns.boxplot(data = iris, x = 'Species', y = 'petal_lentowid')
sns.relplot(data = iris, x = 'Petal.Length', y = 'Petal.Width',  hue = 'Species')
sns.relplot(data = iris, x = 'Sepal.Length', y = 'Sepal.Width',  hue = 'Species')
pd

# In[ ]:





# In[30]:


#Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
dta = sns.load_dataset('anscombe')
dta.info()
dta.groupby('dataset').describe()


# In[59]:


#Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
dta_1 = dta[dta.dataset == 'I']
dta_2 = dta[dta.dataset == 'II']
dta_3 = dta[dta.dataset == 'III']
dta_4 = dta[dta.dataset == 'IV']

plt.subplot(2,2,1)
sns.regplot(data = dta_1, x = 'x', y = 'y')
plt.title('I')

plt.subplot(2,2,2)
sns.regplot(data = dta_2, x = 'x', y = 'y')
plt.title('II')

plt.subplot(2,2,3)
sns.regplot(data = dta_3, x = 'x', y = 'y')
plt.title('III')

plt.subplot(2,2,4)
sns.regplot(data = dta_4, x = 'x', y = 'y')
plt.title('IV')


# In[58]:


sns.relplot(data = dta, x = 'x', y = 'y', col = 'dataset')


# In[100]:


#Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.

dta = data('InsectSprays')
avg_bugs_left = dta.groupby('spray').mean().sort_values(by = 'count')
sns.barplot(x = avg_bugs_left.index, y = 'count', data = avg_bugs_left) 
plt.title("How many bugs didn't die")
plt.show()


# In[117]:

# Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:
dta = data('swiss')

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)
dta['is_catholic'] = dta['Catholic'] >= 70
# catholic_fertility = dta[['is_catholic', 'Fertility']].groupby('is_catholic').mean()
# catholic_fertility
sns.boxplot(data = dta, x = 'is_catholic', y = "Fertility")


# In[126]:

#What measure correlates most strongly with fertility?
dta = data('swiss')
plt.subplot(2,2,1)
sns.regplot(data = dta, x = 'Fertility', y = 'Agriculture')
plt.title('Ag')

plt.subplot(2,2,2)
sns.regplot(data = dta, x = 'Fertility', y = 'Examination')
plt.title('Exam')

plt.subplot(2,2,3)
sns.regplot(data = dta, x = 'Fertility', y = 'Education')
plt.title('Edu')

plt.subplot(2,2,4)
sns.regplot(data = dta, x = 'Fertility', y = 'Catholic')
plt.title('Cath')

plt.subplots_adjust(hspace = 1)

dta.corr()
# In[153]:


#Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.


# In[133]:


def get_db_url(db_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
url = get_db_url('chipotle')


# In[146]:


dta = pd.read_sql('SELECT * from orders', url)


# In[135]:


type(dta)


# In[145]:


dta.info()


# In[ ]:


dta['item_price'] = data.item_price.str.replace('$','').apply(float)


# In[152]:


most_popular = (data[['item_name', 'quantity', 'item_price']]
    .groupby('item_name')
)
bar_data = (most_popular[['quantity', 'item_price']]
    .apply(sum).sort_values('quantity').tail(4))
bar_data


# In[156]:


sns.barplot(x = bar_data.index, y = 'item_price', data = bar_data)


# In[162]:


#Load the sleepstudy data and read it's documentation. Use seaborn 
#to create a line chart of all the individual subject's reaction 
#times and a more prominant line showing the average change in 
#reaction time.

stdy = data('sleepstudy')
stdy.Subject = 'subject_' + stdy.Subject.astype(str)

# In[181]:


stdy.info()
stdy.head(5)


# In[187]:



sns.lineplot(x = 'Days', y = 'Reaction',hue = 'Subject', data = stdy)
sns.lineplot(x = 'Days', y = 'Reaction', data = stdy)


# In[ ]:




