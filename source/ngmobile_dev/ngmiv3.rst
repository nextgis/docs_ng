.. sectionauthor:: Дмитрий Барышников <dmitry.baryshnikov@nextgis.ru>
.. NextGIS Mobile iOS SDK

NextGIS iOS SDK
================

Введение
----------

NextGIS iOS SDK это набор библиотек для работы с геоданным в мобильном приложении для iPhone и iPad. В состав библиотек входят:

* Библиотека `nextgis_datastore <https://github.com/nextgis/nextgis_datastore>`_
* Библиотека `ios_maplib <https://github.com/nextgis/ios_maplib>`_

Библиотека **nextgis_datastore** написана на ``С++11`` и основана на `GDAL <http://gdal.org/>`_. Она обеспечивает следующие возможности:

* создание, изменение и удаление геоданных (растровых и векторных)
* редактирование геоданных (модификация географии и атрибутики)
* управление геоданными (копирование, перенос, изменение формата и др.)
* визуализацию геоданных в виде карт при помощи `OpenGL/OpenGL ES`
* вспомогательные функции (работа с сетью, oAuth2, json)
* интеграция с ``nextgis.com``/``NextGIS Web`` (under development now)

Для взаимодействия с библиотекой используется ``С API`` и биндинги для других языков программирования при помощи ``swig``. 

Библиотека **ios_maplib** написана на ``Swift`` и представляет собой удобную обвязку вокруг C API nextgis_datastore.

Установка
----------

Для использования SDK необходимо :program:`Xcode 8` или выше. Также необходимо установить ``Carthage`` - легковесный менеджер зависимостей для ``Swift`` и ``Objective-C``. Для установки Carthage следуйте инструкциям на `следующей странице <https://github.com/Carthage/Carthage/>`_. 

В папке вашего проекта необходимо создать ``Cartfile`` со следующим содержанием:

.. code-block:: bash

   github "nextgis/ios_maplib"

Далее в терминале следует выполнить команду:

.. code-block:: bash

   carthage update --platform "iOS"

В результате будут скачаны и установлены все необходимые компоненты.

Подключение к проекту
----------------------

Если планируется показывать текущее местоположение на карте, то необходимо внести в Info.plist следующую пару ключ-значение с типом ``String``:

.. code-block:: bash
   
   Privacy - Location When In Use Usage Description | String | Shows your location on the map
   
На вкладке проекта ``General settings`` в секции ``Linked Frameworks and Libraries`` перетяните ``ngstore.framework`` и ``ngmaplib.framework`` из папки ``Carthage/Build/iOS``.

.. figure:: _static/linked_frameworks_xcode.png
   :name: ngmobdev_linked_frameworks_xcode
   :align: center
   :width: 15cm

   Вкладка проекта **General settings** секция **Linked Frameworks and Libraries**.

Далее следует настроить копирование ``ngstore.framework`` и ``ngmaplib.framework`` в папку сборки. Для этого на вкладке ``Build Phases`` следует вбрать иконку со знаком плюс и в контекстном меню выбрать ``New Run Script Phase``. Далее в секции  
``Run Script`` добавить следующий текст в область под строкой коммандного интерпертатора ``Shell``:

.. code-block:: bash

   /usr/local/bin/carthage copy-frameworks

Ниже в поле ``Input Files`` добавить следующие строки:

.. code-block:: bash

   $(SRCROOT)/Carthage/Build/iOS/ngstore.framework
   $(SRCROOT)/Carthage/Build/iOS/ngmaplib.framework
   
.. figure:: _static/build_run_script_xcode.png
   :name: ngmobdev_build_run_script_xcode
   :align: center
   :width: 15cm   
   
   Вкладка проекта **Build Phases**.

Подробнее см. документацию `Carthage <https://github.com/Carthage/Carthage/>`_.

Библиотека собрана с отключенной опцией **bitcode** поэтому в проекте ее тоже следует выключить. Для этого необходимо в настройках проекта перейти на вкладку ``Build Settings`` и для обоих типов сборок **Debug** и **Release** указать настройку ``Enable bitcode NO``. 

.. figure:: _static/bitcode_disable_xcode.png
   :name: ngmobdev_bitcode_disable_xcode
   :align: center
   :width: 15cm   
   
   Вкладка проекта **Build Settings**.

На заключительном этапе на форму необходимо добавить ``GLK View`` и назначить ему в качестве базового класса ``MapView`` из модуля ``ngmaplib`` или производный класс.

.. figure:: _static/storyboard_xcode.png
   :name: ngmobdev_storyboard_xcode
   :align: center
   :width: 15cm  
   
   Настройка формы окна карты.

Подробнее по работе с библиотекой см. :doc:`документацию по API <swift_api>`.
