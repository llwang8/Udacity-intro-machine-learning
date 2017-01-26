# Intro to Machine Learning
# Lesson.1: Naive Bayes

#===========================================

# Quiz: GaussianNB Deployment


# StudentMain.py

#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify

import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classify(features_train, labels_train)
clf.predict(features_test)


### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())


#----------------------------
# classifyNB.py

def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    from sklearn.naive_bayes import GaussianNB
    classifier =  GaussianNB()
    classifier.fit(features_train, labels_train)
    ###GaussianNB(priors=None)
    return classifier

#======================================

# Quiz: Calculating NB Accuracy

# classify.py
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    import numpy as np

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    #print pred

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module

    ### first method
    accuracy = accuracy_score(labels_test, pred)

    ### second method
    #pred = np.array(pred)
    #labels_train = np.array(labels_train)
    #accuracy = np.sum(pred == labels_train) / count(labels_train)
    return accuracy


# studentCode.py

from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy

# accuracy = 88.4%




