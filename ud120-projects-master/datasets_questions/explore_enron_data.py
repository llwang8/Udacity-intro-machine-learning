#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Size of the Enron Data
#print len(enron_data)
#146

# Features in the Enron_data
#print len(enron_data['GLISAN JR BEN F'].keys())
# 21

# Finding POIs in the Enron_data
#count = 0
#for e in enron_data:
#    if enron_data[e]['poi'] == 1:
#       count += 1
#print count
# 18

# How many POIs exist
#nmfile = open("../final_project/poi_names.txt")
#count = 0
#for line in nmfile:
#    if line[0] == "(" :
#        #nmdata = line.strip().split('\t')
#        count += 1
#print count
#nmfile.close()

# Problems with incomplete data


# Query the Dataset 1
#print enron_data['PRENTICE JAMES']['total_stock_value']
# 1095040

# Query the Dataset 2
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
# 11

# Query the Dataset 3
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Follow the money
#print enron_data['SKILLING JEFFREY K']['total_payments']
#print enron_data['LAY KENNETH L']['total_payments']
#print enron_data['FASTOW ANDREW S']['total_payments']
#8682716
#103559793
#2424083

# Quiz: Dealing with Unfilled Features
# NaN

#quantSalCnt = 0
#validEmailCnt = 0
#for e in enron_data:
#    if enron_data[e]['salary'] != 'NaN' and float(enron_data[e]['salary']):
#        quantSalCnt += 1
#    if enron_data[e]['email_address'] != 'NaN':
#        validEmailCnt += 1
#print quantSalCnt
#print validEmailCnt
#95
#111

# Quiz: Missing POIs 1
#count = 0
#for e in enron_data:
#    if enron_data[e]['total_payments'] == 'NaN':
#        count += 1
#print count / len(enron_data) * 100.00
# 21/146 for total E + F dataset

# Quiz: Missing POIs 2
count = 0
countPoi = 0
for e in enron_data:
    if enron_data[e]['poi'] == 1:
        countPoi += 1
        if enron_data[e]['total_payments'] == 'NaN':
            count += 1
print count
print countPoi
# 0 / 18 for POIs

# Quiz: Missing POIs 3


# Quiz: Age/Net worth regression
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(ages_train, net_worths_train)

    return reg

#!/usr/bin/python

import numpy
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from studentRegression import studentReg
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()



reg = studentReg(ages_train, net_worths_train)


plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")


plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())

# Now You practice extracting
# regressionQuiz.py
import numpy
import matplotlib.pyplot as plt

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

### get Katie's net worth (she's 27)
### sklearn predictions are returned in an array, so you'll want to index into
### the output to get what you want, e.g. net_worth = predict([[27]])[0][0] (not
### exact syntax, the point is the [0] at the end). In addition, make sure the
### argument to your prediction function is in the expected format - if you get
### a warning about needing a 2d array for your data, a list of lists will be
### interpreted by sklearn as such (e.g. [[27]]).

km_net_worth = reg.predict([[27]])[0][0]### fill in the line of code to get the right value

### get the slope
### again, you'll get a 2-D array, so stick the [0][0] at the end
slope = reg.coef_[0][0] ### fill in the line of code to get the right value

### get the intercept
### here you get a 1-D array, so stick [0] on the end to access
### the info we want
intercept = reg.intercept_[0]### fill in the line of code to get the right value


### get the score on test data
test_score = reg.score(ages_test, net_worths_test) ### fill in the line of code to get the right value

### get the score on the training data
training_score = reg.score(ages_train, net_worths_train) ### fill in the line of code to get the right value

def submitFit():
    # all of the values in the returned dictionary are expected to be
    # numbers for the purpose of the grader.
    return {"networth":km_net_worth,
            "slope":slope,
            "intercept":intercept,
            "stats on test":test_score,
            "stats on training": training_score}

# age_net_worths.py
import numpy
import random

def ageNetWorthData():

    random.seed(42)
    numpy.random.seed(42)

    ages = []
    for ii in range(100):
        ages.append( random.randint(20,65) )
    net_worths = [ii * 6.25 + numpy.random.normal(scale=40.) for ii in ages]
### need massage list into a 2d numpy array to get it to work in LinearRegression
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    from sklearn.cross_validation import train_test_split
    ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths)

    return ages_train, ages_test, net_worths_train, net_worths_test

#"slope": 6.4735495495770605, "stats on training": 0.87458823582171863, "intercept": -14.353783307755634, "stats on test": 0.81236572923084704, "networth": 160.43205453082501}





