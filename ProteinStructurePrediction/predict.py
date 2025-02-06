import numpy as np
from tensorflow import load_model
from preprocess import encode_sequence

model = load_model("../models/cnn_model.h5")


def predict_structure(seq):
    """Predicts protein structure from a sequence."""
    encoded_seq = encode_sequence(seq, max_len=500)
    encoded_seq = np.expand_dims(encoded_seq, axis=0)  # Add batch dimension
    prediction = model.predict(encoded_seq)
    structure_classes = ["Helix", "Sheet", "Coil"]
    return structure_classes[np.argmax(prediction)]


if __name__ == "__main__":
    test_seq = "MKTLLLTLVVVTIVCLDLGYT"
    print("Predicted Structure:", predict_structure(test_seq))
