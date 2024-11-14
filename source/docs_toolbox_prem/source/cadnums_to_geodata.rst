Пакетный поиск по кадастровым номерам
=====================================

Инструмент создаёт набор слоёв с границами кадастровых объектов, получая на вход текстовый файл со списком их номеров.
Для работы необходим доступ к `geoservices <https://geoservices.nextgis.com/settings/profile>`_. Авторизация через аккаунт на my.nextgis.com (NextGIS ID)

На входе:

* API-ключ из https://geoservices.nextgis.com/settings/profile (Settings -> Profile).
* Текстовый файл (\*.txt) с номерами объектов. Одна строка - один кадастровый номер. Максимально возможное количество номеров - 100.

На выходе:

* Архив с геоданными кадастровых объектов

Запуск инструмента: https://toolbox.nextgis.com/operation/cadnums_to_geodata

**Попробуйте инструмент в действии, скачав наш пример:**

`Набор исходных данных <https://nextgis.ru/data/toolbox/cadnums_to_geodata/cadnums_to_geodata_inputs_ru.zip>`_ для проверки работы инструмента. Внутри архива пошаговая инструкция.

`Пример результата <https://nextgis.ru/data/toolbox/cadnums_to_geodata/cadnums_to_geodata_outputs_ru.zip>`_ работы инструмента.

