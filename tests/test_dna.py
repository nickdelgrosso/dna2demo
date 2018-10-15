from dna import complement_sequence
import pytest


@pytest.mark.parametrize("seq,comp", [('TGC', 'GCA'), ('CCC', 'GGG'), ('ACTGCAT', 'ATGCAGT')])
def test_complement_seq(seq, comp):
    assert complement_sequence(seq) == comp


def test_complement_upper():
    assert complement_sequence("atc") == 'GAT'


def test_complement_invalid():
    with pytest.raises(ValueError):
        complement_sequence('GTB')