CODON_TABLE = {
    "ATG": ("Met", "START"),
    "TAA": ("Stop", "STOP"),
    "TAG": ("Stop", "STOP"),
    "TGA": ("Stop", "STOP"),
    "AAA": ("Lys", "PUSH_1"),
    "AAG": ("Lys", "PUSH_2"),
    "GGC": ("Gly", "ADD"),
    "GGT": ("Gly", "SUB"),
    "GGA": ("Gly", "MUL"),
    "GGG": ("Gly", "DIV"),
    "CCC": ("Pro", "PRINT"),
}
