import matplotlib.pyplot as plt
from collections import Counter
from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter
from biologics.mutation import reproduce
import itertools

# -----------------------------
# INITIAL POPULATION
# -----------------------------
initial_genomes = [
    "ATGAAAAGGCCCCTAA",
    "ATGAAAAGGCCCCTAA",
]

population = [Organism(genome=g, energy=20) for g in initial_genomes]
generations = 5

# Track all genomes that appear (for consistent coloring)
all_genomes_set = set(initial_genomes)
genome_history = []

# Use a color cycle
color_cycle = itertools.cycle([
    "green", "orange", "blue", "purple", "brown", "pink", "cyan", "red", "yellow"
])
genome_colors = {g: next(color_cycle) for g in all_genomes_set}

# -----------------------------
# GENERATION LOOP
# -----------------------------
for gen in range(1, generations + 1):
    print(f"\n--- Generation {gen} ---")
    next_generation = []

    # Run alive organisms
    for org_index, org in enumerate(population, start=1):
        if not org.alive:
            continue

        print(f"\n[Organism {org_index} executing genome]")
        interpreter = BioLogicsInterpreter(org)
        interpreter.run()

        # Reproduction
        offspring = reproduce(org, mutation_rate=1)
        if offspring:
            next_generation.append(offspring)

            # assign new color if genome not seen before
            if offspring.genome not in genome_colors:
                genome_colors[offspring.genome] = next(color_cycle)
            all_genomes_set.add(offspring.genome)

            print(f"[Reproduced] Parent energy: {org.energy}")
            print(f"Parent genome : {org.genome}")
            print(f"Offspring genome: {offspring.genome}")

    population.extend(next_generation)

    # Record alive genomes
    alive_genomes = [org.genome for org in population if org.alive]
    genome_counts = Counter(alive_genomes)
    genome_history.append(genome_counts)

# -----------------------------
# PLOTTING STACKED BAR CHART
# -----------------------------
plt.figure(figsize=(12,6))
bottoms = [0]*generations

# sort genomes so original is first, mutations stacked above
all_genomes_sorted = list(genome_colors.keys())

for genome in all_genomes_sorted:
    counts_per_gen = [genome_counts.get(genome, 0) for genome_counts in genome_history]
    plt.bar(
        range(1, generations+1),
        counts_per_gen,
        bottom=bottoms,
        color=genome_colors[genome],
        label=genome
    )
    bottoms = [b + c for b, c in zip(bottoms, counts_per_gen)]

plt.xlabel("Generation")
plt.ylabel("Number of Alive Organisms")
plt.title("BioLogics Population Evolution (Unique Genome Colors)")
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#What this does

#Each genome gets a unique color, assigned when it first appears.

#Original genomes are green.

#Mutations in the same generation get different colors, so you can clearly see all mutated offspring.

#Stacked bars show exactly how many organisms of each genome are alive per generation.
