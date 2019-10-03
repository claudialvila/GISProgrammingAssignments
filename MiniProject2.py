# -*- coding: utf-8 -*-
"""
GIS 5103
Dr. Johnson
Mini Project 2
Morgan Runion and Claudia Vila

"""
import geopy
from geopy.geocoders import Nominatim
from geopy import distance

# instantiate the geocoder
geolocator = Nominatim(user_agent="mrunion@fsu.edu") 

# geocode a location
location = geolocator.geocode("Tallahassee, FL")

# get distance between two locations
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
dist = distance.distance(newport_ri, cleveland_oh)
print (dist)
print (location)

location_lat = location.latitude
location_long = location.longitude

#Question 2

print (location.latitude,location.longitude)

print (dist.miles) 
print (dist.kilometers) 

print (" ")

#Question 3

cities = ['Tallahassee, FL', 'Orlando, FL', 'Panama City Beach, FL', 'Atlanta, GA', 'Seattle, WA', 'Austin, Tx', 'Chicago, Il', 'New Orleans, LA']
geocoded_cities = []
for city in cities:
    geocoded_cities.append(geolocator.geocode(city))

for city in geocoded_cities:
    print(city[0], city[1])
    
print (" ")    
    
#Question 4
cities_dict = {}
for city in cities:
    geocoded = geolocator.geocode(city)
    cities_dict[geocoded[0]] = geocoded[1]

print (" ")

#Question 5
city_distances = []
for city_a in cities_dict.items():
    distances = []
    for city_b in cities_dict.items():
        distances.append(distance.distance(city_a[1], city_b[1]).miles)
    city_distances.append([city_a[0], distances])
    
print(city_distances)
print (" ")

#Question 6
city_distances_rnd = []
for city_a in cities_dict.items():
    distances_long = []
    for city_b in cities_dict.items():
        distances_long.append(distance.distance(city_a[1], city_b[1]).miles)
        distances_rnd = []
        for value in distances_long:
            if value >= 1000:
                distances_rnd.append(round(value, 1))
            elif value >= 100:
                distances_rnd.append(round(value, 2))
            else:
                distances_rnd.append(round(value, 3))
    city_distances_rnd.append([city_a[0], distances_rnd])
