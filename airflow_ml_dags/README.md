# HW3

## Aiflow

Задание переменных окружения для mail alert:

    export MAIL_LOGIN=<user_name>
    export MAIL_PWD=<password>

Сборка и запуск контейнеров:

    export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
    
    docker-compose up --build

Запуск интерфейса в браузере:

    http://<server ip>:8082

Тестирование:

    pytest -v

