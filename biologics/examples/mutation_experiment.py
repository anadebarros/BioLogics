from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter
from biologics.mutation import point_mutation

def run_organism(label, genome):
    print(f"\n{label}")
    print("Genome:", genome)

    organism = Organism(genome=genome, energy=10)
    interpreter = BioLogicsInterpreter(organism)
    interpreter.run()

# Original genome
original_genome = "ATGAAAAAGGCCCCCTAA"

# Mutated genome
mutated_genome = point_mutation(original_genome)

print("=== Mutation Experiment ===")
print("Original genome:", original_genome)
print("Mutated genome: ", mutated_genome)

run_organism("Running original organism", original_genome)
run_organism("Running mutated organism", mutated_genome)

#Run this multiple times — behavior will vary.
