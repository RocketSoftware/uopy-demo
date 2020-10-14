################################################################
# Copyright (C) Rocket Software 1993-2017
# Calculate the distance between two points on Earth
# assuming it is a perfect sphere
# using Haversine formula

from math import radians, cos, sin, asin, sqrt

def distanceBetweenPoints(point1, point2): 
    # convert degrees to radians
    lat1 = float(point1.lat)
    lat2 = float(point2.lat)
    lng1 = float(point1.lng)
    lng2 = float(point2.lng)
    # Switch to radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lng1 = radians(lng1)
    lng2 = radians(lng2)

    dlat = lat2 - lat1 
    dlng = lng2 - lng1
    a = sin(dlat/2) * sin(dlat/2)
    b = cos(lat1) * cos(lat2) * sin(dlng/2) * sin(dlng/2)
    c = a + b
    d = 2 * asin(sqrt(c)) 

    # Compute based on radius of earth in miles
    e = 3960 * d

    return e
#############################################################