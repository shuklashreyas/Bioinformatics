import numpy as np
from model import build_cnn_model

# Example dummy dataset (replace with real data)
X_train = np.random.rand(1000, 500, 20)  # 1000 protein sequences
y_train = np.random.randint(0, 3, (1000, 3))  # 3 structure classes

model = build_cnn_model()
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Save trained model
model.save("../models/cnn_model.h5")
