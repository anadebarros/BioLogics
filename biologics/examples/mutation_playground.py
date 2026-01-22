from biologics.mutation import point_mutation
from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

base_genome = "ATG AAA AAG GAA CCG CCC TAA"

for i in range(5):
    mutated = point_mutation(base_genome)
    print("\nGenome:", mutated)

    organism = Organism(genome=mutated, energy=10)
    interpreter = BioLogicsInterpreter(organism)
    interpreter.run()

#Rapid exploration of symbolic mutation space
#Emergence & drift
