.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.ru>

.. _docs_geoserv_prem_services:


Сервисы
=======

.. _gs_prem_service_groups:

Группы сервисов
---------------

Сервисы в приложение могут быть добавлены только в определенные группы сервисов. Группы задаются в настройках на вкладке **Группы сервисов**.

.. figure:: _static/geosop_service_group_ru.png
   :name: geosop_gr_serv1
   :align: center
   :width: 20cm

   Одна из групп сервисов


Удалить или изменить группу сервисов можно с помощью соответствующей кнопки в интерфейсе, выбрав нужные сервисы.

.. figure:: _static/geosop_serv_group_edit_ru.png
   :name: geosop_gr_serv2
   :align: center
   :width: 20cm

   Настройки групп сервисов


Для создания новой группы следует указать её название.

.. figure:: _static/geosop_gr_serv3.png
   :name: geosop_gr_serv3
   :align: center
   :width: 20cm

   Создание новой группы сервисов

.. _gs_prem_ngw_webmaps:

Веб-карты NGW
-------------

`NextGIS Web <https://nextgis.ru/nextgis-web/>`_ - это серверная геоинформационная система, предназначенная для сбора, хранения, визуализации и обработки пространственных данных.

Сервис NGW Web Maps позволяет создавать кэшированные тайловые сервисы на основе веб-карт, созданных в NextGIS Web.

Администратор указывает URL развернутого NextGIS Web, ресурс веб-карты, название сервиса и диапазон масштабных уровней для кэширования.
После этого сервис появится в списке созданных. При необходимости сервис можно отредактировать или удалить.

Обращение к созданному сервису не затрагивает NextGIS Web, таким образом можно создать сервис для высоких пиковых нагрузок и снизить нагрузку на сам NextGIS Web.

.. figure:: _static/geosop_ngw_create_button_ru.png
   :name: geosop_ngw1
   :align: center
   :width: 20cm

   Кнопка добавления нового сервиса

.. figure:: _static/geosop_ngw_new_param_ru.png
   :name: geosop_ngw2
   :align: center
   :width: 16cm

   Параметры создаваемого сервиса

.. figure:: _static/geosop_ngw_result_ru.png
   :name: geosop_ngw3
   :align: center
   :width: 20cm

   Созданный сервис в группе

.. _gs_prem_tms:

Внешний TMS
------------

Геосервисы позволяют добавлять внешние TMS для их дальнейшего кэширования и использования.

.. figure:: _static/geosop_ngw_create_button_ru.png
   :name: geosop_tms1
   :align: center
   :width: 20cm

В форме заполняются URL добавляемого TMS сервиса, система координат, название и диапазон уровней отображения.
После чего сервис появится в списке соответствующей группы. При необходимости сервис можно отредактировать или удалить.

.. figure:: _static/geosop_tms_new_param_ru.png
   :name: geosop_tms2
   :align: center
   :width: 16cm

   Параметры создаваемого сервиса

.. figure:: _static/geosop_tms_result_ru.png
   :name: geosop_tms3
   :align: center
   :width: 20cm

   Созданный сервис в группе
