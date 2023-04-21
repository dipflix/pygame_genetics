import math
import random


class Genetics:
    def __init__(self, population_size, chromosome_length, crossover_rate, mutation_rate, generations):
        self.POPULATION_SIZE = population_size
        self.CHROMOSOME_LENGTH = chromosome_length
        self.MIN_VALUE = -5.12
        self.MAX_VALUE = 5.12
        self.CROSSOVER_RATE = crossover_rate
        self.MUTATION_RATE = mutation_rate
        self.GENERATIONS = generations

    def fitness(self, chromosome):
        x1, x2 = chromosome
        return 20 + x1 ** 2 + x2 ** 2 - 10 * math.cos(2 * math.pi * x1) - 10 * math.cos(2 * math.pi * x2)

    def generate_initial_population(self):
        population = []
        for i in range(self.POPULATION_SIZE):
            chromosome = [random.uniform(self.MIN_VALUE, self.MAX_VALUE) for _ in range(self.CHROMOSOME_LENGTH)]
            population.append(chromosome)
        return population
