<h2 align="center">PySoNet by Django</h2>

Социальная сеть на Django Rest Framework.

## Start

#### 1) Create an image

    docker-compose build

##### 2) Launch container

    docker-compose up
    
##### 3) Go to address

    http://127.0.0.1:8000/api/v1/swagger/

## Developing with Docker

##### 1) Fork the repository

##### 2) Clone repository

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3)Create .env.dev in the root of the project

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=pysonet
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=pysonet
    POSTGRES_USER=pysonet_user
    POSTGRES_PASSWORD=pysonet_pass
    POSTGRES_HOST=pysonet-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    # Email
    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587
    
##### 4) Create an image

    docker-compose build

##### 5) Launch container

    docker-compose up
    
##### 6) Create a superuser

    docker exec -it pysonet_pysonet_back_1 python manage.py createsuperuser
                                                        
##### 7) If you need to clear the DB

    docker-compose down -v
 



