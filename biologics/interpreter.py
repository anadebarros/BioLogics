from biologics.codons import CODON_TABLE
from biologics.vm import StackVM
from biologics.biology import translate_dna_to_protein
from biologics.semantic_map import AMINO_ACID_SEMANTICS

class BioLogicsInterpreter:
    def __init__(self, organism, mode="symbolic"):
        self.organism = organism
        self.mode = mode  # "symbolic" or "real"
        self.vm = StackVM()
        self.running = False

    def run(self):
        if self.mode == "real":
            self.run_real()
        else:
            self.run_symbolic()

    # -----------------------
    # SYMBOLIC MODE (existing)
    # -----------------------
    def run_symbolic(self):
        seq = self.organism.genome.strip().upper()
        codons = [seq[i:i+3] for i in range(0, len(seq), 3)]

        for codon in codons:
            amino, instruction = CODON_TABLE.get(codon, (None, None))

            if instruction == "START":
                self.running = True
                continue

            if instruction == "STOP":
                print("[organism terminated normally]")
                break

            if self.running and instruction:
                self.organism.consume_energy()
                if not self.organism.alive:
                    print("[organism died: energy depleted]")
                    break
                self.vm.execute(instruction)

    # -----------------------
    # REAL BIOLOGY MODE
    # -----------------------
    def run_real(self):
        protein = translate_dna_to_protein(self.organism.genome)

        for aa in protein:
            instruction = AMINO_ACID_SEMANTICS.get(aa)

            if instruction == "START":
                self.running = True
                continue

            if instruction == "STOP":
                print("[organism terminated normally]")
                break

            if self.running and instruction:
                self.organism.consume_energy()
                if not self.organism.alive:
                    print("[organism died: energy depleted]")
                    break
                self.vm.execute(instruction)
