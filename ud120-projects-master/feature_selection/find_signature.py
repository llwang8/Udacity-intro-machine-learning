#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]



### your code goes here

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
#pred = clf.predict(features_test)
#acc = accuracy_score(pred, labels_test)

print 'number of training points: ', len(features_train)
print 'accuracy: ', clf.score(features_test, labels_test)
#print 'acc:', acc
# number of training points:  150
# accuracy:  1.0  ???


#================================
# Quiz: Identify the Most Powerful Features
import numpy as np
#from sklearn.ensemble import ExtraTreesClassifier
#forest = ExtraTreesClassifier()
#forest.fit(features_train, labels_train)

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1][:41306]
print len(indices)
print importances[-1]

print 'Feature Ranking: '
for i in range(5):
    print '{} feature no. {} ({})'.format(i+1, indices[i], importances[indices[i]])

#Feature Ranking:
#1 feature no. 41306 (0.0) 31614 ???
#2 feature no. 13794 (0.0)
#3 feature no. 13772 (0.0)
#4 feature no. 13771 (0.0)
#5 feature no. 13770 (0.0)
#6 feature no. 13769 (0.0)
#7 feature no. 13768 (0.0)
#8 feature no. 13767 (0.0)
#9 feature no. 13766 (0.0)
#10 feature no. 13765 (0.0)

#================================
# Quiz: Use Tfldf to get the important features
print vectorizer.get_feature_names()[33614]
# result: u'sshacklensf' ???



