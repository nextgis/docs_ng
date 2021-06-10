.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.com>

.. _nggeos_pkk:

Сервисы Публичной кадастровой карты Росреестра
=============================================

`NextGIS Geoservices <https://my.nextgis.com>`_ позволяет получить растровые данные сервиса ПКК и подключить их как внешние источники (:numref:`nggeos_basemap_rosreestr_pkk`).

Доступные слои кадастрового деления:

1. Единицы кадастрового деления (ngrr1)
2. Земельные участки (ngrr2)
3. Зоны с особыми условиями использования территории (ngrr3)


.. figure:: _static/nggeos_basemap_rosreestr_pkk_rus.png
   :name: nggeos_basemap_rosreestr_pkk
   :align: center
   :width: 30cm
 
   Сервисы Публичной кадастровой карты

.. note:: 
	Для подключения данных необходимо получить персональный `API ключ <https://docs.nextgis.ru/docs_geoservices/source/reissue_api_key.html>`_ (apikey в строке запроса, размыто на изображении).
   
`Пример <https://demo.nextgis.com/resource/3928>`_ подключения кадастровых данных
как `слои TMS <https://docs.nextgis.ru/docs_ngweb/source/layers.html#tms>`_ в NextGIS Web.

Также данные можно отфильтровать по координатам и идентификатору, выполнив соответствующие запросы.
