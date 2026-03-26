import random
import matplotlib.pyplot as plt

ITERATIONS = 1000
POPULATION_SIZE = 100
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
        target_int = int("".join(map(str, TARGET)))
        chromosome_int = int("".join(map(str, chromosome)))
    return abs(fitness-(target_int-chromosome_int))

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
    tournament = []
    while len(parents) <= POPULATION_SIZE:
        tournament.clear()
        for i in range(0,k):
            random_number = random.randint(0,POPULATION_SIZE-1)
            member = population[random_number]
            tournament.append(member)
        winner = min(tournament, key=lambda win: win.fitness)
        parents.append(winner)
    return parents

def crossover(parent_1: Member, parent_2: Member, crossover_point: int) -> Member:
    chromosome = []
    for i in range(CHROMOSOME_LENGHT):
        if i <= crossover_point:
            chromosome.append(parent_1.chromosome[i])
        else:
            chromosome.append(parent_2.chromosome[i])
    fitness = fitness_function(chromosome)
    child = Member(chromosome, fitness)
    return child

def mutate(child: Member) -> Member:
    gene_to_mutate = random.randint(0,CHROMOSOME_LENGHT-1)
    child.chromosome[gene_to_mutate] = random.randint(0,9)
    return child

def generate_new_population(parents: list[Member]) -> list[Member]:
    new_population = []
    new_population.append(parents[0])
    new_population.append(parents[1])
    indx = 0
    while len(new_population) <= POPULATION_SIZE-1:
        #generate random point for crossover
        crossover_point = random.randint(0,CHROMOSOME_LENGHT)
        child = crossover(parents[indx], parents[indx+1],crossover_point)
        
        mutation = random.random()
        if mutation >= MUTATION_CHANCE:
            child = mutate(child)

        new_population.append(child)
        indx += 1
    return new_population

#================================================
#               GENETIC ALGORITHM
#================================================

def genetic_algorithm(population: list[Member]) -> Member:
    solution_found = False
    generation = 0
    solution = []
    solution.append(min(population, key=lambda ind: ind.fitness))
    
    while generation < ITERATIONS:
        parents = tournament_selection(population,TOURNAMENT_SIZE)
        parents.sort(key=lambda parent: parent.fitness)
        #parents.reverse()

        population = generate_new_population(parents)
        
        solution.append(min(population, key=lambda ind: ind.fitness))
        if target_found(solution[generation]):
            solution_found = True
            print(f'===================================================\nsolution found at {generation}. generation')
            print(f'Solution chromosome {solution[generation].chromosome}, solution fitness {solution[generation].fitness}')
            break
        else:
            #print(f'Iteration: {generation}\nSolution chromosome {solution.chromosome}, solution fitness {solution.fitness}')
            generation += 1
    return solution, generation, solution_found




#================================================
#               MAIN FUNCTION
#================================================
def main():
    population = initialize_population()
    solution, generation, solution_found = genetic_algorithm(population)
    if not solution_found:
        print(f'Could not find solution')

    plt.plot([solution[i].fitness * -1 for i in range(len(solution))],color='blue',linestyle='--')
    plt.show()

if __name__ == '__main__':
    main()