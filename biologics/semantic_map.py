# Amino acid → semantic behavior

AMINO_ACID_SEMANTICS = {
    # Initiation / termination
    "M": "START",    # Methionine
    "*": "STOP",     # Stop codon

    # Arithmetic / computation
    "G": "ADD",      # Glycine
    "A": "PUSH_1",   # Alanine
    "V": "PUSH_2",   # Valine

    # Output
    "P": "PRINT",    # Proline

    # Neutral / structural (do nothing)
    "L": None,
    "I": None,
    "S": None,
    "T": None,
    "C": None,
    "Y": None,
    "F": None,
    "H": None,
    "K": None,
    "R": None,
    "D": None,
    "E": None,
    "N": None,
    "Q": None,
    "W": None,
}

#Most amino acids do nothing
#This creates robustness, neutral mutations, and biological realism
