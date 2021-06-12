import pytest


@pytest.mark.parametrize(
    "temperature, luminocity, radius, magnitude, type, color", [
    (3068, 0.0024, 0.17, 16.12, 0, "red"),
    (3042, 0.0005, 0.1542, 16.6, 0, "red"),
    (2600, 0.0003, 0.102, 18.7, 0, "white"),
    (2800, 0.0002, 0.16, 16.65, 0, "white"),
    (1939, 0.000138, 0.103, 20.06, 0, "blue")
])
def test_online_inference_1(
    client, temperature, luminocity, radius, magnitude, type, color
):

    rv = client.get('/predict', json={
        "temperature": temperature,
        "luminocity": luminocity,
        "radius": radius,
        "magnitude": magnitude,
        "type": type,
        "color": color,
    }, follow_redirects=True)

    assert 200 == rv.status_code

@pytest.mark.parametrize(
    "temperature, luminocity, radius, magnitude, type, color", [
    ("0.11", 0.0024, 0.17, 16.12, 0, "red"),
    (3042, "DFEG", 0.1542, 16.6, 0, "red"),
    (2600, 0.0003, "QQQ", 18.7, 0, "white"),
    (2800, 0.0002, 0.16, "fsdfjl", 0, "white"),
    (1939, 0.000138, 0.103, 20.06, "34.3", "blue"),
    (1939, 0.000138, 0.103, 20.06, 34.3, 242)
])
def test_online_inference_incorrect_1(
    client, temperature, luminocity, radius, magnitude, type, color
):

    rv = client.get('/predict', json={
        "temperature": temperature,
        "luminocity": luminocity,
        "radius": radius,
        "magnitude": magnitude,
        "type": type,
        "color": color,
    }, follow_redirects=True)

    assert 400 == rv.status_code