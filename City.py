# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:29:54 2020

@author: Supernova
"""
import numpy as np

class City():
    def __init__(self, x, y):
        """
        Parameters
        ----------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.
        Returns
        -------
        None.
        """
        self.__x = x
        self.__y = y
        pass
    
    # getters and setter 
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__xx = x
        
    def setY(self, y):
        self.__xy = y
    
    def __str__(self):
        return "(x={}, y={})".format(self.__x, self.__y)
    
    def calculDistance(self, city):
        distanceX = abs(self.getX() - city.getX())
        distanceY = abs(self.getY() - city.getY())
        return np.sqrt( distanceX*distanceX + distanceY*distanceY)
    