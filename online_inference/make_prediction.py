import click
import requests


def make_prediction(
    ip: str, port: int, temperature: int, luminocity: float,
    radius: float, magnitude: float, type: int, color: str
):

    url = f"http://{ip}:{port}/predict"

    payload = {
        "temperature": f"{temperature}",
        "luminocity": f"{luminocity}",
        "radius": f"{radius}",
        "magnitude": f"{magnitude}",
        "type": f"{type}",
        "color": f"{color}"
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, json=payload, headers=headers)

    print(response.text)


@click.command()
@click.option(
    "--ip", type=str, default='127.0.0.1',
    help="Server IP"
)
@click.option(
    "--port", type=int, default=5000,
    help="Server port"
)
@click.option(
    "--temperature", type=int, default=10000,
    help='Temperature (K)'
)
@click.option(
    "--luminocity", type=float, default=1000.0,
    help='Luminosity(L/Lo)'
)
@click.option(
    "--radius", type=float, default=1000.0,
    help='Radius(R/Ro)'
)
@click.option(
    "--magnitude", type=float, default=0.0,
    help='Absolute magnitude(Mv)'
)
@click.option(
    "--type", type=int, default=3,
    help='Star type'
)
@click.option(
    "--color", type=str, default='red',
    help='Star color'
)
def main(*arg, **kwarg):
    make_prediction(*arg, **kwarg)


if __name__ == "__main__":
    main()