#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    #print 'starting clean read data to tuple'
    #print 'length:', len(predictions)
    ### your code goes here
    for i in range(0, len(predictions)):
        age = ages[i][0]
        net_worth = net_worths[i][0]
        pred = predictions[i][0]
        err = net_worth - pred

        cleaned_data.append((age, net_worth, err))

    #print 'length of cleaned_data before sort:', len(cleaned_data)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=True)[0:81]
    #print cleaned_data[-1]

    print 'length of cleaned_data:', len(cleaned_data)
    return cleaned_data

