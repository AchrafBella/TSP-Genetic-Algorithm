# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:51:19 2020

@author: Supernova
"""
import numpy as np
import random
import matplotlib.pyplot as plt
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
# city class define by two coordanate x and y 
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        return np.sqrt((xDis ** 2) + (yDis ** 2))
    
    def __repr__(self):
        return "x = {}, y = {}".format(self.x, self.y)
    
# Rout class to regester all possible routes 
# we shuffle the cities to get a random rout each time we instance rout 
class Rout():
    def __init__(self, cities):
        self.cities = random.sample(cities, len(cities))
        self.distance = 0
        self.Fitness = 0
        pass
    
    def setCities(self, cities):
        self.cities = cities
    
    def __routeDistance(self):
        path = 0
        if self.distance  == 0:
            for i in range(len(self.cities)):
                From = self.cities[0]
                to = None
                if(i+1 <len(self.cities)):
                    to = self.cities[i+1]
                else:
                    to = self.cities[0]
                path += From.distance(to)
            self.distance = path
        return self.distance
    
    def routeFitness(self):
        if(self.Fitness == 0):
            self.Fitness = 1 / (float) (self.__routeDistance())
        return self.Fitness
    
    def __str__(self):
        s = ""
        for elm in self.cities:
            s += elm.__repr__()+"|"
        s +="fitness "+str(self.Fitness)
        return s

"""
Genetic algorithm steps :
    popualtion 
    selction
    crossover
    mutation
"""
# creation of a collection on induvidual where every individual is a possible rout 
# pop == popualtion of routes
def Population(cities, size):
    pop = [ Rout(cities) for _ in range(size)]
    return pop

# to have an idea about the total distance in each rout 
def routDistance(pop):
    distance = 0
    for elm in pop:
        elm.routeFitness()
        distance += elm.distance
    return distance

# selection of the top best way based on their fitness
# we calculed the fitness of each rout and then we sorted it
def Selection(pop):
    for elm in pop:
        elm.routeFitness()
    pop.sort(key = lambda rout : rout.Fitness, reverse = True )
    return pop

# merging the best two parents to get new child where every child is possible rout
# from the selcted people 
# we have to make sure that we will not add any city more than once
# each parent is a tour 
# and we gonna take some cities in parent1 (tour1) and take the rest from parent 2 and making sure that the cityes aren't the same

def beerd(parent1 , parent2):
    p1 = []
    geneA = int(random.random() * len(parent1.cities))
    geneB = int(random.random() * len(parent1.cities))
    
    kid = Rout([])
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    
    for i in range(startGene, endGene):
        p1.append(parent1.cities[i])
    
    p2 = [c for c in parent2.cities if c not in p1]
    
    kid.setCities(p1 + p2)
    kid.routeFitness()
    return kid

def crossover(pop, top):
    top_10 = pop[:top]
    children = []
    del pop[top:len(pop)]
    
    parent1 = random.choice(top_10)
    parent2 = random.choice(top_10)
    
    for i in range(top):
        kid = beerd(parent1, parent2)
        children.append(kid)
    pop.extend(children)
    return pop

# for the mutation we are going to select an individual which is a rout 
# and then we gonna randomly choose a swap to change all the cities places in the tour
def mutation(pop, mutationRate):
    # we choosed a tour in the population
    individual = random.choice(pop)
    if(random.random() < mutationRate):
        random.sample(individual.cities, len(individual.cities))
    return pop

def __nextGeneration(curentgeneration, top, mutationRate):
    s = Selection(curentgeneration)
    c = crossover(s, top)
    m = mutation(c, mutationRate)
    m = Selection(m)
    nextGenration = m
    return nextGenration

progress = []
def GeneticAlgorithm(cities, size, top, mutationRate, generation):
    
    p = Population(cities,size)
    print("Initial distance ",routDistance(p))
    progress.append(routDistance(p))
    
    for e in range(generation):
        if( e % 100 == 0):
            print("distance at generation ",e,' is ',routDistance(p))
        p = __nextGeneration(p, top, mutationRate)
        progress.append(routDistance(p))

    
    print('Final distance ',routDistance(p))
    print(' best rout ',Selection(p)[0].__str__())
    pass

def GeneticAlgorithmPlot():
    plt.plot(progress)
    plt.xlabel('distance')
    plt.ylabel('Generation')
    plt.show()

# pour tester notre algorithme 
if __name__ == "__main__":
    # cities decitinetion
    c1 = City(1,0)
    c2 = City(0,0)
    c3 = City(5,4)
    c4 = City(11,10)
    c5 = City(5,8)
    c6 = City(20,5)
    
    # liste of cities 
    cities = [c1, c2, c3, c4, c5, c6]
   
    GeneticAlgorithm(cities, 8, 4, 0.2, 10000)
    GeneticAlgorithmPlot()
    
    
    

















 