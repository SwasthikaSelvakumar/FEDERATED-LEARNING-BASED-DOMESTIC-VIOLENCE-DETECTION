import numpy as np
from tensorflow.keras import layers, models

def build_model(input_shape=(40,)):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Dense(64, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(3, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

# ✅ Directly convert NumPy arrays → Python lists for JSON
def weights_to_numpy(model):
    return [w.astype(float).tolist() for w in model.get_weights()]

# ✅ Convert lists back → NumPy arrays
def set_weights_from_numpy(model, numpy_weights):
    model.set_weights([np.array(w, dtype=np.float32) for w in numpy_weights])
