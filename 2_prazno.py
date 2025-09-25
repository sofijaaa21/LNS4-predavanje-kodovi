import random

# -----------------------------
# 1. PODACI PROBLEMA
# -----------------------------
# Lista predmeta: ime, težina, vrednost
items = [
    {"name": "Item 1", "weight": 5, "value": 7},
    {"name": "Item 2", "weight": 8, "value": 8},
    {"name": "Item 3", "weight": 3, "value": 4},
    {"name": "Item 4", "weight": 2, "value": 10},
    {"name": "Item 5", "weight": 7, "value": 4},
    {"name": "Item 6", "weight": 9, "value": 6},
    {"name": "Item 7", "weight": 4, "value": 4},
]

# >>> POLAZNICI: postavite maksimalni kapacitet ranca (npr. 15 ili 20)
knapsack_capacity = ____


# -----------------------------
# 2. PARAMETRI GENETSKOG ALGORITMA
# -----------------------------
# >>> POLAZNICI: odaberite vrednosti na osnovu eksperimenta
population_size = ____       # npr. 50
mutation_rate   = ____       # npr. 0.05
num_generations = ____       # npr. 200


# -----------------------------
# 3. KREIRANJE POPULACIJE
# -----------------------------
def create_individual():
    """
    Kreira nasumičnog pojedinca.
    Pojedinac je binarna lista dužine = broj predmeta.
    """
    return [random.randint(0, 1) for i in range(len(items))]

def create_population():
    """
    Kreira inicijalnu populaciju od population_size jedinki.
    """
    return [create_individual() for _ in range(population_size)]


# -----------------------------
# 4. FITNES FUNKCIJA
# -----------------------------
def evaluate_fitness(individual):
    """
    Računa ukupnu vrednost i težinu za datog pojedinca.
    Ako je težina veća od kapaciteta, vrednost je 0 (kazna).
    """
    total_value  = #dodati
    total_weight = #dodati
    for i in range(len(items)):
        if individual[i] == 1:
        #dodati
    if total_weight > knapsack_capacity:
        #dodati
    return total_value


# -----------------------------
# 5. SELEKCIJA RODITELJA
# -----------------------------
def select_parents(population):
    """
    Roulette-wheel selekcija:
    veća verovatnoća izbora za jedinke s većim fitness-om.
    """
    fitness_values = [evaluate_fitness(ind) for ind in population]
    total_fitness  = sum(fitness_values)

    # >>> POLAZNICI: razmislite šta se dešava ako je total_fitness = 0
    # i kako to rešiti (hint: dodajte malu konstantu ili izaberite slučajno)

    probabilities  = [f / total_fitness for f in fitness_values]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents[0], parents[1]


# -----------------------------
# 6. CROSSOVER
# -----------------------------
def crossover(parent1, parent2):
    """
    Jednotackasti crossover.
    >>> POLAZNICI: da li želite jedno-tačkani ili uniform crossover?
    """
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = #dodati
    child2 = #dodati
    return child1, child2


# -----------------------------
# 7. MUTACIJA
# -----------------------------
def mutate(individual):
    """
    Bit-flip mutacija: svaka pozicija se obrće s verovatnoćom mutation_rate.
    """
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = #dodati


# -----------------------------
# 8. GLAVNA PETLJA GA
# -----------------------------
def genetic_algorithm():
    population = create_population()

    for generation in range(num_generations):
        new_population = []

        # >>> POLAZNICI: možete dodati ELITIZAM (zadržati najbolju jedinku)
        # ako želite da poboljšate rezultate.

        for _ in range(population_size // 2):
            parent1, parent2 = #pozvati funkciju
            child1, child2   = #pozvati funkciju
            mutate(#dete)
            mutate(#dete)
            new_population.extend([#dodati decu])

        # >>> UČENICI: razmislite da li treba da dodate popravku (repair)
        # za rešenja koja prelaze kapacitet

        population = new_population

    # Najbolje rešenje iz finalne populacije
    best_individual = max(population, key=evaluate_fitness)
    best_fitness    = evaluate_fitness(#pozvati)
    return best_individual, best_fitness


# -----------------------------
# 9. POKRETANJE
# -----------------------------
best_solution, best_fitness = genetic_algorithm()

print("Best Solution (binarno):", #print)
print("Best Fitness (vrednost):", #print)

# >>> POLAZNICI: prikažite i listu imena predmeta koji su izabrani
# pomoću best_solution da biste jasno videli sadržaj ranca.
