from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter

# START + NOOPs + STOP
genome = "ATG TTC TTC TTC TAA"

organism = Organism(genome=genome, energy=10)
interpreter = BioLogicsInterpreter(organism)
interpreter.run()

# Alive but does nothing, neutral genome
