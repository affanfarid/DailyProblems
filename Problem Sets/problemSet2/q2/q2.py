'''
strat:
loop through each query in queries and have a finalArr,
add the result of the operation of each query to finalArr

loop through cities (exclude the current one)
compare the distance, have a current smallest distance 

have cases if its equal 


'''

import math
import sys

def distance(x1,y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
    #return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

def closestCity(cities, xCoordinates, yCoordinates, queryIndex):
    #the initial index is set to None
    shortestCityIndex = None
    #the initial shortDistance is set to the maximum value
    shortestCityDistance = sys.maxint
    #saved the query coordinates for easier use
    qX = xCoordinates[queryIndex]
    qY = yCoordinates[queryIndex]
    
    #loop through the rest of the cities to check for shortest distance
    for cityIndex in range(len(cities)):
        #cant perform operation on self
        if cityIndex == queryIndex:
            continue
        #can only compare if it matches the x or y coordinate
        if qX == xCoordinates[cityIndex] or qY == yCoordinates[cityIndex]:
            #gets the current Distance
            currDist = distance(qX, qY,  xCoordinates[cityIndex], yCoordinates[cityIndex] )
            #if there is a closer city
            if currDist < shortestCityDistance:
                shortestCityIndex = cityIndex
                shortestCityDistance = currDist
            #if there are cities of equal distance
            if currDist == shortestCityDistance:
                #alphabetically smaller name
                if cities[cityIndex] < cities[shortestCityIndex]:
                    shortestCityIndex = cityIndex
                    shortestCityDistance = currDist
                
                    
    
    if shortestCityIndex == None:
        return "NONE"
    else:
        return cities[shortestCityIndex]
            
    
    


def closestStraightCity(numOfCities, cities, xCoordinates, yCoordinates, 
                        numOfQueries, queries):
    #the final array to be returned                       
    finalArr = []
    
    #loops through all queries
    for x in queries:
        #gets the city index of that query 
        indx = cities.index(x)
        #adds the return value of the helper function to the final array in the right order
        finalArr.append( closestCity(cities, xCoordinates, yCoordinates, indx) )
    
    return finalArr

    
    
    
    
    
    
    
    
    
    
    