#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Get geo-location. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import geocoder
import socket
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
print(f'{g.latlng}')

geoLoc = Nominatim(user_agent="GetLoc")
locname = geoLoc.reverse(str(g.latlng[0]) + "," + str(g.latlng[1]))

location = locname.address.split(',')
print(f'{location[2].strip()}')

print(f'{socket.gethostname()}')
# TODO Combine with weather API and build a site