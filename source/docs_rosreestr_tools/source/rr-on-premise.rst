.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.ru>

.. _ngq_rosreestr_on-premise:


Работа с модулем Rosreestr Tools на своем сервере
=================================================

Некоторые функции NGQ Rosreestr Tools требуют наличия активного соединения с серверами NextGIS и без него не работают. 
Для организации подобного взаимодействия необходимо связать глобальные сервисы NextGIS и NextGIS ID на своем сервере. 

Технически, необходимо:

1. Создать глобальный аккаунт `my.nextgis.com <https://my.nextgis.ru>`_ если его еще нет.
2. Сообщить через `систему поддержки <https://nextgis.ru/terms-support>`_ о создании аккаунта, запросить перевод на Premium.
3. Дождаться уведомления о переводе на Premium.
4. В NextGIS QGIS в разделе *Настройки > Параметры > NextGIS* поменять Endpoint на ваш сервер авторизации `NextGIS ID on-premise <https://docs.nextgis.ru/docs_ngid/source/ngidop.html>`_
5. Скопировать `ключ доступа <https://docs.nextgis.ru/docs_ngid/source/ngidop.html#nextgis-id-on-premise>`_ из NGID (система управления пользователями, размещающаяся на вашем сервере) и добавить его в `настройки <https://my.nextgis.com/myngidonpremises>`_ NextGIS ID on-premise.

После этого запросы из NGQ Rosreestr Tools с рабочих мест внутри корпоративной сети к глобальным сервисам NextGIS должны заработать.

.. warning::
   Необходимо разрешить в локальной сети организации доступ ко внешнему серверу по адресу https://geoservices.nextgis.com
   
   
   
Подключение кадастровых сервисов для NextGIS Web on-premise для работы на веб-карте
----------------------------------------------------------------------------------

Чтобы подключить функциональность кадастровых сервисов для работы на веб-картах в NextGIS Web расположенном на своем сервере, воспользуйтесь `этой <https://docs.nextgis.ru/docs_ngweb/source/admin_tasks.html#nextgis-web-on-premise>`_ инструкцией.

1. Создать глобальный аккаунт my.nextgis.com (если его еще нет);
2. Сообщить письмом на support@nextgis.com о создании аккаунта, указать на какой email он зарегистрирован, запросить его перевод на Premium;
3. Дождаться уведомления о переводе на Premium;
4. Авторизоваться на geoservices.nextgis.com (облачный аккаунт NextGIS ID, пункт 1);
5. Перейти на вкладку `Rosreestr <https://geoservices.nextgis.com/pkk>`_ и скопировать `API ключ <https://docs.nextgis.ru/docs_geoservices/source/rosreestr_pkk.html#nggeos-pkk>`_;
6. Вставить ключ в настройки на стороне NGW в `Панели управления <https://docs.nextgis.ru/docs_ngweb/source/admin_tasks.html#ngw-cadastre-services>`_ .

.. warning::
   Для работы этой функциональности NGW должен иметь доступ ко внешнему серверу по адресу https://geoservices.nextgis.com
