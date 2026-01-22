from Bio import Entrez, SeqIO

Entrez.email = "scralowrealow@gmail.com"  # Replace with your email

def fetch_gene(accession: str, start: int = None, end: int = None) -> str:
    """
    Fetch a DNA sequence from GenBank.

    Parameters:
    - accession: GenBank accession ID
    - start: optional 1-based start position
    - end: optional 1-based end position

    Returns:
    - genome string (uppercase)
    """
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()

    genome = str(record.seq).upper()

    # Apply start/end slicing if provided
    if start is not None or end is not None:
        start_idx = start - 1 if start else 0
        end_idx = end if end else len(genome)
        genome = genome[start_idx:end_idx]

    return genome
