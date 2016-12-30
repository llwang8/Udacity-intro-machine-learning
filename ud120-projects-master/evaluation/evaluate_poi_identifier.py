#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn import svm

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print 'accuracy:', clf.score(features_test, labels_test)
print 'predict(features_test):'
print clf.predict(features_test)
#[ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.
#  0.  1.  0.  1.  0.  0.  0.  0.  0.  0.  0.]

print 'np.array(labels_test):'
print np.array(labels_test)
#[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.
#  0.  0.  0.  0.  1.  0.  1.  1.  0.  1.  0.]

#print 'num of POI predict:', clf.predict(features_test)
print 'num of POI predict:', len([e for e in labels_test if e == 1.0])
# result: 4

print 'num of tests:', len(labels_test)
#result: 29

# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print 1.0 - 4.0 / 29
# result: 1.0 - 5.0 / 29 = 0.8275862068965517

from sklearn.metrics import *
print 'precision:', precision_score(labels_test, clf.predict(features_test))
print 'recal:', recall_score(labels_test, clf.predict(features_test))



