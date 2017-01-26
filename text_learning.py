#!/usr/bin/python

# Intro to Machine Learning
# Features Scaling




# Bag of Words in Sklearn

#from sklearn.feature_extraction import CountVectorizer

#vectorizer = CountVectorizer()
#str1 = ''
#str2 = ''
#str3 = ''
#email_list = [str1, str2, str3]
#bag_of_words = vectorizer.fit(email_list)
#bag_of_words = vectorizer.transform(email_list)

#print vectorizer.get('great')




# Getting stopwords from NLTK
# first nltk.download() at command line
#import nltk
from nltk.corpus import stopwords

sw = stopwords.words('english')
print 'Num of stopwords:', len(sw)
