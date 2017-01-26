# Intro to Machine Learning
# Lesson.4: SVM

#===========================================

# Quiz: Coding a Decision Tree

# studentMain.py
#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

clf.predict(features_test)

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())


# classifyDT.py
def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)

    return clf


# In general, this is the shape that is going to characterize a
# decision tree or decision tree boundary.  There's some sign of
# overfitting, perhaps in this example the long slices.


#----------------------------------
#Quiz: Decision Tree Accuracy

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

#################################################################################

########################## DECISION TREE #################################
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)

### be sure to compute the accuracy on the test set
def submitAccuracies():
  return {"acc":round(acc,3)}


#{"message": "{'acc': 0.908}"}

#---------------------------------
# Quiz: Desision Tree Accuracy (min_sample_split)
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## DECISION TREE #################################

### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split = 2)
clf.fit(features_train, labels_train)
acc_min_samples_split_2 = accuracy_score(clf.predict(features_test), labels_test)

clf = tree.DecisionTreeClassifier(min_samples_split = 50)
clf.fit(features_train, labels_train)
acc_min_samples_split_50 = accuracy_score(clf.predict(features_test), labels_test)


def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}

{"message": "{'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}"}



#--------------------------------------
