
complement_nucleotides = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}

def complement_sequence(seq):
    """
    Returns the complement of the dna sequence.

    Args:
        -seq (str): a DNA sequence

    Returns:
        -complement (str): the reverse complement of the sequence.
    """
    try:
        return ''.join(complement_nucleotides[nt] for nt in seq[::-1].upper())
    except KeyError:
        raise ValueError("Invalid nucleotide in sequence")
