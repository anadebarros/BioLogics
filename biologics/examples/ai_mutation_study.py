from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter
from biologics.mutation import point_mutation

base_gene = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

for i in range(5):
    mutant = point_mutation(base_gene)
    print("\nMutant genome:", mutant)

    organism = Organism(genome=mutant, energy=50)
    interpreter = BioLogicsInterpreter(organism, mode="real")
    interpreter.run()

#AI-style mutation loop (no AI yet, just structure)
#This is where: Real genes mutate, Phenotypes diverge, Selection pressure emerges
#Evolutionary structure
