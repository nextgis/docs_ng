Инструкция администратора для NextGIS Toolbox on-premise
=========================================================

.. _tbop_connection:

Выбор адресов подключения
----------------------------

Toolbox On-Premise использует две точки подключения по HTTP (или HTTPS):

* Веб-интерфейс Toolbox и API - основной адрес по которому пользователи взаимодействуют с продуктом. Значение по умолчанию -  http://server.example.com:58347, где server.example.com DNS-имя сервера, на котором развернут продукт. В крайнем случае можно вместо server.example.com можно использовать IP-адрес сервера.
* Интерфейс Buildbot - вспомогательный адрес, не используется в ходе нормальной работы, но доступ к нему может потребоваться при решении вопросов со службой поддержки. Значение по умолчанию http://hostname.example.com:61978.

Если ваша ИТ-инфраструктура позволяет, рекомендуется настроить обратный прокси-сервер (reverse proxy) для обеспечения TLS-шифрования и работы через HTTPS. Это особенно важно, если доступ к продукту будет осуществляться не только из локальной сети, но и через Интернет. В этом случае адреса точек подключения зависят от настроек обратного прокси-сервера, рекомендуемые значения:

* Веб-интерфейс Toolbox и API - https://toolbox.example.com
* Интерфейс Buildbot - https://avral.example.com

Совместно с вашим ИТ-департаментом выберите адреса, которые вы хотите использовать, и запишите их, они потребуются в дальнейшем. Настройка обратного прокси-сервера должна выполняется силами ИТ-департамента клиента и не относится к области ответственности компании NextGIS. Необходимые параметры приведены в этом документе ниже на примере Nginx.

::

   TOOLBOX_URL
   BUILDBOT_URL

.. _tb_ngid:

Авторизация NextGIS ID
-----------------------

Toolbox On-Premise использует NextGIS ID On-Premise в качестве сервера авторизации, который поставляется как часть NextGIS Web On-Premise. Первым делом выясните адрес подключения к NextGIS ID On-Premise и проверьте, что вы можете авторизоваться в нем под учетной записью administrator. Адрес подключения может выглядеть как https://ngid.example.com или http://server.example.com:8081. Запишите адрес подключения, он понадобится в дальнейшем::

   NEXTGISID_URL

В файл docker-compose.yaml в секцию x-shared нужно добавить переменную TOOLBOX_URL, чтобы получилось следующее::

   x-shared: &shared
     NEXTGISID_URL: "https://ngid.example.com"
     NEXTGISWEB_URL: "https://ngw.example.com"
     TOOLBOX_URL: "https://toolbox.example.com"
     NEXTGISID_INSTANCE_NGID: "a73ed33d-7e04-4405-a1fc-90188093268e"
     NEXTGISID_ADMINISTRATOR_NGID: "cc533d32-6123-4d5f-8ffe-80e0135a54b6"

Для этого на сервере, где установлен NextGIS ID On-Premise (NextGIS Web On-Premise), перейдите в директорию /srv/ngwdocker и отредактируйте файл docker-compose.yaml, например, текстовым редактором и перезапустите стек. Также запишите значение переменной NEXTGISID_ADMINISTRATOR_NGID из секции x-shared.

::

   $ cd /srv/ngwdocker
   $ nano docker-compose.yaml
   $ docker compose up -d

::

   NEXTGISID_ADMINISTRATOR_NGID

.. _tbop_docker_setup:

Установка и настройка Docker
------------------------------

Если на сервере еще не установлен Docker Engine и Docker Compose их нужно установить или обновить до актуальных версий:

* `Docker Engine <https://docs.docker.com/engine/install/>`_
* `Docker Compose <https://docs.docker.com/compose/install/linux/>`_

Для получения образов необходимо выполнить авторизацию в NextGIS Container Registry c использованием имени пользователя (example) и пароля (sesame), предоставленного компанией NextGIS::

   $ docker login cr.nextgis.com -u example -p sesame
   Login Succeeded

В случае если развертывание осуществляется на сервере без доступа к Интернет, то вместо этого шага свяжитесь со службой поддержки для получения архива образов в виде одного файла. Его нужно будет перенести на сервер и загрузить образы командой docker load.

Toolbox On-Premise потребуется Docker Swarm, его нужно инициализировать после установки выполнив команду::

   $ docker swarm init


.. _tbop_setup:

Установка NextGIS Toolbox
---------------------------

На сервере, где планируется развернуть Toolbox On-Premise, создайте директорию /srv/toolbox и перейдите в нее, скачайте шаблон конфигурации (docker-compose-24.10.0.tar.bz2, где 20.10.0 - текущая версия) и распакуйте его. Если установка производится на сервере без доступа в Интернет, скачайте файл на другом ПК и перенесите его на сервер.

::

  $ mkdir /srv/toolbox
  $ cd /srv/toolbox
  $ wget https://nextgis.com/onpremise/toolbox/docker-compose-24.10.0.tar.bz2
  $ tar jxf docker-compose-24.10.0.tar.bz2

Сгенерируйте пароль для Buildbot и запишите его, он может потребоваться в дальнейшем:

::

  $ tr -dc A-Za-z0-9 < /dev/urandom | head -c 12; echo
  ezn81wfERYOW

::

  TOOLBOX_BUILDBOT_SECRET


Отредактируйте файл .env в текстовом редакторе, заполнив значения переменных, которые вы записали выше. В переменной BUILDBOT_REGISTRY_AUTH нужно указать имя пользователя и пароль для подключения NextGIS Container Registry разделив их двоеточием. В итоге должно получится приблизительно следующее::

  IMAGE_VERSION=24.10.0
  IMAGE_BASE=cr.nextgis.com/toolbox
  COMPOSE_BIND=0.0.0.0
  TOOLBOX_URL=https://toolbox.example.com
  BUILDBOT_URL=https://avral.example.com
  NEXTGISID_URL=https://ngid.example.com
  NEXTGISID_ADMINISTRATOR_NGID=7f16c028-df44-457b-be6d-cd9075fad034
  TOOLBOX_BUILDBOT_SECRET=ezn81wfERYOW
  BUILDBOT_REGISTRY_AUTH=example:sesame

После этого можно запускать стек Docker Compose, вначале рекомендуется запустить сервис postgres, подождать полминуты и затем уже запустить остальное::

  $ docker compose up -d postgres && sleep 30
  [+] Running 1/1
   ✔ postgres Pulled                                    1.0s
  [+] Running 3/3
   ✔ Network toolbox_default         Created            0.1s
   ✔ Volume "toolbox_data_postgres"  Created            0.0s
   ✔ Container toolbox-postgres-1    Started            0.3s
  $ docker compose up -d
  [+] Running 3/3
   ✔ background Pulled                                  1.6s
   ✔ app Pulled 1.6s
   ✔ docker Pulled                                      1.6s
   ✔ buildbot Pulled                                    1.6s
  [+] Running 5/5
   ✔ Volume "toolbox_data_storage"   Created            0.0s
   ✔ Container toolbox-postgres-1    Running            0.0s
   ✔ Container toolbox-background-1  Started            0.3s
   ✔ Container toolbox-app-1         Started            0.3s
   ✔ Container toolbox-docker-1      Started            0.3s
   ✔ Container toolbox-buildbot-1    Started            0.3s

На этом установка завершена, если используется HTTPS, то на этом этапе выполните настройку обратного прокси-сервера. Если нет, то сразу приступайте к проверке работоспособности.


.. _tbop_proxy:

Рекомендации по настройке обратного прокси-сервера
---------------------------------------------------

Для обеспечения HTTPS шифрования мы рекомендуем использовать обратный прокси-сервер на базе Nginx, для справки приведем пример фрагмента конфигурационного файла для toolbox.example.com::

  server {
      server_name toolbox.example.com;
      # Директивы сервера: listen, ssl_* и пр.
  
      location / {
          client_max_body_size 2G;
  
          proxy_http_version 1.1;
          proxy_pass http://127.0.0.1:58347;
          proxy_set_header Host $http_host;
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection $proxy_connection;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Forwarded-For $remote_addr;
      }
  }

Директива client_max_body_size определяет максимальный размер загружаемого файла (в примере 2 GiB), нужна только для веб-интерфейса (для Buildbot не нужна).

.. _tbop_check:

Проверка работоспособности
---------------------------

Откройте в браузере веб-интерфейс Toolbox по адресу, который вы выбрали (TOOLBOX_URL) - должна отобразиться страница со списком инструментов и ссылкой Войти в правом верхнем углу.

Перейдите по ссылке Войти, браузер будет перенаправлен в NextGIS ID On-Premise. Может потребоваться ввести пароль от учетной записи administrator, после чего должно сработать перенаправление обратно в веб-интерфейс Toolbox, где в правом верхнем углу должно быть указано имя текущего пользователя (Administrator).

Выберите инструмент **Привет, Мир!** и попробуйте его запустить. Первый запуск инструмента может занять больше времени, так как Docker-образы инструментов скачиваются из NextGIS Container Registry при первом запуске.

Попробуйте запустить инструмент **Конвертация векторных слоёв** на тестовых данных инструмента. Это позволит протестировать загрузку и скачивание файлов.


