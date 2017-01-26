#!/usr/bin/python

# Intro to Machine Learning
# Features Scaling

# Quiz: Min/Max Rescaler Coding

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    scale = []
    amax = max(arr)
    amin = min(arr)

    if amax == amin:
        for i in range(0, len(arr)):
            scale.append(0.5)
    else:
        for e in arr:
            if e == amax:
                scale.append(1)
            elif e == amin:
                scale.append(0)
            else:
                s = float(e-amin) / float(amax-amin)
                scale.append(s)

    return scale

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

def featureScaling_sklearn(arr):
    import numpy
    from sklearn.preprocessing import MinMaxScaler
    weights = numpy.array([[115.], [140.], [175.]])
    scaler = MinMaxScaler()
    rescaled_weight = scaler.fit_transform(weights)
    return rescaled_weight


