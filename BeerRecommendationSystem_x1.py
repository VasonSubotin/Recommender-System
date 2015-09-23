
# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np
import pylab as pl
import os 


# In[20]:

os.chdir(r'E:\Andrey\Stanford\PythonClass')
df=pd.read_csv("beer_reviews.csv")


# In[21]:

beer_1,beer_2="Dale's Pale Ale","Fat Tire Amber Ale"


# In[22]:

beer_1_reviewers=df[df.beer_name==beer_1].review_profilename.unique()
beer_2_reviewers=df[df.beer_name==beer_2].review_profilename.unique()
common_reviewers=set(beer_1_reviewers).intersection(beer_2_reviewers)


# ##Beer Recomendation system:
# ### If there is a beer you like and want some recomnedation for a style of beer to try, then the system will do it for you. How does it work?  There are three types of beer A,B,C. If Person 1 likes beer A and C, Person 2 likes beer A and C and You like beer C then: 
# ### You will also like beer A and you should be recommeneded beer A. In oredr to understand which beers are simlilar we are going to use "K nearest neighbors" approach.  
#     

# In[23]:

(df[df.beer_name==beer_1].review_profilename).head()


# ### Get unique beer_names in the data

# In[24]:

df.beer_name.unique()


# ### Get the beer reviews for common users for a beer
# 

# In[25]:

def get_beer_reviewrs(beer, common_users):
    mask=(df.review_profilename.isin(common_users))&(df.beer_name==beer)
    reviews=df[mask].sort('review_profilename')
    reviews=reviews[reviews.review_profilename.duplicated()==False]
    return reviews


# In[31]:

common_users=common_reviewers
beer=beer_1
mask=(df.review_profilename.isin(common_users)) & (df.beer_name==beer)


# In[32]:

reviews=df[mask].sort('review_profilename')


# In[52]:

reviews=reviews[reviews.review_profilename.duplicated()==False]


# In[74]:

(get_beer_reviewrs(beer_1,common_reviewers)).head()


# In[38]:

beer_1_reviews= get_beer_reviewrs(beer_1,common_reviewers)
beer_2_reviews= get_beer_reviewrs(beer_2,common_reviewers)
ALL_FEATURES=['review_overall','review_aroma','review_palate','review_taste']


# In[39]:

cols=['beer_name','review_profilename','review_overall','review_aroma','review_palate','review_taste']
beer_2_reviews[cols].head()


# In[40]:

from sklearn.metrics.pairwise import euclidean_distances


# In[41]:


def calculate_similarity(beer1,beer2):
    #find common reviewrs
    beer_1_reviewers=df[df.beer_name==beer1].review_profilename.unique()
    beer_2_reviewers=df[df.beer_name==beer2].review_profilename.unique()
    
    #find users who reviewed beer1 and beer2  
    common_reviewers=set(beer_1_reviewers).intersection(beer_2_reviewers)

    #get reviews for beer1 and beer2
    beer_1_reviwers=get_beer_reviewrs(beer1,common_reviewers)
    beer_2_reviwers=get_beer_reviewrs(beer2,common_reviewers)
    dists=[]
    #find the euclidean distances between beer1 and beer2 
    for f in ALL_FEATURES:
        dists.append(euclidean_distances(beer_1_reviwers[f],beer_2_reviwers[f])[0][0])
    return dists


# In[42]:

f=ALL_FEATURES[2]
print(f)
euclidean_distances(beer_1_reviews[f],beer_2_reviews[f])[0][0]


# In[309]:

euclidean_distances(beer_1_reviews[f],beer_2_reviews[f])


# In[310]:

beer_1_reviwers=df[df.beer_name==beer_1].review_profilename.unique()
beer_2_reviwers=df[df.beer_name==beer_2].review_profilename.unique()
common_reviewers=set(beer_1_reviwers).intersection(beer_2_reviwers)


# In[311]:

beer_1_reviwers


# In[312]:

common_reviewers=set(beer_1_reviwers).intersection(beer_2_reviwers)


# In[313]:

calculate_similarity(beer_1,beer_2)


# In[ ]:




# In[315]:

list1.append(1)
list1


# In[316]:

list1.append(2)
list1


# In[44]:

beers_list=df.beer_name.unique()
beers_list


# In[45]:

beers=["Dale's Pale Ale","Sierra Nevada Pale Ale","Michelob Ultra",
       "Natural Light","Bud Light","Fat Tire Amber Ale","Coors Light",
       "Blue Moon Belgian White","60 Minute IPA","Guinness Draught"]


# In[46]:

def task1(beer1,beers):
    #find common reviewrs
    empty_list=[]
    for i in range(len(beers)):
        #print(beers[i])
        #print(calculate_similarity(beer1,beers[i]))
        empty_list.append(calculate_similarity(beer1,beers[i]))
    print empty_list


# In[ ]:




# In[47]:

beers[1],beers[0],beers[7]


# In[48]:

calculate_similarity(beer_1,beers[8])


# In[49]:

calculate_similarity("Sausa Weizen","Red Moon")


# In[52]:

task1(beers[0],beers)


# ## Find all euclidean distances for earch of beer pairs in beers list:
# 
# 

# In[61]:

def task2(beers):
    #find common reviewrs
    simple_list=[]
    for beer1 in beers:
        #print(beer1)
        for beer2 in beers:
            #print(beer1+'-'+beer2)
            if beer1!=beer2:
                row=[beer1,beer2]+calculate_similarity(beer1,beer2)
                #print(row)
                #print("")
                simple_list.append(row)
                
    return(simple_list)
simple_distances=task2(beers)
simple_distances
cols=["beer1","beer2","overall_dist","aroma_dist","palate_dist","taste_dist"]
simple_distances=pd.DataFrame(simple_distances,columns=cols)
simple_distances.head()


# ###Weights are user inputs. As a person asking for recommendation, if I prefer to value taste over aroma, I will give higher weight to taste (less value of weight means more importance). This way the recommendation will be biased towards taste more than aroma.
# 

# In[60]:

def calc_distance(dist,beer1,beer2,weights):
    mask=(dists.beer1==beer1)&(dists.beer2==beer2)
    row=dists[mask]
    row=row[['overall_dist','aroma_dist','palate_dist','taste_dist']]
    dist=weights*row
    return dist.sum(axis=1).tolist()[0]  


# In[62]:

weights=[2,1,1,1]
dists=simple_distances
beer1=beer_1
beer2=beer_2


# In[63]:

mask=(dists.beer1==beer1)&(dists.beer2==beer2)
row=dists[mask]
row=row[['overall_dist','aroma_dist','palate_dist','taste_dist']]
dist=weights*row
row.head()


# ### The final weighted values of euclidean distances calculated for each pair of the beer
# 

# In[64]:

dist.head()


# In[65]:

dist.sum(axis=1).tolist()[0]


# In[66]:

calc_distance(simple_distances,"Fat Tire Amber Ale","Dale's Pale Ale",weights)


# In[67]:

calc_distance(simple_distances,"Fat Tire Amber Ale","Michelob Ultra",weights)


# ### Let's make prediction for person having "Coors Light" beer
# 

# In[68]:

my_beer="Coors Light"
result=[]
for b in beers:
    if my_beer!=b:
        result.append((my_beer,b,calc_distance(simple_distances,my_beer,b,weights)))
        


# ### The sorted list of sorted beers with clalculated euclidean distances

# In[70]:

sorted(result,key=lambda x:x[2])


# ### The "Natural Light" beer should be recomended for a person who liked "Coors Light ", based on the histirical data.
# 

# In[73]:

sorted(result,key=lambda x:x[2])[0][1]


# In[ ]:



