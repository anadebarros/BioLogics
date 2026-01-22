from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

# Small real DNA sequence
gene = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

organism = Organism(genome=gene, energy=50)
interpreter = BioLogicsInterpreter(organism, mode="real")
interpreter.run()

#Run a real biological gene as an organism
#This uses: Real DNA, Real translation, Abstract semantic execution
