import random
from biologics.organism import Organism

BASES = ["A", "T", "G", "C"]

def point_mutation(genome: str) -> str:
    """
    Introduce a single point mutation into the genome.
    One base is randomly changed to a different base.
    """
    if not genome:
        return genome

    genome = genome.upper()
    index = random.randint(0, len(genome) - 1)
    original_base = genome[index]

    possible_bases = [b for b in BASES if b != original_base]
    new_base = random.choice(possible_bases)

    mutated = genome[:index] + new_base + genome[index + 1 :]
    return mutated


def reproduce(parent: Organism, mutation_rate: int = 1) -> Organism:
    """
    Parent produces an offspring organism.
    Reproduction consumes energy and applies point mutations.
    """
    if parent.energy < 5:  # reproduction cost
        print("[Not enough energy to reproduce]")
        return None

    parent.energy -= 5  # energy cost to reproduce

    # offspring genome starts as a copy
    offspring_genome = parent.genome

    # apply mutations
    for _ in range(mutation_rate):
        offspring_genome = point_mutation(offspring_genome)

    # create offspring with half of parent's remaining energy
    offspring = Organism(genome=offspring_genome, energy=parent.energy // 2)
    return offspring
