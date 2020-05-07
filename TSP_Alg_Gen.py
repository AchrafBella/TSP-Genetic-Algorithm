    # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

@author: Supernova

"""
#importing packaging 
import numpy as np
import random 
from matplotlib import pyplot as plt
from Rout import Rout
from City import City


# creation of a collection on induvidual where every individual is a possible rout 
# pop == popualtion of routes
def Initilize_popualtion(cities, size):
    routs = [ Rout(cities) for _ in range(size)]
    return routs

# selection of the top best way based on their fitness
# we calculed the fitness of each rout and then we sorted it
def Selection(pop):
    for elm in pop:
        elm.calculFitness()
    pop.sort(key = lambda rout : rout.getFitness(), reverse = True )
    return pop

# merging the best two parents to get new child where every child is possible rout
# from the selcted people 
# we have to make sure that we will not add any city more than once
# each parent is a tour 
# and we gonna take some cities in parent1 (tour1) and take the rest from parent 2 and making sure that the cityes aren't the same

def merge(parent1 , parent2):
    p1 = []
    geneA = int(random.random() * len(parent1.getCities()))
    geneB = int(random.random() * len(parent1.getCities()))
    
    kid = Rout([])
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    
    for i in range(startGene, endGene):
        p1.append(parent1.getCities()[i])
    
    p2 = [c for c in parent2.getCities() if c not in p1]
    
    kid.setCities(p1 + p2)
    kid.calculFitness()
    return kid

def crossover(pop, top):
    top_10 = pop[:top]
    children = []
    del pop[top:len(pop)]
  
    for i in range(top):
        parent1 = top_10[np.random.randint(top)]
        parent2 = top_10[np.random.randint(top)]
        while( parent1 == parent2):
            parent2 = top_10[np.random.randint(top)]
            pass
        
        kid = merge(parent1, parent2)
        children.append(kid)
    pop.extend(children)
    return pop

# for the mutation we are going to select an individual which is a rout 
# and then we gonna randomly choose a swap to change all the cities places in the tour
    
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def mutation1(pop, mutationRate):
    for elm in pop:
        mutate(elm.getCities(),mutationRate)
    return pop
# this mutation is far better than mutation1
def mutation(pop, mutationRate):
    # we choosed a tour in the population
    individual = random.choice(pop)
    if(random.random() < mutationRate):
        random.sample(individual.getCities(), len(individual.getCities()))
    return pop


# to have an idea about the total distance for the population  
def Distance_generation(pop):
    distance = 0
    for elm in pop:
        elm.calculFitness()
        distance += elm.getDistance()
    return distance

# evolution of our population 
def __nextGeneration(curentgeneration, top, mutationRate):
    s = Selection(curentgeneration)
    c = crossover(s, top)
    m = mutation(c, mutationRate)
    m = Selection(m)
    nextGenration = m
    return nextGenration

progress = []
def GeneticAlgorithm(cities, size, top, mutationRate, generation):
    
    p = Initilize_popualtion(cities,size)
    print("Initial distance of the population ",Distance_generation(p))
    # rout distance for a population 
    progress.append(Distance_generation(p))
    
    for e in range(generation):
        if( e % 100 == 0):
            print("distance of population at generation ",e,' is ',Distance_generation(p))            
        p = __nextGeneration(p, top, mutationRate)
        progress.append(Distance_generation(p))
      
    
    print('Final distance of population for generation ',Distance_generation(p))
    print('best rout ',p[0].__str__())

    pass


def GeneticAlgorithmPlot():
    plt.plot(progress)
    plt.xlabel(' generation ')
    plt.ylabel('distance')
    plt.show()


# pour tester notre algorithme 
if __name__ == "__main__":
    # cities decitinetion
    cityList = []
    # inititialize the cities     
    for i in range(0,5):
        cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
        pass
    # genetic algorithm
    
    GeneticAlgorithm(cityList, 16, 5, 0.1, 100)

