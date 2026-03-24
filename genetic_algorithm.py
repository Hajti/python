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

def generate_chromosome() -> int:
    return [random.randint(0,9) for _ in range(CHROMOSOME_LENGHT)]

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


# def genetic_algorithm(population):
#     best = population[0]
#     while i < ITERATIONS or target_found(best) == False:
#     return best

#================================================
#               MAIN FUNCTION
#================================================
def main():
    population = initialize_population()
    parents = tournament_selection(population,TOURNAMENT_SIZE)
    


if __name__ == '__main__':
    main()