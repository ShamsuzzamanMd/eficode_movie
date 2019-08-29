#!/usr/bin/env python
# coding: utf-8

# In[30]:


# required dependencise (packages)

#import numpy as np
#import pandas as pd
#from pandas import Series, DataFrame
#import matplotlib.pyplot as plt
#%matplotlib inline
#import seaborn as sns
#import warnings
#warnings.filterwarnings('ignore')


# In[2]:


# featuring the data set

column_names= ['MovieID','Title','Genre']
df=pd.read_csv('movies.dat',header= None, names=column_names,sep='::',encoding='latin-1')


# In[3]:


# data view

df.head(5)


# In[4]:


# slicing

df['Title']=df['Title'].str.slice(0,-7)


# In[5]:


# view

df.head()


# In[6]:


# Split genres and create a new entry for each of the genre a movie falls into

g = df['Genre'].str.split('|').apply(Series, 1).stack()
g.index = g.index.droplevel(-1)
g.name = 'Genre'
del df['Genre']
df_spliting_gen = df.join(g)


# In[7]:


# data view

df_spliting_gen.head()


# In[29]:


# missing value checking

#df_spliting_gen.isnull().sum() # no missing values


# In[ ]:





# In[8]:


names=['UserId', 'MovieID','Rating','Timestamp']
df2=pd.read_csv('ratings.dat',header= None, names=names,sep='::')


# In[9]:


# data view

df2.head()


# In[ ]:


# missing value checking

#df2.isnull().sum() # no missing values


# In[ ]:





# In[10]:


# data set featuring

cl_name=['UserId','Gender','Age','Occupation','Zipcode']
df3=pd.read_csv('users.dat',header= None, names=cl_name,sep='::')


# In[11]:


#data view

df3.head()


# In[ ]:


# missing value checking

#df3.isnull().sum() # no missing values


# In[ ]:





# In[12]:


# data sets merging

df_new= pd.merge(df2,df3,how='inner', on='UserId')


# In[13]:


# data view

df_new.head()


# In[14]:


# data sets merging

Movie_Data=pd.merge(df_new,df_spliting_gen, how='inner',on='MovieID')
Movie_Data.drop_duplicates(inplace=True)


# In[15]:


# more info of the data set

Movie_Data.info()


# In[16]:


# Statistical analysis

#Movie_Data.describe()


# In[17]:


Movie_Data.head()


# In[18]:


# Best Rated Movie
md=Movie_Data[['Title', 'Rating']].sort_values(by=['Rating'], ascending=False)
md.drop_duplicates(inplace=True)


# In[19]:


# checking after duplicate removing

md.head()


# In[20]:


# ploting 

plt.figure(figsize=(12,8))
Movie_Data[['Rating','Title']].groupby('Rating').count().plot(kind='bar', title='Content Rating Visualization')
plt.xlabel('Content Rating')
plt.ylabel('Title Count')
plt.show()


# In[21]:


# longest movie

Movie_Data[['Title','Timestamp']].sort_values(by=['Timestamp'], ascending=False).head(5)


# In[22]:


# Average duration of the movie

mean_duration =round(Movie_Data['Timestamp'].mean(),3)/60
print("Average value of duration is {} sec.".format(mean_duration))


# In[23]:


# Occupation and Genre

Movie_Data[['Occupation','Genre']].sort_values(by=['Genre'], ascending=False).head(5)


# In[24]:


# Age and Genre

Movie_Data[['Age','Genre']].sort_values(by=['Age'], ascending=False).head()


# In[25]:


# create a histogram of duration

plt.figure(figsize=(12,8))
Movie_Data['Timestamp'].plot(kind='hist', bins=20)
plt.show()


# In[28]:


# plotting 

plt.figure(figsize=(20,8))
sns.barplot(x='Genre',y='Age',data=Movie_Data)
plt.show()


# In[27]:


# plotting (Gender and Rating)

plt.figure(figsize=(12,8))
sns.barplot(x='Gender',y='Rating', data=Movie_Data)
plt.show()

