

complement_nucleotides = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}

def complement_sequence(seq):
    """
    Returns the complement of the dna sequence.

    Args:
        -seq (str): a DNA sequence

    Returns:
        -complement (str): the reverse complement of the sequence.
    """
    return ''.join(complement_nucleotides[nt] for nt in seq[::-1].upper())


def test_complement_seq():
    assert complement_sequence("GCA") == 'TGC'

def test_complement_seq2():
    assert complement_sequence("GGG") == 'CCC'

def test_complement_seq3():
    assert complement_sequence("ATGCAGT") == 'ACTGCAT'

def test_complement_upper():
    assert complement_sequence("atc") == 'GAT'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

