# BioLogics v0.1 — Formal Specification & Overview

## 1. What Is BioLogics?

**BioLogics** is an experimental programming language and artificial life system inspired by biological genetics.

In BioLogics, programs are not abstract scripts — they are **organisms**.  
They are written as **genomes**, executed under **energy constraints**, subject to **mutation**, and capable of **failure or death**.

BioLogics explores computation as **embodied, fragile, and emergent**, rather than deterministic and guaranteed.

> **Execution is biological, not guaranteed.**

---

## 2. Core Design Principles

- Programs are organisms, not static code  
- Genomes are primary — all behavior emerges from sequence  
- Execution is embodied — energy is consumed per operation  
- Failure is natural — organisms may fail silently or die  
- Mutation is first-class — variation is expected, not exceptional  
- Biology is both inspiration and data source  
- Correctness is less important than behavior  

---

## 3. Alphabet & Genome Model

### 3.1 Alphabet

BioLogics uses the DNA alphabet:

A C G T


### 3.2 Genome

A **genome** is a string of DNA bases.  
It may be:

- **Symbolic** (engineered by humans)
- **Real** (biological DNA from databases)

Genomes are read left-to-right in **non-overlapping codons** (triplets).

---

## 4. Codons & Open Reading Frames (ORFs)

### 4.1 Codons

- A **codon** = 3 DNA bases  
- Codons are the smallest executable unit  
- Codons outside execution regions are ignored  

### 4.2 START and STOP

Execution only occurs inside an **open reading frame**:

- Execution begins after a **START** signal  
- Execution ends at **STOP** or organism death  
- Absence of START may result in silent organisms  

This mirrors biological transcription.

---

## 5. Execution Modes (v0.1)

BioLogics supports **two execution modes**.

### 5.1 Symbolic Mode (default)

- Genome interpreted as codons  
- Codons mapped to abstract instructions  
- Designed for experimentation and hand-written genomes  

### 5.2 Real Biology Mode (`--real`)

- Genome interpreted as real DNA  
- DNA translated into amino acids using standard codon tables  
- Amino acids mapped to BioLogics semantic behaviors 
- In real mode, we insert one extra biological layer 
- Designed for executing real genes 

A real gene becomes:

- an organism whose protein sequence drives behavior
- mutations change amino acids
- amino acid changes change behavior

Both modes share:
- Organism model  
- Energy model  
- Virtual machine  
- Mutation mechanisms  

---

## 6. Translation Layers

### 6.1 Symbolic Translation

DNA codon → Amino Acid → Instruction


Defined in `codons.py`.

Multiple codons may map to the same amino acid, enabling **silent mutations**.

### 6.2 Real Biological Translation

DNA → Amino Acids → Semantic Behaviors


Implemented using **Biopython**.

---

## 7. Amino-Acid–Based Semantics

Amino acids define **behavioral meaning**, not low-level instructions.

### Example Semantic Categories

- Initiation  
- Energy storage / release  
- Computation  
- Structural stability  
- Conditional logic  
- Replication (planned)  
- Termination  

Multiple amino acids may map to the same semantic.  
Some amino acids map to **no behavior** (neutrality).

---

## 8. Symbolic Codon Table (v0.1)

### Structural Codons

| Codon | Amino Acid | Instruction |
|------|-----------|-------------|
| ATG  | Methionine | START |
| TAA  | Stop       | STOP |
| TAG  | Stop       | STOP |
| TGA  | Stop       | STOP |

### Lysine — Constants

| Codon | Instruction | Value |
|------|-------------|-------|
| AAA  | PUSH        | 1 |
| AAG  | PUSH        | 2 |

### Glycine — Arithmetic

| Codon | Instruction |
|------|-------------|
| GGC  | ADD |
| GGT  | SUB |
| GGA  | MUL |
| GGG  | DIV |

### Proline — Output

| Codon | Instruction |
|------|-------------|
| CCC  | PRINT |

---

## 9. Formal Grammar

program ::= noncoding* start gene+ stop noncoding*
start ::= "ATG"
stop ::= "TAA" | "TAG" | "TGA"
gene ::= codon codon codon*
codon ::= base base base
base ::= "A" | "C" | "G" | "T"
noncoding ::= codon


### Semantic Rules

- Execution begins immediately after START  
- Execution halts at first STOP  
- Codons outside ORFs are ignored  
- Redundant codons enable silent mutation  

---

## 10. Virtual Machine (VM)

The BioLogics VM is **minimal and forgiving**.

### VM State

- Stack (LIFO)  
- Memory register  
- Implicit instruction pointer  

### Supported Behaviors (non-exhaustive)

- PUSH  
- ADD / SUB / MUL / DIV  
- STORE  
- PRINT  
- IF / NOOP  
- REPLICATE (planned)  

Invalid instructions do not crash execution.

---

## 11. Energy Model

- Each executed behavior consumes energy  
- Energy depletion causes organism death  
- Death halts execution immediately  
- Energy introduces **selection pressure**  

---

## 12. Mutation Model

### 12.1 Point Mutation

- Single-base substitution  
- Random position  
- Always changes base  

### 12.2 Mutation Effects

- Neutral  
- Behavioral  
- Lethal  

Mutation applies equally to symbolic and real genomes.

---

## 13. Reproduction Model (Planned)

- Organisms may reproduce  
- Offspring genome may mutate  
- Reproduction consumes energy  
- Enables population-level evolution  

---

## 14. AI Integration (Exploratory)

AI systems may:

- Propose mutations  
- Generate genomes  
- Analyze fitness landscapes  

AI does **not** control execution — it participates in evolutionary exploration.

---

## 15. Example: Hello, Life

### Genome

ATG AAA AAG GGC CCC TAA


### Interpretation

START
PUSH 1
PUSH 2
ADD
PRINT
STOP


### Output

[organism output] 3
[organism terminated normally]


---

## 16. File Architecture

biologics/
├── organism.py
├── interpreter.py
├── vm.py
├── codons.py
├── semantic_map.py
├── biology.py
├── mutation.py
├── genbank.py
│
├── examples/
│ ├── hello_life.py
│ ├── silent_organism.py
│ ├── conditional_life.py
│ ├── mutation_experiment.py
│ ├── real_gene.py
│ └── ai_mutation_study.py
│ └── broken_frame.py
│ └── starvation.py
│ └── real_gene.py
│ └── real_gene_mutation.py
│ └── mutation_playground.py
│ └── population_simulation.py
│ └── genbank_gene.py
│
└── docs/
└── ReadMe.md
└── Examples.md


---

## 17. Installation

### Requirements

- Python 3.10+
- Biopython

```
pip install biopython
```

## 18. Philosophy

BioLogics treats programs not as correct instructions, but as living structures.

Code is metabolism

Output is behavior

Termination is death

Mutation is creativity

Code is not written. It is grown.

## 19. Status

BioLogics v0.1 is experimental and evolving.
The language is designed to grow through exploration, not rigid guarantees.
