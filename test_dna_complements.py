# https://rosalind.info/problems/revc/

def complementary_dna_strand(dna: str):
    reversed_strand = dna[::-1].replace("\n", "")
    complements = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"}

    return "".join(oldBase if oldBase not in reversed_strand else complements[oldBase] for oldBase in reversed_strand)


def test_complementary_dna_strand():
    dna = "AAAACCCGGT"
    expected = "ACCGGGTTTT"
    actual = complementary_dna_strand(dna)
    assert expected == actual


if __name__ == "__main__":
    with open("test_data/rosalind_revc.txt") as file:
        dna = file.read()
        print(complementary_dna_strand(dna))
