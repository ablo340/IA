import random

IND_SIZE = 10
POP_SIZE = 6

# Initialising the population.
population = []


# Defining the fitness function.
def evaluate(ind):
    return sum(ind)


# Defining the mating function.
# single point crossover
def mate(ind1, ind2):
    k = random.randint(0, IND_SIZE-1)  # generating the random number to perform crossover

    # interchanging the genes
    if random.random() < PROB_MATING:
        for i in range(k, IND_SIZE):
            ind1[i], ind2[i] = ind2[i], ind1[i]
    return ind1, ind2


# Defining the mutation function.
# Bit Flip Mutation
def mutate(ind):
    for i in range(IND_SIZE):
        if random.random() < PROB_MUTATION:
            ind[i] = type(ind[i])(not ind[i])
    return ind


# Defining the selection function.
def select(pop):
    for i in range(3):
        ind1 = roulette_wheel(pop)
        pop.remove(ind1)

        ind2 = roulette_wheel(pop)
        pop.remove(ind2)

        ind1, ind2 = mate(ind1, ind2)  # crossover
        ind1 = mutate(ind1)  # mutate
        pop.append(ind1)
        pop.append(ind2)

    return pop


def roulette_wheel(pop):
    sum_fit = sum(evaluate(ind) for ind in pop)
    pick = random.uniform(0, sum_fit)
    current = 0
    for ind in pop:
        current += evaluate(ind)
        if current > pick:
            return ind


# Running the simulation.
if __name__ == '__main__':
    PROB_MATING = 0.5
    PROB_MUTATION = 0.2
    ITERATIONS = 100
    it = 1  # iteration

    # initialize population
    population = ([[random.randint(0, 1) for x in range(IND_SIZE)] for i in range(POP_SIZE)])
    print("initial pop is ", population)

    best_fitness = max(evaluate(ind) for ind in population)
    print(best_fitness)

    while it < ITERATIONS and best_fitness != IND_SIZE:
        print(f"🧬 GENERATION {it}")
        population = select(population)
        print(population)

        best_fitness = max(evaluate(ind) for ind in population)
        print(best_fitness)

        it += 1

    best_ind = max(evaluate(ind) for ind in population)
    print(best_ind)