# BioLogics — A Bio-Inspired Programming Language

BioLogics is an experimental **programming language and artificial life system** inspired by **genetics and protein semantics**. Programs are written as DNA sequences, executed as “living organisms,” and can mutate, reproduce, or even execute real biological genes.

This repository contains the **v0.1 reference implementation**, examples, and documentation for exploring artificial life, emergent behavior, and computational evolution.

---

## Table of Contents

- [Concept](#concept)
- [Execution Modes](#execution-modes)
- [Organisms & Genomes](#organisms--genomes)
- [Virtual Machine](#virtual-machine)
- [Mutation & Reproduction](#mutation--reproduction)
- [Real Biology Integration](#real-biology-integration)
- [Project Architecture](#project-architecture)
- [Examples](#examples)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Future Directions](#future-directions)

---

## Concept

- **Programs are living organisms:** Each DNA string (genome) encodes a sequence of instructions.
- **Computation is embodied:** Instructions consume energy, organisms may die mid-execution, and failure is expected.
- **Mutation is natural:** Genomes can mutate, producing variation and emergent behavior.
- **Real biology connection:** Real genes can be executed in semantic mode to explore AI-driven bio-inspired computation.

BioLogics is not about “correct outputs,” but about **existence, behavior, and evolution**.

---

## Execution Modes

1. **Symbolic Mode (default)**  
   - Genome interpreted as codons.
   - Codons mapped to abstract instructions using `codons.py`.
   - For hand-written genomes and experiments.

2. **Real Biology Mode (`mode="real"`)**  
   - Genome translated into amino acids via `biology.py`.
   - Amino acids mapped to semantic behaviors (`semantic_map.py`).
   - Allows running real genes or mutated sequences.

Both modes use the same organism model, VM, and energy-based execution.

---

## Organisms & Genomes

- **Genome:** String of DNA bases (`A`, `T`, `G`, `C`).  
- **Energy:** Each instruction consumes energy. Energy depletion = death.  
- **START / STOP codons:** Define the Open Reading Frame (ORF) for execution.  

```python
from biologics.organism import Organism
organism = Organism(genome="ATGAAAAGGGCCCCCTAA", energy=10)
````

* **Mutation:** Introduced via `mutation.py`. Single-base substitutions or planned reproduction.

---

## Virtual Machine

* Stack-based execution engine (`vm.py`) handles instructions:

  * Arithmetic: `ADD`, `SUB`, `MUL`, `DIV`
  * Stack operations: `PUSH_1`, `PUSH_2`
  * Output: `PRINT`
* Safe execution: handles empty stacks and invalid instructions gracefully.

---

## Mutation & Reproduction

* **Point Mutation:** Random single-base change.
* **Population-level simulation:** Offspring inherit genomes with possible mutations.
* **Energy cost:** Reproduction consumes energy.
* **Emergent evolution:** Over multiple generations, genomes diversify and behavior evolves.

---

## Real Biology Integration

* **GenBank Access:** Fetch real gene sequences with `genbank.py`.
* **DNA → Protein Translation:** Biopython used to translate DNA into amino acids.
* **Semantic Mapping:** Amino acids mapped to behaviors in BioLogics.
* **AI-driven experimentation:** Real genes can be mutated and executed to explore emergent properties.

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

* **Modular design** ensures safety, extensibility, and separation of concerns.

---

## Examples

| Example                    | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| `hello_life.py`            | Minimal organism that consumes energy, prints output, and dies. |
| `broken_frame.py`          | Demonstrates open reading frame errors and stack underflow.     |
| `starvation.py`            | Organism dies due to insufficient energy.                       |
| `mutation_experiment.py`   | Tests point mutation effects on behavior.                       |
| `silent_organism.py`       | Organism with no START codon; shows silent behavior.            |
| `conditional_life.py`      | Demonstrates conditional instructions in symbolic mode.         |
| `real_gene.py`             | Runs a real gene in real biology mode.                          |
| `genbank_gene.py`          | Fetches a gene from GenBank and executes it.                    |
| `ai_mutation_study.py`     | Explores AI-proposed genome mutations.                          |
| `mutation_playground.py`   | Safe environment for mutation experiments.                      |
| `population_simulation.py` | Multi-organism evolution with mutations and energy dynamics.    |
| `real_gene_mutation.py`    | Mutates real genes and observes semantic behavior.              |

---

## Getting Started

1. **Clone the repository** and navigate into it:

```bash
git clone <repo-url>
cd biologics_project
```

2. **Create a virtual environment** (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install biopython matplotlib
```

4. **Run an example**:

```bash
python3 biologics/examples/hello_life.py
```

Expected output:

```
[organism output] 3
[organism terminated normally]
```

---

## Dependencies

* Python 3.10+
* [Biopython](https://biopython.org/)
* [Matplotlib](https://matplotlib.org/) (for plotting population or evolutionary data)

```

---

## Future Directions

* **Expanded instruction set** (more codons and behaviors)
* **Multiple ORFs per genome**
* **Regulatory sequences (non-coding DNA)**
* **Reproduction with mutation and AI-driven evolution**
* **Graphical population evolution visualization**
* **Integration with real genes for semantic behavior analysis**

---

BioLogics is **experimental and evolving**, designed to **grow through exploration** rather than rigid guarantees. Code is not just written — it is **grown, mutated, and observed**.

```
