.. sectionauthor:: Дмитрий Барышников <dmitry.baryshnikov@nextgis.ru>
.. NextGIS Mobile Android SDK

NextGIS Android SDK v3
======================

Введение
----------

NextGIS Android SDK это набор библиотек для работы с геоданными в мобильном приложении для Android. В состав библиотек входят:

* Библиотека `nextgis_datastore <https://github.com/nextgis/nextgis_datastore>`_
* Библиотека `android_maplib <https://github.com/nextgis/android_maplib>`_

Библиотека **nextgis_datastore** написана на ``С++11`` и основана на `GDAL <http://gdal.org/>`_. Она обеспечивает следующие возможности:

* создание, изменение и удаление геоданных (растровых и векторных)
* редактирование геоданных (модификация географии и атрибутики)
* управление геоданными (копирование, перенос, изменение формата и др.)
* визуализацию геоданных в виде карт при помощи `OpenGL/OpenGL ES`
* вспомогательные функции (работа с сетью, oAuth2, json)
* интеграция с ``nextgis.com``/``NextGIS Web`` (under development now)

Для взаимодействия с библиотекой используется ``С API`` и биндинги для android java/kotlin при помощи ``jni``.

Библиотека **android_maplib** написана на ``Kotlin`` и представляет собой удобную обвязку вокруг C API nextgis_datastore.

Установка
----------

Для использования SDK необходимо :program:`Android Studio`. Для использования SDK необходимо подключить его к проекту.

Подключение к проекту
----------------------

Для подключения ``NextGIS Mobile SDK`` выполните следующие шаги:

1. Запустите :program:`Android Studio`.
2. Откройте файл ``build.gradle`` вашего приложения.
3. Убедитесь что параметр ``minSdkVersion`` в проекте соответсвует API уровня 14 или выше.
4. В блоке зависимостей добавть новую строку вида:

.. code-block:: groovy

    dependencies {
      implementation 'com.nextgis.maplib:maplib:3.0.+'
    }

Добавлениe карты
-----------------

Для добавления карты в приложение необходимо:

1. Как можно раньше в коде вызвать инициализацию библиотеки:

   .. code-block:: kotlin

      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_main)

          API.init(this@MainActivity)
      }

2. Добавить ``MapView`` в компановку окна:

   .. code-block:: xml

       <com.nextgis.maplib.MapView
            android:id="@+id/mapView"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

3. Создать или открыть файл карты:

   .. code-block:: kotlin

      val map = API.getMap("main")


4. Связать карту с окном и включить отрисовку (по-умолчанию отрисовка отключена):

   .. code-block:: kotlin

      val mapView = findViewById<MapView>(R.id.mapView)
      if(mapView != null) {
          mapView.setMap(map)
      }
      mapView.freeze = false

Документация по API
---------------------

Подробнее по работе с библиотекой см. :doc:`документацию по API <kotlin_api>`.

Демо проекты
-------------

Демо проекты размещены на отдельной :doc:`странице <android_demos>`.
