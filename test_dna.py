# https://rosalind.info/problems/dna/

def count_bases(dna):
    a = dna.count("A")
    c = dna.count("C")
    g = dna.count("G")
    t = dna.count("T")
    return f"{a} {c} {g} {t}"


def test_count_bases():
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    expected = "20 12 17 21"
    actual = count_bases(dna)
    assert expected == actual


if __name__ == "__main__":
    with open("test_data/rosalind_dna.txt") as file:
        dna = file.read()
        print(count_bases(dna))
