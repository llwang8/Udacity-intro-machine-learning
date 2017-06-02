#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='rbf', C=10000)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"
accuracy = accuracy_score(pred, labels_test)

print accuracy

#print "pred 10th:", pred[10]
#print "pred 26th:", pred[26]
#print "pred 50th:", pred[50]

print "num for Chris:", sum(pred)
print "num for Sara:", len(pred)-sum(pred)


#-------------------------------------------
# full trainin gdataset with linear kernel
# 0.984072810011

# 1% training dataset with linear kernel
# training time: 0.095 s
# predict time: 1.002 s
# 0.884527872582

# 1% training dataset with rbf kernel
# training time: 0.113 s
# predict time: 1.132 s
# 0.616040955631

# 1% training dataset with rbf kernel (C=10)
# training time: 0.112 s
# predict time: 1.145 s
# 0.616040955631

# 1% training dataset with rbf kernel (C=100)
#training time: 0.115 s
#predict time: 1.132 s
#0.616040955631

# 1% training dataset with rbf kernel (C=1000)
# training time: 0.11 s
# predict time: 1.08 s
# 0.821387940842

# 1% training dataset with rbf kernel (C=10000)
# training time: 0.109 s
# predict time: 0.924 s
# 0.892491467577

# full trainin gdataset with rbf kernel (C=10000)
# training time: 108.159 s
# predict time: 10.772 s
# 0.990898748578

# 1% training dataset with rbf kernel (C=10000)
# pred 10th: 1
# pred 26th: 0
# pred 50th: 1
# training time: 0.113 s
# predict time: 0.979 s
# 0.892491467577

# full training dataset with rbf kernel (C=10000)
# training time: 105.053 s
# predict time: 10.576 s
# num for Chris: 877
# num for Sara: 881
# 0.990898748578

#########################################################


