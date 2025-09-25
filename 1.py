import numpy as np

# 1. Ciljna funkcija
def f(x):
    return np.sin(x) + np.cos(2*x)

# 2. Parametri GA
pop_size = 50
generations = 100
mutation_rate = 0.1
x_min, x_max = 0, 10

# 3. Inicijalna populacija
pop = np.random.uniform(x_min, x_max, pop_size)

for gen in range(generations):
    fitness = f(pop)

    # 4. Selekcija (rulet)
    probs = fitness - fitness.min() + 1e-6
    probs /= probs.sum()
    parents = np.random.choice(pop, size=pop_size, p=probs)

    # 5. Ukreštanje (parovi)
    children = []
    for i in range(0, pop_size, 2):
        p1, p2 = parents[i], parents[i+1]
        alpha = np.random.rand()
        child1 = alpha*p1 + (1-alpha)*p2
        child2 = alpha*p2 + (1-alpha)*p1
        children += [child1, child2]

    pop = np.array(children)

    # 6. Mutacija
    mutations = np.random.rand(pop_size) < mutation_rate
    pop[mutations] += np.random.normal(0, 0.1, size=mutations.sum())
    pop = np.clip(pop, x_min, x_max)

best_x = pop[np.argmax(f(pop))]
print("Najbolje rešenje:", best_x, "f(x) =", f(best_x))
