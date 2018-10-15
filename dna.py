
seq = "ACTGCA"


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
    """
    complements = []
    for nt in seq:
        if nt == 'G':
            comp = 'C'
        elif nt == 'C':
            comp = 'G'
        elif nt == 'A':
            comp = 'T'
        elif nt == 'T':
            comp = 'A'
        complements.append(comp)
    complements = complements[::-1]
    return ''.join(complements)




if __name__ == '__main__':
    import doctest
    doctest.testmod()