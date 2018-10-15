from dna import complement_sequence


def test_complement_seq():
    assert complement_sequence("GCA") == 'TGC'


def test_complement_seq2():
    assert complement_sequence("GGG") == 'CCC'


def test_complement_seq3():
    assert complement_sequence("ATGCAGT") == 'ACTGCAT'


def test_complement_upper():
    assert complement_sequence("atc") == 'GAT'