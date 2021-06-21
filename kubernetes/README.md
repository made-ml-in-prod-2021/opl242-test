# READ.me

Используется образ docker.io/opl242/opl-star-app, и его модификации:

docker.io/opl242/opl-star-app:v1 - версия из HW2
docker.io/opl242/opl-star-app:v2 - версия с задержкой 20 секунд и срубанием через минуту
docker.io/opl242/opl-star-app:v3 - версия без задержек и сбрубания, аналогичная v1, но с endpoint /health
docker.io/opl242/opl-star-app:v4 - с задержкой 20 секунд, без срубания

Для заливки образа в minikube, если это не прошло автоматически при применении манифеста:

    minikube ssh
    docker login
    docker pull docker.io/opl242/opl-star-app:v1

# k8s manifest

Описание манифестов:

online-inference-pod.yaml - приложение из HW2
online-inference-pod-resources.yaml - то же, с ограничением ресурсов
online-inference-pod-probes.yaml - то же, с проверкой доступности
online-inference-replicaset.yaml - то же, с набором реплик
online-inference-deployment-rolling-upgrade.yaml - деплоймент новой версии постепенной заменой
online-inference-deployment-blue-green.yaml - деплоймент новой версии с одновременным поднятием новых версий

Для применения манифеста:

    minikube kubectl -- apply -f online-inference-pod-replicaset.yaml

Для проброса порта до приложения: 

    minikube kubectl -- port-forward pod/opl-star-app 5000:5000

# HELM

В каталоге charts представлены конфиги для chart helm - configmap.yaml и deployment.yaml

Деплой:

    helm upgrade --install opl-star-app-service --namespace=opl-ns
    helm upgrade --install opl-star-app-service --namespace=opl-ns ./charts