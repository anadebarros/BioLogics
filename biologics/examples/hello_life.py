from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

# A minimal, valid BioLogics genome
# START → 1 → 2 → ADD → PRINT → STOP
genome = "ATGAAAAAGGCCCCCTAA"

organism = Organism(
    genome=genome,
    energy=10  # more than enough
)

interpreter = BioLogicsInterpreter(organism)
interpreter.run()
