from tensorflow import Sequential
from tensorflow import Conv1D, MaxPooling1D, Flatten, Dense, \
    Dropout


def build_cnn_model(input_shape=(500, 20)):
    """Defines a CNN model for protein structure prediction."""
    model = Sequential([
        Conv1D(filters=64, kernel_size=3,
               activation='relu', input_shape=input_shape),
        MaxPooling1D(pool_size=2),
        Conv1D(filters=128, kernel_size=3, activation='relu'),
        MaxPooling1D(pool_size=2),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.3),
        # Output: 3 classes (helix, sheet, coil)
        Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    return model


if __name__ == "__main__":
    model = build_cnn_model()
    model.summary()
