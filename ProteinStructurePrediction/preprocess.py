import numpy as np

amino_acids = "ACDEFGHIKLMNPQRSTVWY"
aa_to_index = {aa: i for i, aa in enumerate(amino_acids)}


def encode_sequence(seq, max_len=500):
    """Encodes an amino acid sequence as a one-hot matrix."""
    encoded = np.zeros((max_len, len(amino_acids)))
    for i, aa in enumerate(seq[:max_len]):
        if aa in aa_to_index:
            encoded[i, aa_to_index[aa]] = 1
    return encoded


if __name__ == "__main__":
    test_seq = "MKTLLLTLVVVTIVCLDLGYT"
    encoded = encode_sequence(test_seq)
    print("Encoded Shape:", encoded.shape)
