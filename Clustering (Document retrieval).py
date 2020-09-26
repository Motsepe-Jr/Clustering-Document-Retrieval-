#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import graplab


# In[ ]:


#Loading dataset from wikipedia, pages on people
people = graphlab.Sframe('people_wiki.gl')


# In[ ]:


people.head()


# In[ ]:


# Explore the dataset, and checkout the texts contains


# In[ ]:


obama = people[people['name'] == 'Barak Obama']


# In[ ]:


obama['text']


# In[ ]:


clooney = people[people['name'] == 'George Clooney']


# In[ ]:


# explore words count


# In[ ]:


obama['word_count'] = graphlab.text_analytics.count_words(obama['text'])


# In[ ]:


obama['words_ccount']


# In[ ]:


#Sort the words cccount for the obama article


# In[ ]:


obama_words_count_table = obama[['obama_count']].stack('word_count', new_coloum_name = ['word', 'count']) # create a table


# In[ ]:


obama_words_count_table.sort_values('count', ascending= False) # words such as "the, a. and" are not informative


# In[ ]:


# compute and explore tf-idfs for corpus


# In[ ]:


people['words_count'].graphlab.text_analytics.count_words(people['text'])


# In[ ]:


tfidf = graphlab.text_analytics.tf_idf(people['word_count'])


# In[ ]:


tfidf


# In[ ]:


people["tfidf"] = tfidf['docs']


# In[ ]:


# Examine TF-IDF for obama article


# In[ ]:


obama = people[people['name'] == 'Barak Obama']


# In[ ]:


obama_tfidf_table = obama[["tfidf"]].stack('tfidf',  
                                           new_coloum_name = ['word', 'tfidf']).sort_values(column='tfidf', 
                                                                                            ascending =False)
#tfidf = removes all the words which are not important such as "the, a, and"


# In[ ]:


# manaually compute distances between a few people


# In[ ]:


clinton = people[people['name'] == 'Bill Clinton']


# In[ ]:


Beckham = people[poeple['name'] == 'David Beckham']


# In[ ]:


# Is Obama close to clinton than Beckham


# In[ ]:


graphlab.distance.cosine[obama["tfidf"][0], clinton["tfidf"][0]] # take note that the less cosine, the moe obama is close the person


# In[ ]:


graphlab.distance.cosine[obama["tfidf"][0], Beckham["tfidf"][0]] # the higher the cosine, the person is not close to beckham


# In[ ]:


## Building the nearest neighbor model for wikipedia articles


# In[ ]:


knn_model = graphlab.nearest_neighbor.create(people, features= ['tfidf'], label='name') # the label return the name of the person


# In[ ]:


# applying the nearest model for retrieval


# In[ ]:


# who is close to obama


# In[ ]:


knn_model.query(obama)


# In[ ]:


# other example of document retrieval


# In[ ]:


swift = people[people['name'] == 'Taylor Swift']


# In[ ]:


knn_model.query(swift)


# In[ ]:


jolie = people[people['name'] == 'Angelina Jolie']


# In[ ]:


knn_model.query(swift)


# In[ ]:





# In[ ]:




