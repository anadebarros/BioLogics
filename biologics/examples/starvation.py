from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

# One-base insertion at the start causes a frameshift
# STOP codon is never reached

genome = "ATGAAAAAGGCCCCCTAA"

organism = Organism(
    genome=genome,
    energy=2
)

interpreter = BioLogicsInterpreter(organism)
interpreter.run()
