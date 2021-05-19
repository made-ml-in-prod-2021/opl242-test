# opl242-test

# Project for MADE 2021 #

MADE profile link:
https://data.mail.ru/profile/a.opolchenov/

## Installation:##

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


## Usage: ##

    python predict_online.py [OPTIONS]

    Options:
    --temperature   int     Temperature (K)
    --luminosity    float   Luminosity(L/Lo)
    --radius        float   Radius(R/Ro)
    --magnitude     float   Absolute magnitude(Mv)
    --type          int     Star type
    --color         str     Star color
    
## Tets: ##

    pytest -v tests\
