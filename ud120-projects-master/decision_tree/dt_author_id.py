#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
from sklearn import tree
from sklearn.metrics import accuracy_score

print features_train.shape[1]
#print features_train.shape()
print len(features_train[0])

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print acc

# 0.978953356086 for selector percentile=10

# 0.966439135381 for selector percentile=1

# 0.911262798635 for selector percentile=0.1

#########################################################


