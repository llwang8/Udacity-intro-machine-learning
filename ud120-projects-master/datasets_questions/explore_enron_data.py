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
#  for POIs
