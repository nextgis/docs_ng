.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.ru>

.. _docs_geoserv_prem_admin:

Инструкция администратора для NextGIS Geoservices
=====================================================

Введение
---------

В настоящей инструкции приведен порядок развертывания ПО NextGIS Geoservices. В качестве преимущественного способа развертывания и работы ПО предполагается использование технологии Docker и средство docker-compose. Все шаги необходимо выполнять в ОС на базе Linux.

.. _docs_geoserv_prem_admin_prep:

Подготовка
-----------

На подготовительном этапе необходимо получить исходные коды. Наиболее простой способ это сделать - склонировать из git репозитория:

	git clone --depth 1 https://gitlab.com/nextgis_private/geoservices.git
	cd geoservices

Далее необходимо собрать образ СУБД с поддержкой  PostGIS (например, с названием registry.nextgis.com/postgis:3.3.2):

	docker build -t registry.nextgis.com/postgis:3.3.2 basemap

На следующем шаге необходимо сформировать исходные данные для наполнения базовой картографической подложки:

	docker build -t prepare-data -f basemap/Dockerfile-prepare basemap
	docker run -it --rm -v $(pwd)/basemap:/work prepare-data

Собрать образ веб-приложения (например, с названием registry.nextgis.com/geoservices:2.5.0):

	docker build -t registry.nextgis.com/geoservices:2.5.0 .

.. _docs_geoserv_prem_admin_setup:

Настройка
----------

После успешной сборки всех образов и подготовки данных необходимо поправить docker-compose.yml:

* Исправить названия образов в соответствии с заданными при их сборке (тэг image) 
* Изменить переменную окружения SESSION_KEY на случайное текстовое значение (опциональное, если не указан или пустой - генерируется автоматически)
* Исправить переменные окружения DB_PASSWORD и POSTGRES_PASSWORD на новый пароль (значения должны совпадать во всех вхождениях)
* Исправить переменную окружения  ADMIN_PASSWORD на новый пароль
* Исправить переменные окружения  S3_ACCESS_KEY/MINIO_ACCESS_KEY и S3_SECRET_KEY/MINIO_SECRET_KEY на новые пароли (значения должны быть разными для *_ACCESS_KEY и *_SECRET_KEY)
* В команде запуска redis установить объем выделяемой памяти (не более доступной контейнеру, лучше на 1-2Гб меньше лимита). Например:

	nano docker-compose.yml

version: '3.7'
services:
  app:
    image: registry.nextgis.com/geoservices:2.5.0
    depends_on:
      - "postgis"
      - "postgres"
      - "redis"
      - "s3"
    environment:
      SESSION_KEY: 5n3zczvhe3v0
      DB_TYPE: postgres
      DB_HOST: postgres
      DB_PASSWORD: b0apciz6p3n9
      REDIS_ENDPOINT: redis:6379
      ADMIN_PASSWORD: admin
      BM_DB_HOST: postgis
      DEBUG: "false"
      GIN_MODE: release
      S3_ACCESS_KEY: 8lo5m0wcteuf
      S3_SECRET_KEY: rro48pbjh6o8
      S3_ENDPOINT: s3:9000
      S3_SSL: "false"
      S3_DEFAULT_STORAGE_CLASS: REDUCED_REDUNDANCY
      S3_BUCKET_PREFIX: tiles
      EXT_TMS_SUPPORT: "true"
    volumes:
      - data:/work
    ports:
      - 8088:8088
    restart: always


  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: b0apciz6p3n9
      POSTGRES_DB: geoservices
      POSTGRES_USER: geoservices
    volumes:
      - postgres:/var/lib/postgresql/data
    restart: always


  redis:
    image: redis:alpine
    command: "redis-server --maxmemory 20Gb --maxmemory-policy allkeys-lru --appendonly no"
    volumes:
      - redis:/data
    restart: always


  postgis:
    image: registry.nextgis.com/postgis:3.3.2
    environment:
      POSTGRES_PASSWORD: b0apciz6p3n9
      POSTGRES_DB: basemap
      POSTGRES_USER: geoservices
    volumes:
      - postgis:/var/lib/postgresql/data
    restart: always


  s3:
    image: minio/minio
    command: server /data
    environment:
      MINIO_ACCESS_KEY: 8lo5m0wcteuf
      MINIO_SECRET_KEY: rro48pbjh6o8
      MINIO_BROWSER: "false"
    volumes:
      - s3:/data
    restart: always


volumes:
  data: {}
  postgres: {}
  redis: {}
  s3: {}
  postgis: {}

Для интеграции с внешними геосервисами для получения данных ПКК необходимо в переменные окружения контейнера app добавить переменную PKK_EXTERNAL_APIKEY с API ключом из вашего профиля на https://geoservices.nextgis.com.

Для интеграции с NextGIS Web необходимо  в переменные окружения контейнера app добавить следующие переменные: NGW_URL, NGW_LOGIN, NGW_APIKEY.

	NGW_URL - адрес сервера NextGIS Web в виде схема-домен-порт
NGW_LOGIN и NGW_APIKEY - логин и пароль для доступа к NextGIS Web из сервиса для формирования изображений тайлов. У пользователя должны быть доступ на чтение к данным которые требуется кэшировать в геосервисах. 

.. _docs_geoserv_prem_admin_launch:

Запуск
---------

Для запуска и проверки корректности работы стэка необходимо выполнить:

	docker-compose up

Для запуска в режиме сервиса:

	docker-compose up -d

После запуска в браузере открыть адрес сервиса с указанием порта 8088. Например,

	http://localhost:8088

.. _docs_geoserv_prem_admin_var:

Приложение: полный список переменных окружения NextGIS Geoservices
-------------------------------------------------------------------
