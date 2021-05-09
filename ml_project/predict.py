from pathlib import Path
import pandas as pd
import pickle


def predict(model_path: Path, path_to_X: Path):
    with open(model_path, "rb") as fin:
        model = pickle.load(fin)
    X = pd.read_csv(path_to_X)
    y = model.predict(X)
    return y