import random

# Knapsack Problem parameters
items = [
    {"name": "Item 1", "weight": 5, "value": 7},
    {"name": "Item 2", "weight": 8, "value": 8},
    {"name": "Item 3", "weight": 3, "value": 4},
    {"name": "Item 4", "weight": 2, "value": 10},
    {"name": "Item 5", "weight": 7, "value": 4},
    {"name": "Item 6", "weight": 9, "value": 6},
    {"name": "Item 7", "weight": 4, "value": 4},
]

knapsack_capacity = 22

# Genetic Algorithm parameters
population_size = 100
mutation_rate = 0.1
num_generations = 100

# Create initial population
def create_individual(): 
    # Generate a random binary string of the same length as the items list
    return [random.randint(0, 1) for i in range(len(items))]

def create_population():  
    # Create a population of random individuals
    return [create_individual() for _ in range(population_size)]

# Evaluate fitness of an individual
def evaluate_fitness(individual):
    # Calculate the total value and weight of the knapsack for the given individual
    total_value = 0
    total_weight = 0
    for i in range(len(items)):
        if individual[i] == 1:
            total_value += items[i]['value']
            total_weight += items[i]['weight']
    # If the total weight exceeds the knapsack capacity, set the value to 0 (invalid solution)
    if total_weight > knapsack_capacity:
        total_value = 0
    return total_value

# Select parents for crossover using a roulette wheel selection
def select_parents(population):
    fitness_values = [evaluate_fitness(individual) for individual in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents[0], parents[1]

# Perform crossover using a single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Perform mutation by flipping bits with a given probability
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

# Run the genetic algorithm
def genetic_algorithm():
    population = create_population()

    for _ in range(num_generations):
        new_population = []
        # Create new individuals through crossover and mutation
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    # Find the best individual (highest fitness) in the final population
    best_individual = max(population, key=evaluate_fitness)
    best_fitness = evaluate_fitness(best_individual)
    return best_individual, best_fitness

# Run the genetic algorithm and print the results
best_solution, best_fitness = genetic_algorithm()
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)