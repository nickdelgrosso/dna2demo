

complement_nucleotides = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}

def complement_sequence(seq):
    """
    Returns the complement of the dna sequence.

    Args:
        -seq (str): a DNA sequence

    Returns:
        -complement (str): the reverse complement of the sequence.

    Examples:
    >>> complement_sequence("GCA")
    'TGC'

    >>> complement_sequence('GGG')
    'CCC'

    >>> complement_sequence('ATGCAGT')
    'ACTGCAT'

    >>> complement_sequence('atc')
    'GAT'

    """
    return ''.join(complement_nucleotides[nt] for nt in seq[::-1].upper())




if __name__ == '__main__':
    import doctest
    doctest.testmod()

