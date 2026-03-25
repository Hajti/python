import random
import matplotlib

ITERATIONS = 100
POPULATION_SIZE = 50
CHROMOSOME_LENGHT = 5
TOURNAMENT_SIZE = 5
MUTATION_CHANCE = 0.2

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

def crossover(parent_1: Member, parent_2: Member, crossover_point: int) -> Member:
    chromosome = []
    for i in range(CHROMOSOME_LENGHT):
        if i <= crossover_point:
            chromosome.append(parent_1.chromosome[i])
        else:
            chromosome.append(parent_2.chromosome[i])

    child = Member()
    return child

def mutate(child: Member) -> Member:
    gene_to_mutate = random.randint(0,CHROMOSOME_LENGHT)
    child.chromosome[gene_to_mutate] = random.randint(0,9)
    return child

def generate_new_population(parents: list[Member]) -> list[Member]:
    new_population = []
    new_population.append(parents[i] for i in range(2))
    indx = 0
    while len(new_population) < POPULATION_SIZE:
        #generate random point for crossover
        crossover_point = random.randint(0,CHROMOSOME_LENGHT)
        child = crossover(parents[indx], parents[indx],crossover_point)
        
        mutation = random.random()
        if mutation >= MUTATION_CHANCE:
            child = mutate(child)

        new_population.append(child)
    return new_population

#================================================
#               GENETIC ALGORITHM
#================================================

def genetic_algorithm(population: list[Member]) -> Member:
    generation = 0
    best = {'Generation': generation,'Member': Member}
    best = max(population, key=lambda ind: ind.fitness)
    
    while generation < ITERATIONS and target_found(best) == False:
        parents = tournament_selection(population,TOURNAMENT_SIZE)
        parents.sort(key=lambda parent: parent.fitness)
        parents.reverse()

        population = generate_new_population(parents)
        
        best = max(population, key=lambda ind: ind.fitness)
        generation += 1
    return best, i




#================================================
#               MAIN FUNCTION
#================================================
def main():
    population = initialize_population()
    
    best_member = genetic_algorithm(population,)
    print([parent.fitness for parent in parents])


if __name__ == '__main__':
    main()