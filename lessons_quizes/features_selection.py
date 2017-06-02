#!/usr/bin/python

# Intro to Machine Learning
# Features Selecting

#============================
# 3. Quiz: A New Enron Features


###
### in poiFlagEmail() below, write code that returns a boolean
### indicating if a given email is from a POI
###

import sys
import reader
import poi_emails

def getToFromStrings(f):
    '''
    The imported reader.py file contains functions that we've created to help
    parse e-mails from the corpus. .getAddresses() reads in the opening lines
    of an e-mail to find the To: From: and CC: strings, while the
    .parseAddresses() line takes each string and extracts the e-mail addresses
    as a list.
    '''
    f.seek(0)
    to_string, from_string, cc_string   = reader.getAddresses(f)
    to_emails   = reader.parseAddresses( to_string )
    from_emails = reader.parseAddresses( from_string )
    cc_emails   = reader.parseAddresses( cc_string )

    return to_emails, from_emails, cc_emails


### POI flag an email

def poiFlagEmail(f):
    """ given an email file f,
        return a trio of booleans for whether that email is
        to, from, or cc'ing a poi """

    to_emails, from_emails, cc_emails = getToFromStrings(f)

    ### poi_emails.poiEmails() returns a list of all POIs' email addresses.
    poi_email_list = poi_emails.poiEmails()

    to_poi = False
    from_poi = False
    cc_poi   = False

    ### to_poi and cc_poi are related functions, which flag whether
    ### the email under inspection is addressed to a POI, or if a POI is in cc
    ### you don't have to change this code at all

    ### there can be many "to" emails, but only one "from", so the
    ### "to" processing needs to be a little more complicated
    if to_emails:
        ctr = 0
        while not to_poi and ctr < len(to_emails):
            if to_emails[ctr] in poi_email_list:
                to_poi = True
            ctr += 1
    if cc_emails:
        ctr = 0
        while not to_poi and ctr < len(cc_emails):
            if cc_emails[ctr] in poi_email_list:
                cc_poi = True
            ctr += 1


    #################################
    ######## your code below ########
    ### set from_poi to True if #####
    ### the email is from a POI #####
    #################################
    if from_emails and from_emails[0] in poi_email_list:
        from_poi = True

    #################################
    return to_poi, from_poi, cc_poi



#============================
# 4. Quiz: Visualizing Your New Features

import pickle
from get_data import getData

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator)
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """


    ### you fill in this code, so that it returns either
    ###     the fraction of all messages to this person that come from POIs
    ###     or
    ###     the fraction of all messages from this person that are sent to POIs
    ### the same code can be used to compute either quantity

    ### beware of "NaN" when there is no known email address (and so
    ### no filled email features), and integer division!
    ### in case of poi_messages or all_messages having "NaN" value, return 0.
    fraction = 0.
    if poi_messages != 'NaN' and all_messages != 'NaN':
        fraction = float(poi_messages) / float(all_messages)

    return fraction


data_dict = getData()
print data_dict['ELLIOTT STEVEN']

submit_dict = {}
for name in data_dict:

    data_point = data_dict[name]

    print
    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = computeFraction( from_poi_to_this_person, to_messages )
    print fraction_from_poi
    data_point["fraction_from_poi"] = fraction_from_poi


    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = computeFraction( from_this_person_to_poi, from_messages )
    print fraction_to_poi
    data_point["fraction_to_poi"] = fraction_to_poi

    submit_dict[name]={"from_poi_to_this_person":fraction_from_poi,
                       "from_this_person_to_poi":fraction_to_poi}



#####################

def submitDict():
    return submit_dict




