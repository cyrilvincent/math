"""
Simple genetic algorithm guessing a string.
"""

# ----- Dependencies

import random
import pandas as pd
from typing import Tuple, List

import numpy as np
from numpy._typing import NDArray


class Genetic:

    def __init__(self,
                 mutate_ratio=0.1,
                 chance_retain_best_scored=0.2,
                 chance_retain_low_scored=0.05,
                 population_nb=100,
                 max_generation=100000,
                 nb_max=10000):
        self.mutate_ratio = mutate_ratio
        self.chance_retain_best_scored = chance_retain_best_scored
        self.chance_retain_low_scored = chance_retain_low_scored
        self.population_nb = population_nb
        self.max_generation = max_generation
        self.nb_max = nb_max
        self.x = None
        self.y = None
        self.fn = None


    def get_random(self) -> int:
        return np.random.randint(self.nb_max)

    def get_random_individual(self) -> List[int]:
        return [self.get_random() for _ in range(2)]

    def get_random_population(self):
        return [self.get_random_individual() for _ in range(self.population_nb)]

    def score(self, l: List[int]) -> float:
        losses = []
        min = (self.fn(np.min(self.x),0,0) - self.y[0]) ** 2
        max = (self.fn(np.max(self.x), self.nb_max, self.nb_max) - self.y.values[-1]) ** 2
        for (x, y) in zip(self.x, self.y):
            res = self.fn(x, l[0], l[1])
            losses.append((res - y) ** 2)
        return 1 / np.sqrt(np.mean(losses))




    def population_scores(self, population: List[List[int]]) -> List[Tuple[List[int], float]]:
        scores = []
        for individual in population:
            scores.append((individual, self.score(individual)))
        return sorted(scores, key=lambda x: x[1], reverse=True)

    def mutate(self, parents: List[List[int]]):
        for individual in parents:
            if random.random() < self.mutate_ratio:
                place_to_modify = int(random.random() * 2)
                individual[place_to_modify] = self.get_random()

    def create_children(self, parents: List[List[int]]) -> List[List[int]]:
        desired_len = self.population_nb - len(parents)
        children = []
        while len(children) < desired_len:
            father = random.choice(parents)
            mother = random.choice(parents)
            child = father[:2 // 2] + mother[2 // 2:]
            children.append(child)
        return children

    def evolve_population(self, population: List[List[int]]) -> Tuple[List[List[int]], float, float]:
        raw_population_scores = self.population_scores(population)
        scores = []
        population_scores = []
        for individual, score in raw_population_scores:
            scores.append(score)
            population_scores.append(individual)
            if score == 1.0:
                return population, float(np.mean(scores)), float(np.max(scores))

        # Filter the top graded individuals
        parents = population_scores[:int(self.population_nb * self.chance_retain_best_scored)]

        # Randomly add other individuals to promote genetic diversity
        for individual in population_scores[int(self.population_nb * self.chance_retain_best_scored):]:
            if random.random() < self.chance_retain_low_scored:
                parents.append(individual)

        # Mutate some individuals
        self.mutate(parents)

        # Crossover parents to create children
        children = self.create_children(parents)

        # The next generation is ready
        parents.extend(children)
        return parents, float(np.mean(scores)), float(np.max(scores))

    def evolve(self, population: List[List[int]]) -> Tuple[List[List[int]], float, int]:
        i = 0
        max_score = 0
        while max_score < 1 and i < self.max_generation:
            population, average_score, max_score = self.evolve_population(population)
            if i % 100 == 0:
                print(f'Error: {int(1 / max_score)} in {i} generations')
                print(population[0])
            i += 1
        return population, max_score, i

    def fit(self, x:NDArray, y:NDArray, fn) -> Tuple[List[int], float]:
        """ Main function. """

        # Create a population and compute starting grade
        self.x = x
        self.y = y
        self.fn = fn
        population = self.get_random_population()

        # Make the population evolve
        population, max_score, i = self.evolve(population)
        print(f'Error: {int(1 / max_score)} in {i} generations')

        # Print the solution
        if max_score == 1.0:
            print(f'Solution found:')
        else:
            print(f'No solution found after {i} generations.')
            print('Best solution:')
        print(population[0])
        return population[0], max_score

if __name__ == '__main__':
    dataframe = pd.read_csv("data/house/house.csv")
    dataframe = dataframe[dataframe.surface < 200]
    g = Genetic(nb_max=1000, max_generation=2000)
    g.fit(x=dataframe.surface, y=dataframe.loyer, fn=lambda x,a,b: a*x+b)

