import argparse
import numpy as np
import requests
from tensorflow.keras.utils import to_categorical
from model_utils import build_model, set_weights_from_numpy, weights_to_numpy

# ===============================
# Fake local dataset (for demo)
# ===============================
def load_local_dataset():
    X = np.random.rand(100, 40)  # 100 samples, 40 features
    y = np.random.randint(0, 3, size=(100,))  # 3 classes
    y = to_categorical(y, num_classes=3)
    return X, y

# ===============================
# Main federated client
# ===============================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", type=str, default="http://127.0.0.1:5000")
    parser.add_argument("--client_id", type=str, required=True)
    parser.add_argument("--epochs", type=int, default=2)
    args = parser.parse_args()

    print(f"🖥️ Starting Client {args.client_id}...")

    # 1. Get global weights from server
    r = requests.get(f"{args.server}/fl/get_model")
    if r.status_code != 200:
        print("❌ Failed to fetch global model. Server says:", r.text)
        exit(1)
    server_weights = [np.array(w) for w in r.json()["weights"]]

    # 2. Build model and set weights
    model = build_model()
    set_weights_from_numpy(model, server_weights)

    # 3. Train locally
    X, y = load_local_dataset()
    model.fit(X, y, epochs=args.epochs, batch_size=8, verbose=1)

    # 4. Send updated weights back
    client_weights = weights_to_numpy(model)
    r = requests.post(f"{args.server}/fl/update_model", json={"weights": client_weights})
    print("📡 Server response:", r.text)
