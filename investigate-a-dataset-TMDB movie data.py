#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset (TMDB movie data)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ### Introduction
# 
#  The data set I chose to Analysis contain information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue. By reading the desired file we finf that It consist of 21 columns such as imdb_id, revenue, budget, cast... etc.
# 
# here we can pose the following questions:
# - Which movie has the smallest and largest revenues?
# - Which movie has the smallest and largest Budget?
# - What is the shortest, average and longest RunTime for the Movies?
# - What is the Movie that has the most popularity?
# - What is the most popular genres that we have in our dataset?

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# ### General Properties
# we can observe the characteristics of the dataset through:
# - number of rows in the dataset
# - number of columns in the dataset
# - features with missing values
# - duplicate rows in the the dataset
# - number of unique values in the dataset
# And here we can observe also that:
# - some columns are not useful in our analyst process exist in our dataset such as:
# (id,homepage, imdb_id, production_companies,popularity,tagline,keywords, overview, budget_adj,revenue_adj)
# 
# -- So we can omit these columns from our original dataset and built a new one that can be more effective and steady to help us in our analysing process.
# - Also we must change the format of the release_date column from object(str) to be datetime format.
# - We also notice that some columns have Zero Values such as (runtime, budjet, revenue), so we must discard these values.
# Let's begin our Cleaning process in the next fowllowing Cells.

# In[2]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df_mov= pd.read_csv('C:/Users/USER10/Desktop/NanoDegree Projects/final_project/TMDB movie data/tmdb-movies.csv')
df_mov.head()


# In[3]:


df_mov.info()


# In[4]:


# view number of duplicated rows
sum(df_mov.duplicated())


# In[5]:


# Drop duplicates in the dataset
df_mov.drop_duplicates(inplace= True)


# In[6]:


# Confirm Drop duplicates in the dataset
sum(df_mov.duplicated())


# In[7]:


# Removing unuseful columns from the dataset
# Create a list with the columns names that will be deleted
drop_col= ['id','imdb_id','popularity','production_companies','homepage','tagline','keywords','overview','budget_adj','revenue_adj']
# Dropping columns from dataset
df_mov= df_mov.drop(drop_col,1)
# View new dataset columns
df_mov.head(10)


# In[8]:


df_mov.shape


# In[9]:


# view missing value count for each feature
df_mov.isnull().sum()


# In[10]:


# Removing Zero Values from the new dataset for the columns [runtime, budjet, revenue] with NAN
df_mov['runtime']= df_mov['runtime'].replace(0,np.NAN)
df_mov['budget']= df_mov['budget'].replace(0,np.NAN)
df_mov['revenue']= df_mov['revenue'].replace(0,np.NAN)


# In[11]:


df_mov.drop_duplicates(inplace=True)


# In[12]:


drop_list= ['runtime','budget','revenue']
# Removing missing values
df_mov.dropna(subset= drop_list, inplace = True)
#df_mov.dropna(df_mov['budget'], inplace = True)
#df_mov.dropna(df_mov['revenue'], inplace = True)


# In[13]:


df_mov.shape


# In[14]:


# Changing the format of the release_date column from object(str) to be datetime format
df_mov.release_date= pd.to_datetime(df_mov['release_date'])


# In[15]:


# confirming datdtype changes
df_mov.info()


# In[16]:


# Preview the changes in release_date column
df_mov.head(2)


# 

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.
# 
# ### Research Question 1 (Which movie has the smallest and largest Budget? )
# For this question, we made some Exploratory for our dataset and obtain the followinf answers:
# we have two movies that have the smallest Budget : ("Lost & Found ", "Love, Wedding, Marriage") with 1 Dollar,  
# The Largest budget is for the Movie "The Warrior's Way" with (425000000) Dollars, 
# The average budget for all movies is (37203696.95) Dollars

# In[49]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
min_budget= df_mov['budget'].min()
max_budget= df_mov['budget'].max()
avg_budget= round(df_mov['budget'].mean(),2)
print(max_budget, min_budget, avg_budget, sep="\n")


# In[18]:


df_mov.loc[df_mov['budget'] == max_budget]


# In[19]:


df_mov.loc[df_mov['budget'] == min_budget]


# ### Research Question 2  (Which movie has the smallest and largest Revenue?)
# For this question, we made some Exploratory for our dataset and obtain the followinf answers:
# - we have two movies that have the smallest revenue : ("Shattered Glass", "Mallrats") with 2 Dollars.
# - The Largest revenue is for the Movie "Avatar" with (2.781506e+09) Dollars.
# - The average Revenue for all movies is (107686616.1) Dollars

# In[51]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.
min_revenue= df_mov['revenue'].min()
max_revenue= df_mov['revenue'].max()
avg_revenue= round(df_mov['revenue'].mean(),2)
print(min_revenue, max_revenue, avg_revenue, sep="\n")


# In[21]:


df_mov.loc[df_mov['revenue'] == min_revenue]


# In[22]:


df_mov.loc[df_mov['revenue'] == max_revenue]


# ### Research Question 3  (What is the shortest, average and longest RunTime for the Movies?)
# For this question, we made some Exploratory for our dataset and obtain the followinf answers:
# The average Runtime for all Movies is (109.22)
# The shortest Runtime is for the Movie ("Kid's Story") for runtime value = 15.0
# The Longest Runtime is for the Movie ("Carlos") for runtime value = 338.0
# 
# By looking at statical describtion for the runtime, we can say"
# - 25% of movies have a runtime less than 95 minutes.
# - 50% of movies have a runtime less than 106 minutes (close to mean 109.22)
# - 75% of movies have a runtime less than 119 minutes.

# In[23]:


df_mov['runtime'].describe()


# In[24]:


max_runtime= df_mov['runtime'].max()
avg_runtime= round(df_mov['runtime'].mean(),2)
min_runtime= df_mov['runtime'].min()
print(max_runtime,avg_runtime,min_runtime,sep="\n")


# In[25]:


df_mov.loc[df_mov['runtime'] == max_runtime]


# In[26]:


df_mov.loc[df_mov['runtime'] == min_runtime]


# ### Sice we don't have a spesific row for average runtime, we can make a graph for this column as the following:

# In[27]:


#plot a histogram of runtime of movies
plt.figure(figsize=(10,6), dpi = 100)
plt.xlabel('Movies Runtime', fontsize = 10)
plt.ylabel('Movies in the Dataset', fontsize= 10)
plt.title('Runtime For movies', fontsize= 10)
plt.hist(df_mov['runtime'], rwidth = 0.5, bins =30)
plt.show()


# ### So, we have a right skewed histogram that tell us the most runtime range is between (70 - 125) and we have more than 600 movies  exist in that range.

# 
# ### Research Question 4 (What is the Movie that has the most popularity?)
# To answer this question, we must look for the largest count of votting for the desired filme,
# The Movie that has the most popularity is ("Inception") with vote_count value = 9767.

# In[28]:


max_vote= df_mov['vote_count'].max()
print(max_vote)


# In[29]:


df_mov.loc[df_mov['vote_count'] == max_vote]


# ## Research Question 5 (What is the most popular genres that we have in our dataset?)
# #### Here we notice that the column Genres have multiple values in each row, and these values seperated with " | " character, so first we must store these values separatly then calculate each unique value to obtain the most genres in our dataset.
# #### After analysing the most popular genres in our dataset, we find that the genres "Drama" is the most popular with value of (1756)

# In[36]:


# separate values in each cell with "|"
genres_sep = df_mov['genres'].str.cat(sep = '|')
# storing values separated with "|" 
genres_kind = pd.Series(genres_sep.split('|'))
# count repetatiom for each uniqe values for genres
genres_count = genres_kind.value_counts()
# print the result
genres_count


# In[44]:


# plot genres count to show the most popular genres in a clear way:
genres_count.plot(kind='bar', title ="Most Popular Genres in our Movies DataSet", figsize=(15, 10), legend=True, fontsize=12)
plt.xlabel("Genres Kind", fontsize=12, color='g')
plt.ylabel("Genres Count", fontsize=12, color='g')
plt.show()


#  
#  ### we can also plot and find the relation between two variables, for example: relation between revenue and the release date for movies, Let's do that:

# In[46]:


# We will use bar plot for this analysis
# Here we want to know the revenue of movies for each year therefore we have to group all the movies in it's release year
year_revenue= df_mov.groupby('release_year')['revenue'].sum()
year_revenue.plot(kind='bar', title ="Relation Between Revenue and Year of Release", figsize=(15, 10), legend=True, fontsize=12)
plt.xlabel("Release Year", fontsize=12, color='g')
plt.ylabel("Renenue", fontsize=12, color='g')
plt.show()


# ### We notice that the relation between the two variables(Revenue, Release_year) is Positive, and the revenue is increasing by increasing the release year and all movies after the year 2010 have more big revenue, and the movies that have the highest revenue located in the year 2015. 

# In[31]:


year_revenue.idxmax()


# <a id='conclusions'></a>
# ## Conclusions
# > we made this analysis on our dataset after cleaning the data (omit some columns, delete duplicates and missing values), and obtain the results above, so we can say that dataset is somehow sufficiant to answer questions posed to be analysis but don't know if missing value have an impact if exists, for example: missing runtime may be longer than values we found, may be the missing budget or revenue bigger or smaller than the values that we found, so I think in the future if we have a complete data set without missing values, our results may differ from our existing analysis.
# 
# > Finally, after we finish our analysing for our Movies dataset, we can draw these conclusions:
# - The average budget for all movies is (37203696.95) Dollars
# - The average revenue for all movies is (107686616.1) Dollars
# - The average Runtime for all Movies is (109.22)
# - The genres "Drama" is the most popular with value of (1756)
# 
# -- So if we want to produce an amazing filme, we must give it a budget not less than (37203696.95) Dollars with Runtime not less than (110) minutes and the genres prefered are (Drama, Comedy, Thriller, Action).
# If we achive these elements, we expect to have a great filme with revenue not less than (107686616.1) Dollars.
# 
# 

# In[52]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

