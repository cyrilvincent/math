"""
Simple genetic algorithm guessing a string.
"""

# ----- Dependencies

import random
import string
from typing import Tuple, List

import numpy as np

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
        self.expected = None


    def get_random(self) -> int:
        return np.random.randint(self.nb_max)

    def get_random_individual(self) -> List[int]:
        return [self.get_random() for _ in range(len(self.expected))]

    def get_random_population(self):
        return [self.get_random_individual() for _ in range(self.population_nb)]

    def score(self, l: List[int]) -> float:
        l = np.array(l)
        return len(l[l == self.expected]) / len(self.expected)

    def population_scores(self, population: List[List[int]]) -> List[Tuple[List[int], float]]:
        scores = []
        for individual in population:
            scores.append((individual, self.score(individual)))
        return sorted(scores, key=lambda x: x[1], reverse=True)

    def mutate(self, parents: List[List[int]]):
        for individual in parents:
            if random.random() < self.mutate_ratio:
                place_to_modify = int(random.random() * len(self.expected))
                individual[place_to_modify] = self.get_random()

    def create_children(self, parents: List[List[int]]) -> List[List[int]]:
        desired_len = self.population_nb - len(parents)
        children = []
        while len(children) < desired_len:
            father = random.choice(parents)
            mother = random.choice(parents)
            child = father[:len(self.expected) // 2] + mother[len(self.expected) // 2:]
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
            if i % 1000 == 0:
                print(f'Score: {max_score * 100:.2f}% in {i} generations')
                print(population[0])
            i += 1
        return population, max_score, i

    def fit(self, expected: List[int]) -> Tuple[List[int], float]:
        """ Main function. """

        # Create a population and compute starting grade
        self.expected = np.array(expected)
        population = self.get_random_population()

        # Make the population evolve
        population, max_score, i = self.evolve(population)
        print(f'Score: {max_score * 100:.2f}% in {i} generations')

        # Print the solution
        if max_score == 1.0:
            print(f'Solution found:')
        else:
            print(f'No solution found after {i} generations.')
            print('Best solution:')
        print(population[0])
        return population[0], max_score

if __name__ == '__main__':
    # Addition de 0 à nb_max
    nb_max = 10
    g = Genetic(nb_max=nb_max * 2)
    l = []
    for i in range(nb_max):
        for j in range(nb_max):
            l.append(i)
            l.append(j)
            l.append(i+j)
    print(l)
    g.fit(l)

    # Multiplication de 0 à nb_max
    nb_max = 10
    g = Genetic(nb_max=nb_max ** 2)
    l = []
    for i in range(nb_max):
        for j in range(nb_max):
            l.append(i)
            l.append(j)
            l.append(i * j)
    print(l)
    g.fit(l)

    # nombre premiers
    nb_max = 100
    g = Genetic(nb_max=nb_max)
    l = []
    for i in range(2, nb_max):
        is_prime = True
        for div in range(2,i):
            if i % div == 0:
                is_prime = False
                break
        if is_prime:
            l.append(i)
            is_prime = False
    print(l)
    res, score = g.fit(l)
