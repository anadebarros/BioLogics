
---
## Project Architecture

```
biologics/
├── organism.py          # Organism lifecycle, energy, alive/dead
├── interpreter.py       # Genome execution engine (symbolic + real)
├── vm.py                # Stack-based virtual machine
├── codons.py            # Symbolic codon → amino acid → instruction map
├── semantic_map.py      # Amino acid → abstract behavior mapping
├── biology.py           # DNA → protein translation (real biology mode)
├── mutation.py          # Point mutation and future reproduction
├── genbank.py           # Fetch real genes from GenBank
├── examples/            # Example scripts demonstrating features
├── docs/                # Documentation (specs, examples, architecture)
└── __init__.py          # Package marker
```

## File Descriptions

### 1. `organism.py`
Defines the **Organism** class, which represents a living entity in BioLogics.

**Responsibilities:**
- Stores the genome (DNA string).
- Tracks energy and life status.
- Handles energy consumption (`consume_energy()`).
- Provides the core “life” model that other modules (like the interpreter) use.

**Key concepts:**
- Organisms die if energy reaches zero.
- Future versions support reproduction and mutation.

---

### 2. `interpreter.py`
Implements the **BioLogicsInterpreter**, the execution engine for genomes.

**Responsibilities:**
- Parses the genome into codons (triplets of nucleotides).
- Executes instructions in **symbolic** or **real biology** mode.
- Consumes organism energy per instruction.
- Handles START and STOP codons.
- Integrates with the VM to perform operations like PUSH, ADD, PRINT.

**Modes:**
- `symbolic`: Uses a codon table mapping codons → instructions.
- `real`: Translates DNA → protein → semantic behaviors using real amino acids.

---

### 3. `vm.py`
Implements the **StackVM**, a minimal stack-based virtual machine.

**Responsibilities:**
- Maintains a stack and executes basic instructions:
  - Arithmetic: `ADD`, `SUB`, `MUL`, `DIV`
  - Stack operations: `PUSH_1`, `PUSH_2`
  - Output: `PRINT`
- Handles stack underflow and empty stack safely.
- Executes both symbolic and real biology instructions.

---

### 4. `codons.py`
Defines the **codon-to-instruction mapping** for symbolic mode.

**Responsibilities:**
- Maps DNA codons (triplets) to:
  - Amino acids (e.g., Lys, Gly, Pro)
  - BioLogics instructions (`PUSH_1`, `ADD`, `PRINT`, `START`, `STOP`)
- Provides redundancy similar to biological codon usage.

---

### 5. `semantic_map.py`
Maps **amino acids** to abstract **semantic behaviors** in real biology mode.

**Responsibilities:**
- Provides a behavioral layer for real protein translation.
- Groups amino acids into functional categories like:
  - Initiation
  - Computation
  - Output
  - Replication
  - Energy management
- Enables execution of real genes with emergent behaviors in BioLogics.

---

### 6. `biology.py`
Handles **real DNA → protein translation** using Biopython.

**Responsibilities:**
- Translates DNA sequences into amino acid sequences.
- Ensures sequences are correctly trimmed or padded to avoid partial codon warnings.
- Provides an interface for the interpreter to process real biological data.

---

### 7. `mutation.py`
Implements mutation and future reproduction mechanisms.

**Responsibilities:**
- Introduces **point mutations** (single-base changes) in genomes.
- Supports random mutations for both symbolic and real genomes.
- Prepares infrastructure for population-level evolution and reproduction.

---

### 8. `genbank.py`
Handles fetching **real genes from NCBI GenBank**.

**Responsibilities:**
- Downloads sequences using Biopython’s `Entrez` module.
- Returns raw DNA sequences for use in BioLogics organisms.
- Enables integration of real biological data into experiments.
- Supports experimentation with semantic behavior of actual genes.

---

### 9. `examples/`
Contains **example scripts** demonstrating BioLogics features.

**Examples include:**
- `hello_life.py`: Minimal living organism
- `broken_frame.py`: ORF errors / stack underflow
- `mutation_experiment.py`: Point mutation tests
- `population_simulation.py`: Reproduction and evolution
- `real_gene.py`: Running real genes in BioLogics
- `genbank_gene.py`: Fetching and executing GenBank sequences

---

### 10. `docs/`
Contains documentation files:

- `ReadMe.md` — The philosophy begind BioLogics
- `spec_v0_1.md` — Language specification
- `examples.md` — Explanation of examples
- `architecture.md` — This file
- `Manifesto.md` — An accessible explanation of the logistics behing BioLogics


---

### 11. `__init__.py`
Marks the directory as a **Python package**.

**Purpose:**
- Allows importing modules like `from biologics.organism import Organism`
- Keeps the package organized for both local use and eventual pip installation.

---

## Summary

BioLogics is structured to separate concerns:

- **Organism lifecycle** → `organism.py`
- **Execution engine** → `interpreter.py`, `vm.py`
- **Data mappings** → `codons.py`, `semantic_map.py`
- **Real biological integration** → `biology.py`, `genbank.py`
- **Mutation / evolution** → `mutation.py`
- **Examples and documentation** → `examples/`, `docs/`

This modular design allows **safe experimentation**, **symbolic and real gene execution**, and future extensions like population-level evolution or AI-driven genome generation.
