import random
import matplotlib

CHROMOSOME_LENGHT = 5
POPULATION_SIZE = 50
ITERATIONS = 100
TOURNAMENT_SIZE = 5

TARGET = [1,2,3,4,5]

#================================================
#               MEMBER CLASS
#================================================
class Member():
    def __init__(self,chromosome,fitness):
        self.chromosome = chromosome
        self.fitness = fitness

def generate_chromosome() -> int:
    return [random.randint(0,9) for _ in range(CHROMOSOME_LENGHT)]

#================================================
#               FITNESS FUNCTION
#================================================
def fitness_function(chromosome: list[int]) -> int:
    fitness = 0
    for i in range(len(chromosome)):
        if chromosome[i] == TARGET[i]:
            fitness += 1
    return fitness

def target_found(member: Member) -> bool:
    for i in range(len(TARGET)):
        if member.chromosome[i] != TARGET[i]:
            return False
            break
    return True

#================================================
#               INITIALIZE POPULATION
#================================================

def initialize_population():
    population = []
    for i in range(POPULATION_SIZE):
        chromosome = generate_chromosome()
        fitness = fitness_function(chromosome)
        population.append(Member(chromosome, fitness))
    return population

def tournament_selection(population: list[Member], k: int) -> list[Member]:
    parents = []

    while len(parents) < POPULATION_SIZE:
        tournament = random.sample(population,k)
        winner = max(tournament, key=lambda ind: ind.fitness)
        parents.append(winner)
    return parents

def crossover(parent_1: Member, parent_2: Member) -> Member:
    child = Member()
    return child

# def generate_new_population(parents: list[Member]) -> list[Member]:
#     new_population = []
#     while len(new_population) < POPULATION_SIZE:

#     return new_population

#================================================
#               GENETIC ALGORITHM
#================================================

def genetic_algorithm(population: list[Member],new_member) -> Member:
    best = max(population, key=lambda ind: ind.fitness)
    i = 0
    while i < ITERATIONS and target_found(best) == False:
        parents = tournament_selection(population,TOURNAMENT_SIZE)
        
        
        best = max(population, key=lambda ind: ind.fitness)
        i += 1
    return best, i




#================================================
#               MAIN FUNCTION
#================================================
def main():
    population = initialize_population()
    chromosome = [1,2,3,4,5]
    new_member = Member(chromosome, fitness_function(chromosome))
    solution, end_iteration = genetic_algorithm(population,new_member)
    print(f'Found Solution: {solution.chromosome} in {end_iteration}. iteration')


if __name__ == '__main__':
    main()