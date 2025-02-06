from Bio import Entrez, SeqIO

Entrez.email = "shukla.shre@northeastern.edu"


def fetch_protein_sequence(protein_id):
    handle = Entrez.efetch(db="protein", id=protein_id,
                           rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record.seq


protein_id = "P69905"  # Example: Hemoglobin Subunit Alpha
sequence = fetch_protein_sequence(protein_id)
print('sequence: ' + sequence)
