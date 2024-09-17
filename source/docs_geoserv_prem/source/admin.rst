.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.ru>

.. _docs_geoserv_prem_admin:

Administrator manual for NextGIS GeoServices
=====================================================

Introduction
---------

This manual describes the process of deploying NextGIS GeoServices sowftware on-premise. Mainly it uses Docker platform and docker-compose tool. All steps are performed on Linux-based OS.

.. _docs_geoserv_prem_admin_prep:

Preparation
-----------

First you need to get source codes. The easiest way is to clone them from a git repository:

.. code-block::

	git clone --depth 1 https://gitlab.com/nextgis_private/geoservices.git
	cd geoservices

Next build DBMS image with PostGIS support (name example: registry.nextgis.com/postgis:3.3.2):

.. code-block::

	docker build -t registry.nextgis.com/postgis:3.3.2 basemap

Next you need to prepare data for the basemap:

.. code-block::

	docker build -t prepare-data -f basemap/Dockerfile-prepare basemap
	docker run -it --rm -v $(pwd)/basemap:/work prepare-data

Then build web application image (with a name like registry.nextgis.com/geoservices:2.5.0, for example):

.. code-block::

	docker build -t registry.nextgis.com/geoservices:2.5.0 .

.. _docs_geoserv_prem_admin_setup:

Setting up
----------

After all images are successfully built and data is prepared, modify docker-compose.yml:

* Change image names to those set during building (tag 'image') 
* Change environment variable SESSION_KEY to a random text value (optional, if it is empty or not set, it generates automatically)
* Change environment variables DB_PASSWORD and POSTGRES_PASSWORD to new password (value must be the same in all occurrences)
* Change environment variable ADMIN_PASSWORD to new password
* Change environment variables S3_ACCESS_KEY/MINIO_ACCESS_KEY and S3_SECRET_KEY/MINIO_SECRET_KEY to new passwords (values must be different for \*_ACCESS_KEY and \*_SECRET_KEY)
* In the 'redis' launch command set the memory capacity (within limits available for the container, best set it 1-2 Gb lower than limit). Example:

**nano docker-compose.yml**

.. code-block::

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
	



If you need PKK data for integration with external geo services, then to the environment variables of the container 'app' add variable PKK_EXTERNAL_APIKEY with the API key of your profile on https://geoservices.nextgis.com.

For integration with NextGIS Web  to the environment variables of the container 'app' add the following variables: NGW_URL, NGW_LOGIN, NGW_APIKEY.

* NGW_URL - address of NextGIS Web server in 'scheme-host-port' format
* NGW_LOGIN and NGW_APIKEY - username and password for NextGIS Web This user must have permission to read data that has to be cached in GeoServices. 

.. _docs_geoserv_prem_admin_launch:

Launch
---------

To launch and check functionality of the stack, run the following code:

.. code-block::

	docker-compose up

To launch in service mode:

.. code-block::

	docker-compose up -d

After you launched it in browser open service address with port set to 8088. For example,

.. code-block::

	http://localhost:8088

.. _docs_geoserv_prem_admin_var:

Complete list of environment variables for NextGIS GeoServices
-------------------------------------------------------------------

For each variable the table provides the following info: required or not, default value, short description.

.. list-table::
   :header-rows: 1

   * - **Variable**
     - **Required**
     - **Default value**
     - **Description**
   * - DEBUG
     - no
     - true
     - Enable SQL debugging
   * - ADMIN_PASSWORD
     - yes
     - admin
     - Pre-set administrator password
   * - SESSION_KEY
     - no
     - secret
     - Session key - random text
   * - GIN_MODE
     - no
     - release
     - Controls debugging of the gin library and web application diagnostic messages
   * - INCLUDE_ORIGIN_SUFFIXES
     - no
     - "nextgis.com", "nextgis.ru"
     - Origin array that is added to those specified in the API key
   * - TOKEN_CACHE_SIZE
     - no
     - 1024
     - Max number of authorization tokens in cache
   * - TIMEOUT
     - no
     - 180
     - Network request timeout
   * - FILE_TIMEOUT
     - no
     - 1800
     - Timeout for file downloads
   * - SESSION_MAX_AGE
     - no
     - 259200
     - How long a web application session lasts
   * - HTTP_SKIP_SSL_VERIFY
     - no
     - false
     - Do not check https certificates
   * - LDAP_LOGIN
     - no
     - false
     - | Authentication via LDAP
       | Keep default
   * - LDAP_TLS
     - no
     - no
     - Use TLS
   * - LDAP_URL
     - no
     - “”
     - LDAP server address
   * - LDAP_USER_FILTER
     - no
     - (objectClass=posixAccount)
     - User search filter
   * - LDAP_USER_ATTR
     - no
     - uid
     - User attribute
   * - LDAP_GROUP_FILTER
     - no
     - cn=geoservices
     - Group search filter
   * - LDAP_GROUP_ATTR
     - no
     - memberUid
     - Group attribute
   * - LDAP_DEFAULT_GROUP_ID
     - no
     - 0
     - Default group for LDAP users - 0 group assignment disabled
   * - LDAP_UPDATE_GROUPS
     - no
     - false
     - Update inclusion to groups for users
   * - OAUTH2_LOGIN
     - no
     - false
     - Enable authentication via OAuth2
   * - OAUTH2_CLIENT_ID
     - no
     - 
     - OAuth2 client ID
   * - OAUTH2_CLIENT_SECRET
     - no
     - 
     - OAuth2 client secret
   * - OAUTH2_REDIRECT_URI
     - no
     - 
     - OAuth2 redirect URI
   * - OAUTH2_ENDPOINT
     - no
     - https://my.nextgis.com
     - Endpoint
   * - OAUTH2_SCOPE
     - no
     - user_info.read
     - Scope
   * - OAUTH2_TYPE
     - no
     - 1
     - Authorization type: 1 -NextGIS ID, 2 - Keycloak, 3 - custom, 4 - Blitz
   * - OAUTH2_TOKEN_ENDPOINT
     - no
     - https://my.nextgis.com/oauth2/token
     - Token endpoint
   * - OAUTH2_AUTH_ENDPOINT
     - no
     - https://my.nextgis.com/oauth2/authorize
     - Authorization endpoint
   * - OAUTH2_USERINFO_ENDPOINT
     - no
     - https://my.nextgis.com/api/v1/user_info
     - Endpoint for user info (not needed for JWT)
   * - OAUTH2_INTROSPECTION_ENDPOINT
     - no
     - https://my.nextgis.com/oauth2/introspect
     - Introspection endpoint
   * - OAUTH2_PROFILE_SUBJ_ATTR
     - no
     - nextgis_guid
     - Field for getting user ID (subject)
   * - OAUTH2_PROFILE_KEYNAME_ATTR
     - no
     - username
     - Field for getting username
   * - OAUTH2_PROFILE_FIRSTNAME_ATTR
     - no
     - first_name
     - Field for user's first name
   * - OAUTH2_PROFILE_LASTNAME_ATTR
     - no
     - last_name
     - Field for user's last name
   * - OAUTH2_USER_AUTOCREATE
     - no
     - true
     - Creates user on first enter
   * - OAUTH2_VALIDATE_KEY
     - no
     - “”
     - Key to verify JWT signature
   * - OAUTH2_CREATE_GROUPS
     - no
     - false
     - Create groups based on user roles
   * - OAUTH2_UPDATE_GROUPS
     - no
     - false
     - Update user inclusion into groups based on user roles
   * - OAUTH2_TOKEN_CACHE_TTL
     - no
     - 3600
     - Default token lifetime unless another is not returned by server
   * - OAUTH2_LOGOUT_ENDPOINT
     - no
     - “”
     - Logout endpoint
   * - OAUTH2_GROUPS_JWT_KEY
     - no
     - resource_access/{client_id}/roles
     - Path for role/group search in JWT token
   * - LOCAL_LOGIN
     - no
     - true
     - Allow local user accounts
   * - DEFAULT_LANGUAGE
     - no
     - en
     - Default language
   * - LOG
     - no
     - false
     - stdout messages in structured format
   * - LOG_ONLY_EDITS
     - no
     - false
     - stdout only contains message on data modifications
   * - CLOUD_MODE
     - no
     - false
     - Cloud launch mode
   * - MAX_AGE
     - no
     - 43200
     - Time the tiles are stored in user's browser - 12 hrs
   * - EXT_TMS_SUPPORT
     - no
     - false
     - Enable external TMS service support
   * - 
     - no
     - https://geoservices.nextgis.com
     - URL for integration with public cadaster map (PKK)
   * - PKK_EXTERNAL_APIKEY
     - no
     - “”
     - APIKey for integration with PKK
   * - PKK_TILES_URL
     - no
     - “”
     - URL of the local serveer for PKK integration
   * - PKK_FEATURES_URL
     - no
     - “”
     - URL of the local serveer for PKK integration
   * - PKK_MIN_ZOOM
     - no
     - 3
     - Min level of PKK tile zoom
   * - PKK_MAX_ZOOM
     - no
     - 18
     - Max level of PKK tile zoom
   * - PKK_REGION
     - no
     - | MULTIPOLYGON (((-168.4 84,-168.4 50,-179.999999 50,-179.9999999 84,-168.4 84)),
       | ((130 40,130 84,179.999999 84,179.999999 40,130 40)),
       | ((129.999999 84,129.999999 47,82.5 47,82.5 84,129.999999 84)),
       | ((82.4999999 50,50 50,50 84,82.4999999 84,82.4999999 50)),
       | ((20 84,49.999999 84,49.999999 40,20 40,20 84)))
     - Are for PKK tiles query
   * - DB_TYPE
     - yes
     - sqlite3
     - DB type - sqlite3, postgres, mysql
   * - DB_USER
     - no
     - geoservices
     - User account used to access DB
   * - DB_PASSWORD
     - yes
     - 
     - DB password
   * - DB_HOST
     - yes
     - localhost
     - DB address
   * - DB_PORT
     - yes
     - 5432
     - DB port
   * - DB_NAME
     - no
     - geoservices
     - DB name
   * - DB_MAXCONN
     - no
     - 50
     - Max number of connections
   * - DB_MAXIDLECONN
     - no
     - 10
     - Max number of idle connections
   * - DB_SSL_MODE
     - no
     - 
     - | disable - I don't care about security, and I don't want to pay the overhead of encryption.
       | allow - I don't care about security, but I will pay the overhead of encryption if the server insists on it.
       | prefer - I don't care about encryption, but I wish to pay the overhead of encryption if the server supports it.
       | require - I want my data to be encrypted, and I accept the overhead. I trust that the network will make sure I always connect to the server I want.
       | verify-ca - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server that I trust.
       | verify-full - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server I trust, and that it's the one I specify.
   * - DB_SSL_CERT
     - no
     - 
     - Path to certificate file
   * - DB_SSL_KEY
     - no
     - 
     - Path to key file
   * - DB_SSL_ROOT_CERT
     - no
     - 
     - Path to root certificate
   * - REDIS_ENDPOINT
     - yes
     - localhost:6379
     - Redis service address
   * - REDIS_MAX_IDLE
     - no
     - 100
     - Max time before pool connection is closed
   * - REDIS_MAX_ACTIVE
     - no
     - 1000
     - Max number of active connections in the pool
   * - REDIS_IDLE_TIMEOUT
     - no
     - 60
     - time before pool connection is closed
   * - REDIS_CLUSTER
     - no
     - false
     - Connect to Redis cluster
   * - REDIS_NODES
     - no
     - "localhost:6379 localhost:7001 localhost:7002 localhost:7003 localhost:7004 localhost:7004"
     - Redis cluster node (only used if REDIS_CLUSTER == true)
   * - REDIS_KEY_PREFIX
     - no
     - “”
     - Prefix for Redis keys generated by the app
   * - REDIS_USER
     - no
     - geoservices
     - Redis user login
   * - REDIS_DATABASE
     - no
     - 0
     - Redis data base
   * - REDIS_SSL
     - no
     - false
     - Connection using SSL/TLS
   * - REDIS_INSECURE_SSL
     - no
     - false
     - Do not validate SSL/TLS
   * - S3_ACCESS_KEY
     - yes
     - Q3AM3UQ867SPQQA43P2F
     - Access key for S3
   * - S3_SECRET_KEY
     - yes
     - zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG
     - Secret access key for S3
   * - S3_ENDPOINT
     - yes
     - play.min.io
     - S3 server address
   * - S3_SSL
     - no
     - true
     - Use encryption
   * - S3_INSECURE_SSL
     - no
     - false
     - Do not check SSL certificates
   * - S3_DEFAULT_STORAGE_CLASS
     - no
     - REDUCED_REDUNDANCY
     - Storage method: REDUCED_REDUNDANCY or STANDARD
   * - S3_BUCKET_NAME
     - no
     - geoservices
     - Bucket name
   * - S3_KEY_PREFIX
     - no
     - “”
     - Prefix for S3 keys generated by the app
   * - S3_NO_OBJECT_TAGGING
     - no
     - false
     - Do not dedupe or apply expiration time if S3 does not support tags
   * - RASTER_MAX_ZOOM
     - no
     - 20
     - Max zoom for raster tiles
   * - VECTOR_MAX_ZOOM
     - no
     - 14
     - Max zoom for vector tiles
   * - EXPIRE_TILES_MIN_ZOOM
     - no
     - 7
     - Min zoom for tile expiration control
   * - EXPIRE_TILES_MAX_ZOOM
     - no
     - 16
     - Max zoom for tile expiration control
   * - NET_MAX_RETRY_COUNT
     - no
     - 5
     - Number of attempts for iterative queries
   * - LONG_REQUEST_MIN_TIME
     - no
     - 0
     - Only log long queries - 0 disabled
   * - NGW_URL
     - no
     - https://sandbox.nextgis.com
     - Address of associated NextGIS Web (to create cache from basemaps)
   * - NGW_LOGIN
     - no
     - administrator
     - Login for NextGIS Web - needed to render tile while seeding
   * - NGW_APIKEY
     - no
     - admin
     - Password for NextGIS Web - needed to render tile while seeding
   * - NGW_FEATURE_LIMIT
     - no
     - 256
     - Number of entries in page mode
   * - USERS_MAINTANCE_SCHEDULE
     - no
     - @every 9m1s
     - Schedules user cache clearing
   * - SERVICE_MAINTANCE_SCHEDULE
     - no
     - @every 10m4s
     - Schedules service cache clearing
   * - SERVICE_HOUSEKEEPING_SCHEDULE
     - no
     - @every 25h30m10s
     - Schedules system clearing
   * - DATA_STORE
     - no
     - /data
     - | Path to data necessary for service functioning
       | Keep default
   * - FILE_STORE
     - no
     - /work
     - Path to the working directory. This is the folder for downloading files, performing operations, creating temporary files.
   * - BM_DB_HOST
     - no
     - localhost
     - | Host with PostGIS DB. Upon starting web application checks for DB connection and necessary extensions 
       | If connection fails or extensions are not found, basemap section is disabled 
   * - BM_DB_PORT
     - no
     - 5432
     - Port for PostGIS DB
   * - BM_DB_NAME
     - no
     - basemap
     - DB name for OSM dump import
   * - BM_DB_USER
     - no
     - geoservices
     - User account used to access basemap DB
   * - BM_DB_PASSWORD
     - yes
     - 
     - Password for basemap DB access
   * - BM_DB_SSL_MODE
     - no
     - 
     - | disable - I don't care about security, and I don't want to pay the overhead of encryption.
       | allow - I don't care about security, but I will pay the overhead of encryption if the server insists on it.
       | prefer - I don't care about encryption, but I wish to pay the overhead of encryption if the server supports it.
       | require - I want my data to be encrypted, and I accept the overhead. I trust that the network will make sure I always connect to the server I want.
       | verify-ca - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server that I trust.
       | verify-full - I want my data encrypted, and I accept the overhead. I want to be sure that I connect to a server I trust, and that it's the one I specify.
   * - BM_DB_SSL_CERT
     - no
     - 
     - Path to certificate file
   * - BM_DB_SSL_KEY
     - no
     - 
     - Path to key file
   * - BM_DB_SSL_ROOT_CERT
     - no
     - 
     - Path to root certificate
   * - BM_DB_PARALLEL_SQL
     - no
     - true
     - Perform parallel DB queries for vector tiles
   * - BM_DIFF_URL
     - no
     - 
     - Address to download OSM delta files (only if EXT_SOURCES_SUPPORT == true)
   * - BM_EXPIRE_TILES_MIN_ZOOM
     - no
     - 7
     - Min zoom to log invalid tiles
   * - BM_EXPIRE_TILES_MAX_ZOOM
     - no
     - 16
     - Max zoom to log invalid tiles
   * - EXT_SOURCES_SUPPORT
     - no
     - false
     - | Allow/forbid getting files from Internet. For example, to initialize DB by downloading a dump from Internet or getting diff regularly. 
       | Keep default
   * - EXT_RASTER_RESAMPLING
     - no
     - bilinear
     - | Raster interpolation. Supported methods:
       | near: nearest neighbour resampling (default, fastest algorithm, worst interpolation quality).
       | bilinear: bilinear resampling.
       | cubic: cubic resampling.
       | cubicspline: cubic spline resampling.
       | lanczos: Lanczos windowed sinc resampling.
       | average: average resampling, computes the weighted average of all non-NODATA contributing pixels.
       | rms root mean square / quadratic mean of all non-NODATA contributing pixels (GDAL >= 3.3)
       | mode: mode resampling, selects the value which appears most often of all the sampled points. 
       | In the case of ties, the first value identified as the mode will be selected.
       | max: maximum resampling, selects the maximum value from all non-NODATA contributing pixels.
       | min: minimum resampling, selects the minimum value from all non-NODATA contributing pixels.
       | med: median resampling, selects the median value of all non-NODATA contributing pixels.
       | q1: first quartile resampling, selects the first quartile value of all non-NODATA contributing pixels.
       | q3: third quartile resampling, selects the third quartile value of all non-NODATA contributing pixels.
       | sum: compute the weighted sum of all non-NODATA contributing pixels (since GDAL 3.1)
   * - EXT_ZEROBLOCKHTTPCODES
     - no
     - "204,404"
     - Codes of HTTP responses for white tiles
   * - LOCALES
     - no
     - “ru en”
     - List of user interface languages
   * - OUTDATED_STAT_TABLE_ROWS
     - no
     - 2*365*24*time.Hour
     - Delete log entries from before 2 years
   * - ENABLE_SWAGGER
     - no
     - true
     - Enable web interface for swagger
   * - SSL_CERT_FILE
     - no
     - 
     - | To override path to certificate
       | https://stackoverflow.com/a/67622500/2901140
       | 
       | You can also add certificates using following paths (depends on the platform):
       | 
       | "/etc/ssl/certs/ca-certificates.crt", 
       | // Debian/Ubuntu/Gentoo etc. "/etc/pki/tls/certs/ca-bundle.crt", 
       | // Fedora/RHEL 6 "/etc/ssl/ca-bundle.pem", 
       | // OpenSUSE "/etc/pki/tls/cacert.pem", 
       | // OpenELEC "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem", 
       | // CentOS/RHEL 7 "/etc/ssl/cert.pem", 
       | // Alpine Linux
       | 
       | 
       | https://stackoverflow.com/a/40051432/2901140
   * - DEFAULT_KEY_EXPIRE
     - no
     - 7 days
     - TTL for tiles of external services


