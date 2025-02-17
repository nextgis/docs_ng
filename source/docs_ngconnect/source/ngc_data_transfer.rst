
.. _ng_connect_data_transfer:

Обмен данными
==============

Модуль NextGIS Connect позволяет обмениваться геоданными между QGIS и Веб ГИС в обоих направлениях, но со своими особенностями.

.. _ng_connect_types:

Типы ресурсов 
--------------

Для обмена данными и работы доступны следующие типы ресурсов:

.. |resource_vector_point| image:: _static/nextgis_connect/vector_layer_point.png
.. |resource_vector_mpoint| image:: _static/nextgis_connect/vector_layer_mpoint.png
.. |resource_vector_line| image:: _static/nextgis_connect/vector_layer_line.png
.. |resource_vector_mline| image:: _static/nextgis_connect/vector_layer_mline.png
.. |resource_vector_polygon| image:: _static/nextgis_connect/vector_layer_polygon.png
.. |resource_vector_mpolygon| image:: _static/nextgis_connect/vector_layer_mpolygon.png
.. |resource_wfs| image:: _static/nextgis_connect/resource_wfs_symbol.png
.. |resource_wms| image:: _static/nextgis_connect/resource_wms_symbol.png
.. |resource_style| image:: _static/nextgis_connect/resource_style_symbol.png
.. |resource_webmap| image:: _static/nextgis_connect/resource_webmap_symbol.png
.. |resource_group| image:: _static/nextgis_connect/resource_group.png
.. |raster_layer| image:: _static/nextgis_connect/raster_layer.png
.. |vector_layer| image:: _static/nextgis_connect/vector_layer_symbol.png
.. |basemap_symbol| image:: _static/nextgis_connect/basemap_symbol.png
.. |tms_service_symbol| image:: _static/nextgis_connect/tms_service_symbol.png
.. |tms_connection_symbol| image:: _static/nextgis_connect/tms_connection_symbol.png
.. |postgis_layer_symbol| image:: _static/nextgis_connect/postgis_layer_symbol.png
.. |demo_project_symbol| image:: _static/nextgis_connect/demo_project_symbol.png
.. |wms_layer_symbol| image:: _static/nextgis_connect/wms_layer_symbol.png
.. |wms_connection_symbol| image:: _static/nextgis_connect/wms_connection_symbol.png
.. |wfs_layer_symbol| image:: _static/nextgis_connect/wfs_layer_symbol.png

- |vector_layer| - Векторный слой (NGW Vector Layer), он может быть: 
  |resource_vector_point| Точечный; 
  |resource_vector_mpoint| Мультиточечный; 
  |resource_vector_line| Линейный; 
  |resource_vector_line| Мультилинейный; 
  |resource_vector_polygon| Полигональный; 
  |resource_vector_mpolygon| Мультиполигональный; 

- |resource_style| - Стиль векторного слоя.
- |resource_wfs| - WFS Сервис (NGW WFS Service)
- |resource_wms| - WMS Сервис (NGW WMS Service)
- |tms_service_symbol| - Слой TMS
- |postgis_layer_symbol| - Слой PostGIS
- |wfs_layer_symbol| - Слой WFS
- |raster_layer| - Растровый слой (NGW Raster Layer)
- |basemap_symbol| - Подложка
- |resource_webmap| - Веб карта (NGW Web Map)
- |resource_group| - Группа ресурсов




.. _ng_connect_import:

Загрузка данных из QGIS в Веб ГИС
----------------------------------

Модуль NextGIS Connect позволяет загружать в Веб ГИС:

1. Векторные данные
2. Растровые данные
3. Базовые карты (подложки)
4. Группы слоёв
5. Проект QGIS целиком

Также модуль позволяет опубликовать векторные данные по стандартным протоколам :term:`WFS`, :term:`WMS` и OGC API - Features.

Алгоритм загрузки каждого типа данных описан `здесь <https://docs.nextgis.ru/docs_ngconnect/source/resources.html>`_.

.. figure:: _static/nextgis_connect/add_to_ngw_ru.png
   :align: center
   :width: 10cm
   
   Меню загрузки данных в Веб ГИС в панели NG Connect

Также загрузку данных в Веб ГИС можно выбрать как один из способов экспорта слоя, группы слоёв или проекта целиком.

.. figure:: _static/nextgis_connect/context_export_to_ngw_ru.png
   :align: center
   :width: 20cm

   Загрузка данных в Веб ГИС через контекстное меню панели слоёв

- Векторный слой - в Веб ГИС будет создан векторный слой и стиль, аналогичный стилю 
  выбранного слоя в QGIS, который можно добавить на веб-карту в Веб ГИС.
- Растровый слой - в Веб ГИС будет создан растровый слой со стилем по умолчанию, 
  который можно добавить на веб-карту в Веб ГИС.
- Загрузить всё - В Веб ГИС будут добавлены все слои, для которых доступна операция "Импортировать выбранный слой", и все группы в соответствии с иерархией в панели слоёв QGIS. Также будет создана веб-карта, на которую будут добавлены все импортируемые слои с учетом иерархии и видимости в панели слоёв QGIS. Вам необходимо ввести название новой группы, которая будет создана в Веб ГИС для размещения всех ресурсов, импортируемых в рамках данной операции. После импорта проекта созданная веб-карта откроется в браузере автоматически, если в настройках модуля выбрана соответствуюйщая опция.
- Обновить стиль слоя - В Веб ГИС будет обновлен стиль слоя аналогично стилю выбранного слоя в QGIS.
- Добавить новый стиль к слою - В Веб ГИС будет добавлен новый стиль к слою, аналогично стилю выбранного слоя в QGIS.

При загрузке слоя с **несколькими стилями** в NGW, они загружаются со своими именами. Если название стиля - default (или "по умолчанию"), используется название слоя. 


Добавление ресурсов в Веб ГИС производится в выбранную на панели ресурсов Веб ГИС группу.

- Если выбрана не группа, а другой тип ресурса - в ближайшую родительскую группу выбранного ресурса.
- Если не выбран ресурс - в корневую группу.

Также поддерживается выгрузка в Веб ГИС вложений. Посмотрите, как это работает, в видео:

.. raw:: html

   <iframe width="560" height="315" src="https://rutube.ru/play/embed/4a8748602408662ce01012be6ed9ae51/" frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

Посмотреть видео на `youtube <https://youtu.be/K9S8TPLYC9w>`_, `rutube <https://rutube.ru/video/4a8748602408662ce01012be6ed9ae51/>`_.

.. warning::

   Стоит обратить внимание на то, что **фотографии**, которые были собраны в мобильных приложениях NextGIS Collector/Mobile и загружены в Веб ГИС вместе со слоями в виде вложений, **не будут** доступны в настольной NextGIS QGIS после загрузки этих слоев через модуль NextGIS Connect!



.. ng_connect_keep_photo:

Как сохранить вложения
~~~~~~~~~~~~~~~~~~~~~~~

Пользователь может столкнуться с задачей, когда нужно изменить стилевые настройки слоя, **не потеряв при этом фотографии**. 

Порядок действий в данном случае следующий:

1. Добавить стиль слоя через NextGIS Connect из Веб ГИС в QGIS.
2. Внести необходимые изменения в стиль.
3. Обновить стиль слоя через NextGIS Connect.

.. figure:: _static/nextgis_connect/ngconnect_modify_keep_photo_ru.png
   :align: center
   :width: 20cm   
   
   Обновление стиля

.. _ng_connect_export:

Загрузка данных из Веб ГИС в QGIS
---------------------------------

.. figure:: _static/nextgis_connect/add_to_qgis_ru.png
   :align: center
   :alt: Добавить в QGIS
   :width: 10cm
   
   Кнопка экспорта данных в QGIS

Операция доступна, если в дереве ресурсов NextGIS выбран один из следующих видов ресурсов:

- Векторный слой (NGW Vector Layer) |vector_layer| - в QGIS будет создан векторный 
  слой GeoJSON;
- WFS Слой |wfs_layer_symbol| - в QGIS будет создан WFS слой;
- WFS Сервис (NGW WFS Service) |resource_wfs| - в QGIS будет создан WFS слой, источником 
  данных для которого будет выбранный WFS Сервис;
- WMS Слой |wms_layer_symbol| - в QGIS будет добавлен выбранный WMS слой;
- WMS Сервис |resource_wms| - в QGIS будет создан WMS слой, источником данных для которого будет выбранный WMS Сервис;
- WMS Соединение |wms_connection_symbol| - из списка можно будет выбрать WMS слой, который необходимо добавить в QGIS
- TMS Слой |tms_service_symbol|;
- TMS Соединение |tms_connection_symbol|;
- PostGIS Слой |postgis_layer_symbol|;
- QGIS Стиль Векторного слоя |resource_style| - если стиль относится к векторному слою, в QGIS будет создан векторный слой GeoJSON, со стилем идентичным выбранному стилю; если стиль относится к слою WFS, будет создан слой WFS с таким стилем;
- Растровый слой |raster_layer| - в QGIS будет создан растровый слой GeoTIFF;
- Подложка |basemap_symbol|;
- Веб-карта |resource_webmap| - при добавлении в QGIS она будет представлена в виде проекта со слоями, стилями и подложками. Подложки карты будут объединены во взаимоисключающую группу;
- `Демо-проект <https://docs.nextgis.ru/docs_ngcom/source/demoprojects.html>`_ |demo_project_symbol| - в QGIS будет создан проект, содержащий слои, стили и подложки;
- Группа ресурсов |resource_group| - в текущий проект QGIS будет добавлена новая группа и входящие в неё ресурсы.


Особенности загрузки слоев с **несколькими стилями**:

* При выборе в дереве Connect слоя с несколькими стилями, они подгрузятся все, но будет предложено выбрать текущий.
* При выборе в дереве Connect стиля слоя, добавятся все стили, по умолчанию будет выбранный.
* При добавлении группы ресурсов, которая содержит слои с несколькими стилями, будут добавлены все стили и выбран либо одноименный слою, либо первый по алфавиту. Диалог с выбором показан не будет.
* При добавлении WFS/OGCF стиль будет выбран либо одноименный слою, либо первый по алфавиту.

Процесс добавления слоя с несколькими стилями в видео:

.. raw:: html

   <iframe width="560" height="315" src="https://rutube.ru/play/embed/d65766eacd8a3f162fff6ce09556045b/" frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

Смотреть на `youtube <https://youtu.be/snq2yv8iNEk>`_, `rutube <https://rutube.ru/video/d65766eacd8a3f162fff6ce09556045b/>`_.

Алгоритм загрузки разных типов данных в QGIS подробно описан `здесь <https://docs.nextgis.ru/docs_ngconnect/source/resources.html#connect-data-export>`_.

Векторные слои из вашей Веб ГИС можно `редактировать <https://docs.nextgis.ru/docs_ngconnect/source/edit.html#>`_ сразу после добавления их в QGIS.

.. _ng_connect_cont_menu:

Контекстное меню
----------------
Контекстное меню может отличаться у различных ресурсов. 

.. figure:: _static/nextgis_connect/context_menu_ru.png
   :align: center
   :alt: Контекстное меню qgis стиля векторного слоя
   :width: 10cm
   
   Пример контекстного меню

Общедоступные операции для всех типов ресурсов:

- Открыть в ВебГИС - открывает страницу выбранного ресурса в Веб ГИС, см. :numref:`ngc_open_from_layertree_pic`;

- Переименовать ресурс;

- `Удалить ресурс <https://docs.nextgis.ru/docs_ngconnect/source/ngc_data_transfer.html#connect-resource-delete>`_;

- Редактировать метаданные.


Опциональные - зависят от типа ресурса:

- Добавить в QGIS - операция и список ресурсов, для которых она доступна, описаны `выше <https://docs.nextgis.ru/docs_ngconnect/source/ngc_data_transfer.html#ng-connect-export>`_;

- `Создать Веб Карту <https://docs.nextgis.ru/docs_ngconnect/source/resources.html#web-map>`_ - доступен для ресурсов: Векторный слой, Стиль Векторного слоя, Растровый слой, слой WMS;

- `Загрузить как QML <https://docs.nextgis.ru/docs_ngconnect/source/export.html#connect-save-style>`_ - доступен только для ресурса QGIS Стиль Векторного слоя;

- `Копировать стиль <https://docs.nextgis.ru/docs_ngconnect/source/edit.html#connect-style-copy>`_  - доступен только для ресурса QGIS Стиль Векторного слоя;

- `Создать сервис WFS <https://docs.nextgis.ru/docs_ngconnect/source/resources.html#wfs>`_ - доступен только для ресурса Векторный слой;

- `Создать сервис OGC API - Features <https://docs.nextgis.ru/docs_ngconnect/source/resources.html#ogc-api-features>`_ - доступен только для ресурса Векторный слой;

- `Создать сервис WMS <https://docs.nextgis.ru/docs_ngconnect/source/resources.html#wms>`_ - доступен только для ресурса Векторный слой;

- `Дублировать ресурс <https://docs.nextgis.ru/docs_ngconnect/source/ngc_data_transfer.html#connect-resource-double>`_ - доступен только для ресурсов: Векторный слой и Растровый слой;

- `Перезаписать выбранный слой <https://docs.nextgis.ru/docs_ngconnect/source/edit.html#connect-data-overwrite>`_ - доступен только для ресурса Векторный слой.


Кроме того, при установке модуля появляется возможность переходить к данным в Веб ГИС из панели слоев в QGIS: в контекстном меню слоя в QGIS найдите «NextGIS Connect», и нажмите «Открыть в Веб ГИС».


.. figure:: _static/nextgis_connect/ngc_open_from_layertree_ru.png
   :align: center
   :alt: Контекстное меню в дереве слоев
   :name: ngc_open_from_layertree_pic
   :width: 22cm

   Открытие данных в Веб ГИС из дерева слоев QGIS



.. _connect_resource_double:

Дублирование ресурсов
-----------------------

При помощи модуля можно создать копию слоя в Веб ГИС. Доступно для ресурсов Векторный слой и Растровый слой. 

* Чтобы скопировать слой, выберите его в окне модуля Connect и в контекстном меню нажмите **Дублировать ресурс**.
* Во всплывающем окне подтвердите дублирование.

Копия слоя будет создана в той же папке, стиль слоя также будет скопирован.

.. figure:: _static/NGConnect_double_ru.png
   :name: NGConnect_double_pic
   :align: center
   :width: 8cm

   Дублирование ресурса

.. _connect_resource_delete:

Удаление ресурсов
-------------------

Модуль NextGIS Connect позволяет быстро создавать / удалять любые ресурсы из Веб ГИС. Для этого:

* Выберите в дереве ресурсов Веб ГИС в окне модуля NextGIS Connect ресурс, который вы хотите удалить;
* Выберите пункт **Удалить** в контекстном меню;
* Если ресурс удалился успешно, то он исчезнет из дерева ресурсов Веб ГИС.
 



.. _ng_connect_res_group:

Создать группу ресурсов
-------------------------

Эта операция доступна в верхнем меню модуля NextGIS Connect.

Новая группа будет создана в группе ресурсов:

- которая выбрана в дереве ресурсов Веб ГИС;
- которая является ближайшей родительской группой для выбранного ресурса, если он 
  не является группой ресурсов;
- в основной группе ресурсов, если не выбран ни один ресурс в дереве ресурсов Веб ГИС.

.. figure:: _static/nextgis_connect/create_group_ru.png
   :align: center
   :alt: Создать новую группу ресурсов
   :width: 10cm

   Создание группы ресурсов

.. _connect_refresh:

Обновить
----------

Эта операция доступна в верхнем меню модуля NextGIS Connect.

Операция обновит все дерево ресурсов Веб ГИС до актуального на текущий момент состояния.

.. figure:: _static/nextgis_connect/reload_ru.png
   :align: center
   :alt: Обновить дерево ресурсов
   :width: 10cm

   Актуализация данных Веб ГИС

.. _connect_open_webmap:

Открыть веб-карту в браузере
-----------------------------

Эта операция доступна в верхнем меню модуля NextGIS Connect.

Если в дереве ресурсов выбран ресурс веб-карта (NGW Web Map) |resource_webmap|, 
то она откроется в новой вкладке браузера.

.. figure:: _static/nextgis_connect/open_webmap_ru.png
   :align: center
   :alt: Открыть веб-карту в браузере
   :width: 10cm

   Открытие веб-карты

Также это можно сделать через `контекстное меню <https://docs.nextgis.ru/docs_ngconnect/source/ngc_data_transfer.html#ng-connect-cont-menu>`_.
