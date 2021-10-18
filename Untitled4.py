#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize'] = [11, 7]
office_df= pd.read_csv("datasets/office_episodes.csv")
office_df.head()
cols=[]
for ind,row in office_df.iterrows():
    if (row["scaled_ratings"] <  0.25  ):
        cols.append("red")
    elif   (row["scaled_ratings"] <  0.50  ):
        cols.append("orange") 
        
    elif   (row["scaled_ratings"] <  0.75  ):
        cols.append("lightgreen")  
        
    else :
    
        cols.append("darkgreen") 
        
        
sizes=[]
for ind,row in office_df.iterrows():
    if (row["has_guests"] ==False  ):
        sizes.append(25)
    else:
        sizes.append(250)

fig=plt.figure()
plt.scatter(x=office_df["episode_number"],y=office_df["viewership_mil"],c=cols,s=sizes)

plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.show()
cols=[]
office_df[office_df['viewership_mil']==office_df['viewership_mil'].max]['guest_stars']
top_star="Jack Black"


# In[ ]:




