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

.. list-table::

   * - Переменная
     - Обязательная
     - Значение по-умолчанию
     - Описание
   * - DEBUG
     - нет
     - true
     - Включить режим отладки SQL запросов
   * - ADMIN_PASSWORD
     - да
     - admin
     - Изначальный пароль администратора
   * - SESSION_KEY
     - нет
     - secret
     - Ключ для сессии - случайная строка
   * - GIN_MODE
     - нет
     - release
     - Параметр для управления отладкой библиотеки gin и вывода диагностических сообщений веб приложения
   * - INCLUDE_ORIGIN_SUFFIXES
     - нет
     - "nextgis.com", "nextgis.ru"
     - Массив origin который добавляется к тем что указаны в API ключе
   * - TOKEN_CACHE_SIZE
     - нет
     - 1024
     - Максимальное количество токенов авторизации в кэше
   * - TIMEOUT
     - нет
     - 180
     - Таймаут сетевых запросов
   * - FILE_TIMEOUT
     - нет
     - 1800
     - Таймаут на скачивание файла
   * - SESSION_MAX_AGE
     - нет
     - 259200
     - Время жизни сессии веб приложения
   * - HTTP_SKIP_SSL_VERIFY
     - нет
     - false
     - Не проверять https сертификаты
   * - LDAP_LOGIN
     - нет
     - false
     - | Вход через ldap
       | Оставить по умолчанию
   * - LDAP_TLS
     - нет
     - no
     - Использовать TLS
   * - LDAP_URL
     - нет
     - “”
     - Адрес сервера LDAP
   * - LDAP_USER_FILTER
     - нет
     - (objectClass=posixAccount)
     - Фильтр поиска пользователей
   * - LDAP_USER_ATTR
     - нет
     - uid
     - Атрибут пользователя
   * - LDAP_GROUP_FILTER
     - нет
     - cn=geoservices
     - Фильтр поиск групп
   * - LDAP_GROUP_ATTR
     - нет
     - memberUid
     - Атрибут группы
   * - LDAP_DEFAULT_GROUP_ID
     - нет
     - 0
     - Группа по умолчания для LDAP пользователей - 0 выключено назначение групп
   * - LDAP_UPDATE_GROUPS
     - нет
     - false
     - Обновлять принадлежность пользователя к группе
   * - OAUTH2_LOGIN
     - нет
     - false
     - Разрешить вход через OAuth2
   * - OAUTH2_CLIENT_ID
     - нет
     - 
     - OAuth2 client ID
   * - OAUTH2_CLIENT_SECRET
     - нет
     - 
     - OAuth2 client secret
   * - OAUTH2_REDIRECT_URI
     - нет
     - 
     - OAuth2 redirect URI
   * - OAUTH2_ENDPOINT
     - нет
     - https://my.nextgis.com
     - Оконечная точка
   * - OAUTH2_SCOPE
     - нет
     - user_info.read
     - Скоуп
   * - OAUTH2_TYPE
     - нет
     - 1
     - Тип авторизации: 1-NextGIS ID, 2 - Keycloak, 3 - custom, 4 - Blitz
   * - OAUTH2_TOKEN_ENDPOINT
     - нет
     - https://my.nextgis.com/oauth2/token
     - Оконечная точка получения токена
   * - OAUTH2_AUTH_ENDPOINT
     - нет
     - https://my.nextgis.com/oauth2/authorize
     - Оконечная точка авторизации
   * - OAUTH2_USERINFO_ENDPOINT
     - нет
     - https://my.nextgis.com/api/v1/user_info
     - Оконечная точка получения информации о пользователе (в случае JWT не требуется)
   * - OAUTH2_INTROSPECTION_ENDPOINT
     - нет
     - https://my.nextgis.com/oauth2/introspect
     - Оконечная точка для интроспекции
   * - OAUTH2_PROFILE_SUBJ_ATTR
     - нет
     - nextgis_guid
     - Поле для получения идентификатора пользователя (subject)
   * - OAUTH2_PROFILE_KEYNAME_ATTR
     - нет
     - username
     - Поле для получения логина пользователя
   * - OAUTH2_PROFILE_FIRSTNAME_ATTR
     - нет
     - first_name
     - Поле для получения имени пользователя
   * - OAUTH2_PROFILE_LASTNAME_ATTR
     - нет
     - last_name
     - Поле для получения фамилии пользователя
   * - OAUTH2_USER_AUTOCREATE
     - нет
     - true
     - При первом входе создает пользователя
   * - OAUTH2_VALIDATE_KEY
     - нет
     - “”
     - Ключ для проверки подписи JWT
   * - OAUTH2_CREATE_GROUPS
     - нет
     - false
     - Создавать группы на основе ролей пользователей
   * - OAUTH2_UPDATE_GROUPS
     - нет
     - false
     - Обновлять состав групп на основе ролей пользователей
   * - OAUTH2_TOKEN_CACHE_TTL
     - нет
     - 3600
     - Время жизни токена по умолчанию в сек, если иное не возвращено сервером
   * - OAUTH2_LOGOUT_ENDPOINT
     - нет
     - “”
     - Оконечная точка для разлогина
   * - OAUTH2_GROUPS_JWT_KEY
     - нет
     - resource_access/{client_id}/roles
     - Путь поиска ролей/групп в JWT токене
   * - LOCAL_LOGIN
     - нет
     - true
     - Разрешить локальные учетные записи
   * - DEFAULT_LANGUAGE
     - нет
     - en
     - Язык по умолчанию
   * - LOG
     - нет
     - false
     - Выводить в stdout сообщения в структурированном формате
   * - LOG_ONLY_EDITS
     - нет
     - false
     - Выводить в stdout сообщения только при модификации данных
   * - CLOUD_MODE
     - нет
     - false
     - Режим запуска в облаке
   * - MAX_AGE
     - нет
     - 43200
     - Длительность хранения тайлов в браузере пользователя - 12 часов
   * - EXT_TMS_SUPPORT
     - нет
     - false
     - Включить поддержку внешних сервисов TMS
   * - 
     - нет
     - https://geoservices.nextgis.com
     - Адрес сервиса интеграции с ПКК
   * - PKK_EXTERNAL_APIKEY
     - нет
     - “”
     - APIKey для взаимодействия с сервисом интеграции с ПКК
   * - PKK_TILES_URL
     - нет
     - “”
     - Адрес локального сервиса интеграции с ПКК
   * - PKK_FEATURES_URL
     - нет
     - “”
     - Адрес локального сервиса интеграции с ПКК
   * - PKK_MIN_ZOOM
     - нет
     - 3
     - Минимальный уровень увеличения тайлов ПКК
   * - PKK_MAX_ZOOM
     - нет
     - 18
     - Максимальный уровень увеличения тайлов ПКК
   * - PKK_REGION
     - нет
     - MULTIPOLYGON (((-168.4 84,-168.4 50,-179.999999 50,-179.9999999 84,-168.4 84)),((130 40,130 84,179.999999 84,179.999999 40,130 40)),((129.999999 84,129.999999 47,82.5 47,82.5 84,129.999999 84)),((82.4999999 50,50 50,50 84,82.4999999 84,82.4999999 50)),((20 84,49.999999 84,49.999999 40,20 40,20 84)))
     - Территория для запросов тайлов ПКК
   * - DB_TYPE
     - да
     - sqlite3
     - Тип БД - sqlite3, postgres, mysql
   * - DB_USER
     - нет
     - geoservices
     - Пользователь из под которого будет выполнено подключение к БД
   * - DB_PASSWORD
     - да
     - 
     - Пароль от БД
   * - DB_HOST
     - да
     - localhost
     - Адрес БД
   * - DB_PORT
     - да
     - 5432
     - Порт БД
   * - DB_NAME
     - нет
     - geoservices
     - Имя БД
   * - DB_MAXCONN
     - нет
     - 50
     - Максимальное количество подключений
   * - DB_MAXIDLECONN
     - нет
     - 10
     - Максимальное количество свободных подключений
   * - DB_SSL_MODE
     - нет
     - 
     - | disable - I don't care about security, and I don't want to pay the overhead of encryption.
       | allow - I don't care about security, but I will pay the overhead of encryption if the server insists on it.
       | prefer - I don't care about encryption, but I wish to pay the overhead of encryption if the server supports it.
       | require - I want my data to be encrypted, and I accept the overhead. I trust that the network will make sure I always connect to the server I want.
       | verify-ca - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server that I trust.
       | verify-full - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server I trust, and that it's the one I specify.



