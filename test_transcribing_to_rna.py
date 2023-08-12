# https://rosalind.info/problems/rna/

def transcribe_dna_to_rna(dna: str):
    return dna.replace("T", "U")


def test_transcribe_dna_to_rna():
    dna = "GATGGAACTTGACTACGTAAATT"
    expected = "GAUGGAACUUGACUACGUAAAUU"
    actual = transcribe_dna_to_rna(dna)
    assert expected == actual


if __name__ == "__main__":
    with open("test_data/rosalind_rna.txt") as file:
        dna = file.read()
        print(transcribe_dna_to_rna(dna))
