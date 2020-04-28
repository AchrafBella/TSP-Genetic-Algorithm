# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:34:24 2020

@author: Supernova
"""
from City import City
import numpy as np
import random

class Rout():
    def __init__(self, cities):
        self.__cities = random.sample(cities, len(cities))
        self.__fitness  = 0
        self.__distance = 0
        pass

    # getters and setter    
    def getCities(self):
        return self.__cities
    
    def getFitness(self):
        return self.__fitness
    
    def getDistance(self):
        return self.__distance

    def setCities(self, cities):
        self.__cities = cities
    
    def setFitness(self, fitness):
        self.__fitness = fitness
    
    def setDistance(self, distance):
        self.__distance = distance
        
    def calculDistance(self):
        if (self.__distance == 0 ):
            routDistance = 0 
            for i in range(len(self.__cities)):
                city1 = self.__cities[i]
                city2 = None
                if( i+1 < len(self.__cities)):
                    city2 = self.__cities[i+1]
                else:
                    city2 = self.__cities[0]
                routDistance += city1.calculDistance(city2)
            self.__distance = routDistance
        return self.__distance
    
    def calculFitness(self):
        if( self.__fitness == 0):
            self.__fitness = 1 / float(self.calculDistance())
        return self.__fitness
    
    def __str__(self):
        s = ""
        for city in self.__cities:
            s += city.__str__()+""
        s += " distance :"+str(self.__distance)
        return s
    
    