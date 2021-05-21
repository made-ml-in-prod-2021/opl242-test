import numpy as np

from ml_project.models.evaluate_model import evaluate_model


def test_evaluate_model_1(random_data_y):
    assert evaluate_model(random_data_y, random_data_y) == 1
    shuffled = random_data_y.copy().values
    np.random.shuffle(shuffled)
    assert 0 <= evaluate_model(random_data_y, shuffled) <= 1
