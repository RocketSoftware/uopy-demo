####################################################################
# Copyright (C) Rocket Software 1993-2017
# Geocoding example: Calculate coordinates of a street address
# using Google MAPS API and response in JSON format
# Input is a "postal address" in the form of a human-readable address string and
# an indication whether the request comes from a device with a location sensor
# Response in JSON format contains an array of geocoded address information
# and geometry information. We are specifically interested in "lat" and "lng"
# values of the geometry location result.

import io as StringIO
from urllib.request import urlopen 
from urllib.parse import urlencode 
import json

class Point:
    def __init__ (self, lat=0, lng=0):
        self.lat = lat
        self.lng = lng

    def PointValue (self):
        lat_str = "%.7f" % self.lat
        lng_str = "%.7f" % self.lng
        return lat_str + ', ' + lng_str


class decodeAddressException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
        
def decodeAddressToGeocode( address ): 
    urlParams = {
        'address': address, 
        'sensor': 'false',
    }
    url = 'http://maps.google.com/maps/api/geocode/json?' + urlencode(urlParams)
    response = urlopen( url )
    responseBody = str(response.read(), encoding='UTF-8')
    body = StringIO.StringIO( responseBody )
    result = json.load( body )
    if 'status' not in result or result['status'] != 'OK':
        if 'status' not in result:
             raise decodeAddressException("Unknown error calling decodeAddressToGeocode")
        else:
             raise decodeAddressException("Error from decodeAddressToGeocode: " + result['status'])		
    else:
        #latitude,longitude
        coordinates = Point(result['results'][0]['geometry']['location']['lat'],\
        result['results'][0]['geometry']['location']['lng'])
        return coordinates
####################################################