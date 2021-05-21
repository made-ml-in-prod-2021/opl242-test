from ml_project.models.predict_model import predict_model


def test_predict_model_1(dummy_trained_model, random_data_x):
    y_pred = predict_model(dummy_trained_model, random_data_x)
    assert y_pred.shape[0] == random_data_x.shape[0]