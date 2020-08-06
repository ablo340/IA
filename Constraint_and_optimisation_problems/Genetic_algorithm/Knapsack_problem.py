from deap import base, creator, tools
import random

"""
# Population
sac1 = [1, 2, 3, 4, 2] (9, 17) # representation individu
sac = [3, 2, 1, 1, 4] (12, 25)

# Fitness function
=> poids maximal possible(inferieur ou egale à 15) prix maximal
fct = prix_total/(poids_total - 15)

# Selection
Elistsim => sac1

# Crossover
[1, 2, 3, 4, 2] => [3, 2, 3, 4, 2]
[3, 2, 1, 1, 4] => [1, 2, 1, 1, 4]

# Mutation
[1, 2, 3, 4, 2] => [2, 2, 3, 4, 1] # melange
"""

IND_INIT_SIZE = 6
MAX_WEIGHT = 15
NBR_ITEMS = 5

# building base
creator.create("FitnessMax", base.Fitness, weights=(1.0, 1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

items = {}

items[0] = (12, 4)  # green
items[1] = (4, 10)  # yellow
items[2] = (1, 2)  # grey
items[3] = (2, 2)  # blue
items[4] = (1, 1)  # brown

toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NBR_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def eval_knapsack(individual):
    weight = 0.0
    value = 0.0
    for item in individual:
        weight += items[item][0]
        value += items[item][1]
    if weight > MAX_WEIGHT:
        return MAX_WEIGHT-weight, value  # Ensure overweighted bags are dominated

    return weight, value


toolbox.register("evaluate", eval_knapsack)
toolbox.register("mate", tools.cxTwoPoint)  # crossover operation
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)  # mutation operator
toolbox.register("select", tools.selAutomaticEpsilonLexicase)  # parent selector operator


def launch():
    random.seed(64)

    # create an initial population of 10 individuals
    pop = toolbox.population(n=100)

    # CXPB is the crossover probability
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = 0.5, 0.2

    # number of generation
    num_generations = 8

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print(" Evaluated %i individuals" % len(pop))

    for gen in range(num_generations):

        print("-- Generation %i --" % gen)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            # cross two individuals with probability CXPB
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            # mutate an individual with probability MUTPB
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print(" Evaluated %i individuals" % len(invalid_ind))

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        print(" Min %s" % min(fits))
        print(" Max %s" % max(fits))
        print(" Avg %s" % mean)
        print(" Std %s" % std)

    print("-- End of (successful) evolution --")

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))


if __name__ == "__main__":
    launch()
