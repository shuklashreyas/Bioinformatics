import matplotlib.pyplot as plt
from tensorflow import load_model


def plot_training_history(history):
    """Plots training loss and accuracy."""
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    model = load_model("../models/cnn_model.h5")
    history = model.history.history  # Load training history
    plot_training_history(history)
