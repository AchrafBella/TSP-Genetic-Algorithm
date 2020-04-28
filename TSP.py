# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:24:33 2020

@author: Supernova
"""

#importing packaging 
import numpy as np
import random 
from matplotlib import pyplot as plt
from Rout import Rout
from City import City
import copy
random.seed(1)
"""
TSP : Given a list of cities and the distances between each pair of cities
     what is the shortest possible route that visits each city and returns to the origin city?
Genetic Algorithm approach:
    Gene       : a city (represented as (x, y) coordinates)
    Individual : a single route satisfying the conditions above
    Population : a collection of possible routes (i.e., collection of individuals)
    Parents    : two routes that are combined to create a new route
    Mating pool: a collection of parents that are used to create our next population (thus creating the next generation of routes)
    Fitness    : a function that tells us how good each route is (in our case, how short the distance is)
    Mutation   : a way to introduce variation in our population by randomly swapping two cities in a route
    Elitism    : a way to carry the best individuals into the next generation
"""

def Initialize_routs(cities, rout_numbre):
    routs = [ Rout(cities) for _ in range(rout_numbre)]
    return routs

def Fitness(tours):
    for elm in tours:
        elm.calculFitness()
        pass
    pass

def Selection(routs):
    routs.sort(key = lambda rout : rout.getFitness(), reverse = True)
    return routs

def beerd(parent1 , parent2):
    p1 = []
    geneA = int(random.random() * len(parent1.getCities()))
    geneB = int(random.random() * len(parent2.getCities()))
    
    kid = Rout([])
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    
    for i in range(startGene, endGene):
        p1.append(parent1.getCities()[i])
    
    p2 = [c for c in parent2.getCities() if c not in p1]
    
    kid.setCities(p1 + p2)
    kid.calculFitness()
    return kid


def Crossover(pop, top):
    
    children = []
    for i in range(top):
        children.append(pop[i])
        pass
    print('child',top)
    print(*children, sep="\n")
    
    
    
    print("liste final child ")
    print(*children, sep = '\n')
    return children
"""
def Crossover1(routs, eliteSize):
    children = []
    length = len(routs) - eliteSize
    pool = random.sample(routs, len(routs))

    for i in range(0,eliteSize):
        children.append(routs[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(routs)-i-1])
        children.append(child)
    return children
"""

def Mutation(pop, mutationRate):
    # we choosed a tour in the population
    rout = random.choice(pop)
    if(random.random() < mutationRate):
        cities = random.sample(rout.getCities(), len(rout.getCities()))
        rout.setCities(cities)
    return pop

"""======================================================================================================="""

def distance_Generation(tours):
    distance = 0
    for elm in tours:
        distance += elm.getDistance()
    return distance

def best_rout(current_generation_population):
    
    pass
    

def __nextGeneration(current_generation, eliteSize, mutationRate):
    Fitness(current_generation)
    s = Selection(current_generation)
    c = Crossover(s, eliteSize)
    m = Mutation(c, mutationRate)
    return m

def geneticAlgorithm(cities,tour_numbre, mutationRate, eliteSize, generations):
    p = Initialize_routs(cities, tour_numbre)
    Fitness(p)
    I = distance_Generation(p)
    print("distance initial ",I)
    for i in range(generations):
        p = __nextGeneration(p, eliteSize, mutationRate)
        #print(*p, sep = '\n')
        #print('_'*25)
        pass
    print("distance final", distance_Generation(p))
    print("difference",I - distance_Generation(p))
    pass
    

if __name__ == "__main__":
    
    
    
    
    cityList = []
    
    for i in range(0,5):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
        pass
    
    
    
    """
    cityList = []
    n = int(input('give the nombre of cities'))
    x = np.math.factorial(n)
    for i in range(0,n):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
        pass
    print(' The number of possible routes is ',x)
    mutationrate = [0.1,0.001, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    
    tr = int(input('give the nombre of tours '))
    while(x < tr):
        tr = int(input("this number of tours is not possible "))
        
    geneticAlgorithm(cityList,tr,0.001,10, 155)
    """
 
    
    p = Initialize_routs(cityList,8)
    print(*p, sep="\n")
    print('='*50)
    Fitness(p)
    print(*p, sep="\n")
    print('='*50)
    s = Selection(p)
    print(*s, sep="\n")
    print('='*50)
    c = Crossover(s,4)
    print(*c, sep="\n")
    print('='*50)
    m = Mutation(c,0.8)
    print(*m, sep="\n")
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        