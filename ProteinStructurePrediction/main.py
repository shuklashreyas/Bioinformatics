from fetch_data import fetch_protein_sequence
from predict import predict_structure


def main():
    """Runs the full pipeline."""
    protein_id = "P69905"
    sequence = fetch_protein_sequence(protein_id)
    print("Protein Sequence:", sequence)

    prediction = predict_structure(sequence)
    print("Predicted Structure:", prediction)


if __name__ == "__main__":
    main()
