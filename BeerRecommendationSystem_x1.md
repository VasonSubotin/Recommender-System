

    import pandas as pd
    import numpy as np
    import pylab as pl
    import os 


    os.chdir(r'E:\Andrey\Stanford\PythonClass')
    df=pd.read_csv("beer_reviews.csv")


    beer_1,beer_2="Dale's Pale Ale","Fat Tire Amber Ale"


    beer_1_reviewers=df[df.beer_name==beer_1].review_profilename.unique()
    beer_2_reviewers=df[df.beer_name==beer_2].review_profilename.unique()
    common_reviewers=set(beer_1_reviewers).intersection(beer_2_reviewers)
    

##Beer Recomendation system:
### If there is a beer you like and want some recomnedation for a style of beer to try, then the system will do it for you. How does it work?  There are three types of beer A,B,C. If Person 1 likes beer A and C, Person 2 likes beer A and C and You like beer C then: 
### You will also like beer A and you should be recommeneded beer A. In oredr to understand which beers are simlilar we are going to use "K nearest neighbors" approach.  
    


    (df[df.beer_name==beer_1].review_profilename).head()




    1442361            gskitt
    1444203    savannahbrooks
    1444401       mtstatebeer
    1449783       Monkeyknife
    1450412              dawg
    Name: review_profilename, dtype: object



### Get unique beer_names in the data


    df.beer_name.unique()




    array(['Sausa Weizen', 'Red Moon', 'Black Horse Black Beer', ...,
           'Baron Von Weizen', 'Resolution #2', "The Horseman's Ale"], dtype=object)



### Get the beer reviews for common users for a beer



    def get_beer_reviewrs(beer, common_users):
        mask=(df.review_profilename.isin(common_users))&(df.beer_name==beer)
        reviews=df[mask].sort('review_profilename')
        reviews=reviews[reviews.review_profilename.duplicated()==False]
        return reviews


    common_users=common_reviewers
    beer=beer_1
    mask=(df.review_profilename.isin(common_users)) & (df.beer_name==beer)


    reviews=df[mask].sort('review_profilename')
    


    reviews=reviews[reviews.review_profilename.duplicated()==False]


     (get_beer_reviewrs(beer_1,common_reviewers)).head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brewery_id</th>
      <th>brewery_name</th>
      <th>review_time</th>
      <th>review_overall</th>
      <th>review_aroma</th>
      <th>review_appearance</th>
      <th>review_profilename</th>
      <th>beer_style</th>
      <th>review_palate</th>
      <th>review_taste</th>
      <th>beer_name</th>
      <th>beer_abv</th>
      <th>beer_beerid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1454568</th>
      <td>2681</td>
      <td>Oskar Blues Grill &amp; Brew</td>
      <td>1221154773</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>ATPete</td>
      <td>American Pale Ale (APA)</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>Dale's Pale Ale</td>
      <td>6.5</td>
      <td>6518</td>
    </tr>
    <tr>
      <th>1453868</th>
      <td>2681</td>
      <td>Oskar Blues Grill &amp; Brew</td>
      <td>1297654968</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>AdamBear</td>
      <td>American Pale Ale (APA)</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>Dale's Pale Ale</td>
      <td>6.5</td>
      <td>6518</td>
    </tr>
    <tr>
      <th>1453766</th>
      <td>2681</td>
      <td>Oskar Blues Grill &amp; Brew</td>
      <td>1307229120</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>AlCaponeJunior</td>
      <td>American Pale Ale (APA)</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>Dale's Pale Ale</td>
      <td>6.5</td>
      <td>6518</td>
    </tr>
    <tr>
      <th>1454697</th>
      <td>2681</td>
      <td>Oskar Blues Grill &amp; Brew</td>
      <td>1210781469</td>
      <td>4.5</td>
      <td>3.5</td>
      <td>4.5</td>
      <td>AltBock</td>
      <td>American Pale Ale (APA)</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>Dale's Pale Ale</td>
      <td>6.5</td>
      <td>6518</td>
    </tr>
    <tr>
      <th>1454131</th>
      <td>2681</td>
      <td>Oskar Blues Grill &amp; Brew</td>
      <td>1267989965</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>Andreji</td>
      <td>American Pale Ale (APA)</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>Dale's Pale Ale</td>
      <td>6.5</td>
      <td>6518</td>
    </tr>
  </tbody>
</table>
</div>




    beer_1_reviews= get_beer_reviewrs(beer_1,common_reviewers)
    beer_2_reviews= get_beer_reviewrs(beer_2,common_reviewers)
    ALL_FEATURES=['review_overall','review_aroma','review_palate','review_taste']
    


    cols=['beer_name','review_profilename','review_overall','review_aroma','review_palate','review_taste']
    beer_2_reviews[cols].head()
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>beer_name</th>
      <th>review_profilename</th>
      <th>review_overall</th>
      <th>review_aroma</th>
      <th>review_palate</th>
      <th>review_taste</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202456</th>
      <td>Fat Tire Amber Ale</td>
      <td>ATPete</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>201458</th>
      <td>Fat Tire Amber Ale</td>
      <td>AdamBear</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>4.5</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>201886</th>
      <td>Fat Tire Amber Ale</td>
      <td>AlCaponeJunior</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>202481</th>
      <td>Fat Tire Amber Ale</td>
      <td>AltBock</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>201803</th>
      <td>Fat Tire Amber Ale</td>
      <td>Andreji</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




    from sklearn.metrics.pairwise import euclidean_distances


    
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


    f=ALL_FEATURES[2]
    print(f)
    euclidean_distances(beer_1_reviews[f],beer_2_reviews[f])[0][0]
    

    review_palate
    




    16.522711641858304




    euclidean_distances(beer_1_reviews[f],beer_2_reviews[f])




    array([[ 16.52271164]])




        beer_1_reviwers=df[df.beer_name==beer_1].review_profilename.unique()
        beer_2_reviwers=df[df.beer_name==beer_2].review_profilename.unique()
        common_reviewers=set(beer_1_reviwers).intersection(beer_2_reviwers)


    beer_1_reviwers




    array(['gskitt', 'savannahbrooks', 'mtstatebeer', ..., 'krausenman',
           'MrDonQuixote', 'jondeelee'], dtype=object)




    common_reviewers=set(beer_1_reviwers).intersection(beer_2_reviwers)


    calculate_similarity(beer_1,beer_2)




    [17.656443583009576,
     17.449928366615147,
     16.522711641858304,
     17.599715906798043]




    


    list1.append(1)
    list1




    [1]




    list1.append(2)
    list1




    [1, 2]




    beers_list=df.beer_name.unique()
    beers_list




    array(['Sausa Weizen', 'Red Moon', 'Black Horse Black Beer', ...,
           'Baron Von Weizen', 'Resolution #2', "The Horseman's Ale"], dtype=object)




    beers=["Dale's Pale Ale","Sierra Nevada Pale Ale","Michelob Ultra",
           "Natural Light","Bud Light","Fat Tire Amber Ale","Coors Light",
           "Blue Moon Belgian White","60 Minute IPA","Guinness Draught"]


    def task1(beer1,beers):
        #find common reviewrs
        empty_list=[]
        for i in range(len(beers)):
            #print(beers[i])
            #print(calculate_similarity(beer1,beers[i]))
            empty_list.append(calculate_similarity(beer1,beers[i]))
        print empty_list


    


    beers[1],beers[0],beers[7]




    ('Sierra Nevada Pale Ale', "Dale's Pale Ale", 'Blue Moon Belgian White')




    calculate_similarity(beer_1,beers[8])




    [17.832554500127006, 17.38533865071371, 16.568041525780892, 16.61324772583615]




    calculate_similarity("Sausa Weizen","Red Moon")




    [1.5, 0.5, 1.5, 1.5]




    task1(beers[0],beers)

    [[0.0, 0.0, 0.0, 0.0], [18.553975315279473, 15.771810295587505, 15.748015748023622, 16.201851746019649], [28.626910416599273, 30.504098085339287, 29.841246622753548, 31.519835024948971], [23.021728866442675, 25.865034312755125, 23.606143268225754, 26.186828750346997], [38.147739120424951, 40.574006457336694, 38.298172280149352, 41.590263283610021], [17.656443583009576, 17.449928366615147, 16.522711641858304, 17.599715906798043], [33.933759001914304, 38.275318418009277, 35.972211497209898, 38.584323241440948], [19.924858845171276, 18.953891421024867, 19.059118552545918, 20.790622886291789], [17.832554500127006, 17.38533865071371, 16.568041525780892, 16.61324772583615], [23.059705115200412, 24.305349205473266, 24.197107265125723, 24.964975465639856]]
    

## Find all euclidean distances for earch of beer pairs in beers list:




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
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>beer1</th>
      <th>beer2</th>
      <th>overall_dist</th>
      <th>aroma_dist</th>
      <th>palate_dist</th>
      <th>taste_dist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Dale's Pale Ale</td>
      <td>Sierra Nevada Pale Ale</td>
      <td>18.553975</td>
      <td>15.771810</td>
      <td>15.748016</td>
      <td>16.201852</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Dale's Pale Ale</td>
      <td>Michelob Ultra</td>
      <td>28.626910</td>
      <td>30.504098</td>
      <td>29.841247</td>
      <td>31.519835</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Dale's Pale Ale</td>
      <td>Natural Light</td>
      <td>23.021729</td>
      <td>25.865034</td>
      <td>23.606143</td>
      <td>26.186829</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dale's Pale Ale</td>
      <td>Bud Light</td>
      <td>38.147739</td>
      <td>40.574006</td>
      <td>38.298172</td>
      <td>41.590263</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dale's Pale Ale</td>
      <td>Fat Tire Amber Ale</td>
      <td>17.656444</td>
      <td>17.449928</td>
      <td>16.522712</td>
      <td>17.599716</td>
    </tr>
  </tbody>
</table>
</div>



###Weights are user inputs. As a person asking for recommendation, if I prefer to value taste over aroma, I will give higher weight to taste (less value of weight means more importance). This way the recommendation will be biased towards taste more than aroma.



    def calc_distance(dist,beer1,beer2,weights):
        mask=(dists.beer1==beer1)&(dists.beer2==beer2)
        row=dists[mask]
        row=row[['overall_dist','aroma_dist','palate_dist','taste_dist']]
        dist=weights*row
        return dist.sum(axis=1).tolist()[0]  
    


    weights=[2,1,1,1]
    dists=simple_distances
    beer1=beer_1
    beer2=beer_2
    


    mask=(dists.beer1==beer1)&(dists.beer2==beer2)
    row=dists[mask]
    row=row[['overall_dist','aroma_dist','palate_dist','taste_dist']]
    dist=weights*row
    row.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall_dist</th>
      <th>aroma_dist</th>
      <th>palate_dist</th>
      <th>taste_dist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>17.656444</td>
      <td>17.449928</td>
      <td>16.522712</td>
      <td>17.599716</td>
    </tr>
  </tbody>
</table>
</div>



### The final weighted values of euclidean distances calculated for each pair of the beer



    dist.head()
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall_dist</th>
      <th>aroma_dist</th>
      <th>palate_dist</th>
      <th>taste_dist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>35.312887</td>
      <td>17.449928</td>
      <td>16.522712</td>
      <td>17.599716</td>
    </tr>
  </tbody>
</table>
</div>




    dist.sum(axis=1).tolist()[0]




    86.885243081290639




    calc_distance(simple_distances,"Fat Tire Amber Ale","Dale's Pale Ale",weights)
    




    86.885243081290639




    calc_distance(simple_distances,"Fat Tire Amber Ale","Michelob Ultra",weights)




    153.00571860654327



### Let's make prediction for person having "Coors Light" beer



    my_beer="Coors Light"
    result=[]
    for b in beers:
        if my_beer!=b:
            result.append((my_beer,b,calc_distance(simple_distances,my_beer,b,weights)))
            

### The sorted list of sorted beers with clalculated euclidean distances


    sorted(result,key=lambda x:x[2])




    [('Coors Light', 'Natural Light', 70.483724369544859),
     ('Coors Light', 'Michelob Ultra', 71.312866260028784),
     ('Coors Light', 'Bud Light', 101.35815659584495),
     ('Coors Light', 'Blue Moon Belgian White', 174.68407232789718),
     ('Coors Light', 'Fat Tire Amber Ale', 175.74577705697465),
     ('Coors Light', "Dale's Pale Ale", 180.69937116048874),
     ('Coors Light', 'Guinness Draught', 204.99494753154124),
     ('Coors Light', '60 Minute IPA', 233.68501559769081),
     ('Coors Light', 'Sierra Nevada Pale Ale', 255.00673514359349)]



### The "Natural Light" beer should be recomended for a person who liked "Coors Light ", based on the histirical data.



    sorted(result,key=lambda x:x[2])[0][1]




    'Natural Light'




    
