## Installation: ##

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


### Local build

    docker build -t docker.io/opl242/opl_star_app .
    docker run -p 5000:5000 docker.io/opl242/opl_star_app:latest


#### Load from Docker Hub

    docker pull docker.io/opl242/opl_star_app

## Usage: ##


    Usage: make_prediction.py [OPTIONS]

    Options:
    --ip TEXT              Server IP
    --port INTEGER         Server port
    --temperature INTEGER  Temperature (K)
    --luminocity FLOAT     Luminosity(L/Lo)
    --radius FLOAT         Radius(R/Ro)
    --magnitude FLOAT      Absolute magnitude(Mv)
    --type INTEGER         Star type
    --color TEXT           Star color
    --help                 Show this message and exit.
    
Usage example:

    python make_prediction.py --temperature=3068 --luminocity=0.17 --radius=16.12 --type=0 --color="red"
    "M"

## Tets: ##

    pytest -v tests\



## Оптимизация образа Docker ##

Следующие шаги помолги уменьшить размер образа с полутора Гб до 511 Mb:

1. Выбор базового образа. Образы с суффиксом slim для Python 3.2. Отключение cache для pip.
3. Использование .dockerignore.
4. Объединение команд в цепочку.
