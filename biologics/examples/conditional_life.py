from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

# push 1 → store → ifzero → print
genome = "ATG AAA CCG TTT CCC TAA"

organism = Organism(genome=genome, energy=10)
interpreter = BioLogicsInterpreter(organism)
interpreter.run()

#small mutation, different behavior
#Try mutating AAA → AAG and rerun
