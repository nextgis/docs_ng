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

Далее необходимо собрать образ СУБД с поддержкой  PostGIS (например, с названием registry.nextgis.com/postgis:3.3.2):

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
* Change environment variables S3_ACCESS_KEY/MINIO_ACCESS_KEY and S3_SECRET_KEY/MINIO_SECRET_KEY to new passwords (values must be different for *_ACCESS_KEY and *_SECRET_KEY)
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
