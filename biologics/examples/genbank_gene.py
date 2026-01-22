from biologics.organism import Organism
from biologics.interpreter import BioLogicsInterpreter
from biologics.genbank import fetch_gene

# Example: human TP53 gene (tumor suppressor)
genome = fetch_gene("NM_000546")

print(f"Loaded genome length: {len(genome)}")

organism = Organism(
    genome=genome,
    energy=300
)


interpreter = BioLogicsInterpreter(
    organism,
    mode="real"
)

interpreter.run()
