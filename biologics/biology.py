from Bio.Seq import Seq

def translate_dna_to_protein(dna: str) -> str:
    """
    Translate a DNA sequence into a protein sequence using real biology.

    - Trims partial codons safely
    - Stops at STOP codon
    - Returns amino-acid string
    - Never raises errors during evolution loops
    """

    # Safety check
    if not isinstance(dna, str):
        return ""

    dna = dna.upper().strip()

    # Trim sequence to full codons
    remainder = len(dna) % 3
    if remainder != 0:
        dna = dna[:len(dna) - remainder]

    if len(dna) == 0:
        return ""

    try:
        seq = Seq(dna)
        protein = seq.translate(to_stop=True)
        return str(protein)
    except Exception:
        # Biological failure → silent failure (by design)
        return ""
