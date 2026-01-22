from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter
from biologics.mutation import point_mutation

gene = "ATGGCTGGTCCTTAA"

print("Original gene:", gene)
organism = Organism(genome=gene, energy=10)
BioLogicsInterpreter(organism, mode="real").run()

mutated = point_mutation(gene)
print("\nMutated gene:", mutated)
mutant = Organism(genome=mutated, energy=10)
BioLogicsInterpreter(mutant, mode="real").run()


#Now you can see mutations change semantic behavior — sometimes silently, sometimes catastrophically
