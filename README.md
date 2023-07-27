# API-Moviebook
Esta es una API construída con FASTAPI para realizar operaciones CRUD en un inventario de películas, se usa una base de datos de PostgreSQL para el almacenamiento de los datos de películas y se usa Redis para el almacenamiento en caché de los request para no realizar consultas nuevamente a la base de datos si esta no se ha modificado, además se usa para la validación del token de autenticación con JWT. Se usa por último en producción nginx para redirigir el tráfico de nivel 7 de la aplicación.
Los usuarios podrían buscar, reservar, actualizar y eliminar películas. 

## Getting-started
Primero dedes asegurarte de crear un archivo `.env` el cual puede verse como el siguiente ejemplo:
```
# Contenido del archivo .env
# Base de datos PostgreSQL
DATABASE_NAME=movieapi
DATABASE_USER=adminmovieapi
DATABASE_PASSWORD=passmovieapi
DATABASE_HOST=db
DATABASE_PORT=5432
#Redis
REDIS_HOST=redis
REDIS_PORT=6379
# Secrets jwt
EMAIL=admin@gmail.com
PASSWORD=admin
```

Este es un ejemplo para usar la API en donde se encuentran las configuraciones de la base de datos de postgreSQL y de redis y además tiene las configuraciones necesarias para realizar la validación de la API usando JWT.

## Correr pruebas con docker-compose

Para probar la api primero puedes usar el archivo `docker-compose.yaml`

```
docker-compose up 
```

Este primer paso nos sirve para asegurarnos de que nginx está redirigiendo bien el tráfico de la API que corre en el puerto `8000` con `uvicorn`

## Desplegar en Kubernetes
Los archivos que se encuentran en la carpeta k8s deben ser aplicados en el cluster de Kubernetes en el siguiente orden:

configMap.yaml: Este archivo contiene las configuraciones necesarias para la aplicación y Nginx.

```shell
kubectl apply -f configMap.yaml
```

secrets.yaml: Este archivo almacena los datos sensibles como contraseñas y tokens de forma segura.

```shell
kubectl apply -f secrets.yaml
```

volumes.yaml: Este archivo describe el volumen persistente que será utilizado por el contenedor de PostgreSQL para almacenar los datos.

```shell
kubectl apply -f volumes.yaml
```

deployment.yaml: Este archivo contiene las especificaciones para el despliegue de la aplicación, la base de datos PostgreSQL, Redis y Nginx.

```shell
kubectl apply -f deployment.yaml
```

service.yaml: Este archivo define los servicios que permitirán la comunicación entre los contenedores y expondrá la aplicación al mundo exterior.

```shell
kubectl apply -f service.yaml
```

Espera unos momentos para que los servicios y despliegues se pongan en marcha. Para verificar el estado de los pods, puedes usar el siguiente comando:

```shell
kubectl get pods
```

Una vez que todos los pods estén en estado Running, puedes obtener la dirección IP externa del servicio usando el siguiente comando:

```
kubectl get svc myapp-service
```

El resultado de este comando te proporcionará la dirección IP en la que puedes acceder a la aplicación.

Por favor, ten en cuenta que la dirección IP puede variar dependiendo del proveedor de la nube que estés utilizando. En algunos casos, puede que necesites configurar un Ingress en lugar de un LoadBalancer. Consulta la documentación de tu proveedor de la nube para más detalles.




