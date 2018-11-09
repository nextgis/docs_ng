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
      
Создание векторного слоя
-------------------------

Для создания векторного слоя необходимо выполнить ряд шагов:

1. Получить или создать хранилище. Имя хранилища может быть любым  (например, *store*).

   .. code-block:: kotlin
   
      val dataStore = API.getStore("store")
      
2. Создать в хранилище векторный слой с необходимой структурой. 

   .. code-block:: kotlin
   
      val options = mapOf(
        "CREATE_OVERVIEWS" to "ON",
        "ZOOM_LEVELS" to "2,3,4,5,6,7,8,9,10,11,12,13,14"
      )

      val fields = listOf(
        Field("long", "long", Field.Type.REAL),
        Field("lat", "lat", Field.Type.REAL),
        Field("datetime", "datetime", Field.Type.DATE, "CURRENT_TIMESTAMP"),
        Field("name", "name", Field.Type.STRING)
      )

      val pointsFC = dataStore.createFeatureClass("points", Geometry.Type.POINT, fields, options)
      
3. Загрузить в созданный слой геоданные.
       
   .. code-block:: kotlin

      // Сформируем массив координат
      data class PtCoord(val name: String, val x: Double, val y: Double)
      val coordinates = listOf(
        PtCoord("Moscow", 37.616667, 55.75),
        PtCoord("London", -0.1275, 51.507222),
        PtCoord("Washington", -77.016389, 38.904722),
        PtCoord("Beijing", 116.383333, 39.916667)
      )
      
      // Преобразуем системку координат из EPSG:4326 в EPSG:3857
      val coordTransform = CoordinateTransformation.new(4326, 3857)

      for(coordinate in coordinates) {
        val feature = pointsFC.createFeature()
        if(feature != null) {
          val geom = feature.createGeometry() as? GeoPoint
          if(geom != null) {
            val point = Point(coordinate.x, coordinate.y)
            val transformPoint = coordTransform.transform(point)
            geom.setCoordinates(transformPoint)
            feature.geometry = geom
            feature.setField(0, coordinate.x)
            feature.setField(1, coordinate.y)
            feature.setField(3, coordinate.name)
            pointsFC.insertFeature(feature)
          }
        }
      }

Загрузка векторного слоя
-------------------------

Для загрузки векторного слоя в хранилище из файла ГИС формата необходимо выполнить 
следующие шаги:

1. Получить или создать хранилище. Имя хранилища может быть любым  (например, *store*).

   .. code-block:: kotlin
   
      val dataStore = API.getStore("store")

2. Получить из каталога ссылку на файл ГИС формата и скопировать его в хранилище.  
        
   .. code-block:: kotlin
   
      val tmpDir = API.getTmpDirectory()
      val testGeojsonObj = tmpDir?.child("test.geojson")
      val copyOptions = mapOf(
        "CREATE_OVERVIEWS" to "ON",
        "NEW_NAME" to "trees"
      )

      val createResult = testGeojsonObj?.copy(Object.Type.FC_GPKG, store!!, true, copyOptions) ?: false
      val treesFC = Object.forceChildToFeatureClass(store?.child("trees")!!)

Создание растрового слоя  
---------------------------

Для создания растрового слоя необходимо задать следующие сведения:

* охват растрового слоя
* имя слоя
* URL к источникам тайлов XYZ
* минимальный и максимальный уровни увеличения (zoom level)
* система координат слоя EPSG  

   .. code-block:: kotlin
   
      val bbox = Envelope(-20037508.34, 20037508.34, -20037508.34, 20037508.34)
      val baseMap = dataDir.createTMS("osm.wconn", "http://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    3857, 0, 18, bbox, bbox, 14)

Создание слоя на карте со стилем 
----------------------------------

Для добавления слоя в карту необходимо выполнить:

1. Добавить векторный слой в карту

   .. code-block:: kotlin

      val pointsLayer = map.addLayer("Points", pointsFC)
      
2. Установить тип стиля 

   .. code-block:: kotlin
         
      pointsLayer.styleName = "pointsLayer"
                    
3. Настроить свойства стиля

                    
   .. code-block:: kotlin
   
      val style = pointsLayer.style
      style.setString("color", colorToHexString(Color.rgb(0, 190,120)))
      style.setDouble("size", 8.0)
      style.setInteger("type", 6) // Star symbol

4. Применить модифицированный стиль к слою

   .. code-block:: kotlin
   
      pointsLayer.style = style

Документация по API
---------------------

Подробнее по работе с библиотекой см. :doc:`документацию по API <kotlin_api>`.

Демо проекты
-------------

Демо проекты размещены на отдельной :doc:`странице <android_demos>`.
