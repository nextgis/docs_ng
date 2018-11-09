.. sectionauthor:: Dmitry Baryshnikov <dmitry.baryshnikov@nextgis.com>
.. NextGIS Mobile Android SDK

NextGIS Android SDK
====================

Intro
----------

NextGIS Android SDK is a set of libraries used to support work with geodata in mobile applications for Android OS. The SDK includes:

* `nextgis_datastore <https://github.com/nextgis/nextgis_datastore>`_ library
* `android_maplib <https://github.com/nextgis/android_maplib>`_ library

The **nextgis_datastore** library is written in ``С++11`` and based on `GDAL <http://gdal.org/>`_. The library supports the following functionality:

* create, modify and delete geodata (raster and vector)
* edit vector geodata (modify geometry and attributes)
* geodata management (copy, move, various formats import/export, etc.)
* geodata rendering as maps using `OpenGL/OpenGL ES`
* utility functions (network requests, oAuth2, json)
* ``nextgis.com``/``NextGIS Web`` integration (under development)

The library has ``С API`` and bindings to android java/kotlin programming languages using ``jni``.

**android_maplib** library is written on ``Kotlin`` and acts as easy wrapper around C API nextgis_datastore.

Install
----------

To use SDK the :program:`Android Studio` required. You need to add SDK to your project.

Add to project
----------------------

To add ``NextGIS Mobile SDK`` to your project follow these steps:

1. Launch :program:`Android Studio`.
2. Open you application ``build.gradle`` file.
3. Make sure that the parameter ``minSdkVersion`` has API level 14 or higher.
4. Add following line to dependency block:

.. code-block:: groovy

    dependencies {
      implementation 'com.nextgis.maplib:maplib:3.0.+'
    }

Add map
-----------------

You need to add map into your application:

1. As soon as possible initialize the library:

   .. code-block:: kotlin

      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_main)

          API.init(this@MainActivity)
      }

2. Add ``MapView`` into the application layout:

   .. code-block:: xml

       <com.nextgis.maplib.MapView
            android:id="@+id/mapView"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

3. Create or open map document file:

   .. code-block:: kotlin

      val map = API.getMap("main")


4. Link map with view and enable rendering (rendering is frozen by default):

   .. code-block:: kotlin

      val mapView = findViewById<MapView>(R.id.mapView)
      if(mapView != null) {
          mapView.setMap(map)
      }
      mapView.freeze = false
      
Create feature class
-------------------------

To create feature class in datastore follow these steps:

1. Get or create datastore. You can select any name for a datastore (i.e., *store*).

   .. code-block:: kotlin
   
      val dataStore = API.getStore("store")
      
2. Create feature class in a datastore with needed definitions. 

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
      
3. Load spatial data to the feature class.
       
   .. code-block:: kotlin

      // create coordinates list
      data class PtCoord(val name: String, val x: Double, val y: Double)
      val coordinates = listOf(
        PtCoord("Moscow", 37.616667, 55.75),
        PtCoord("London", -0.1275, 51.507222),
        PtCoord("Washington", -77.016389, 38.904722),
        PtCoord("Beijing", 116.383333, 39.916667)
      )
      
      // Project from EPSG:4326 to EPSG:3857
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

Load feature class to datastore
----------------------------------

To load feature class from GIS file format to datastore follow these steps:

1. Get or create datastore.  You can select any name for a datastore (i.e., *store*).

   .. code-block:: kotlin
   
      val dataStore = API.getStore("store")

2. From catalog get a feature class object if GIS file format and copy it to the datastore.  
        
   .. code-block:: kotlin
   
      val tmpDir = API.getTmpDirectory()
      val testGeojsonObj = tmpDir?.child("test.geojson")
      val copyOptions = mapOf(
        "CREATE_OVERVIEWS" to "ON",
        "NEW_NAME" to "trees"
      )

      val createResult = testGeojsonObj?.copy(Object.Type.FC_GPKG, store!!, true, copyOptions) ?: false
      val treesFC = Object.forceChildToFeatureClass(store?.child("trees")!!)

Create raster  
---------------------------

To create raster set following settings:

* raster extent
* name
* XYZ source URL
* minimum and maximum zoom levels
* raster spatial reference in EPSG code 

   .. code-block:: kotlin
   
      val bbox = Envelope(-20037508.34, 20037508.34, -20037508.34, 20037508.34)
      val baseMap = dataDir.createTMS("osm.wconn", "http://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    3857, 0, 18, bbox, bbox, 14)

Add layer to a map with style 
----------------------------------

To add new layer to the map you need:

1. Add vector layer to a map

   .. code-block:: kotlin

      val pointsLayer = map.addLayer("Points", pointsFC)
      
2. Set style name 

   .. code-block:: kotlin
         
      pointsLayer.styleName = "pointsLayer"
                    
3. Setup style
                    
   .. code-block:: kotlin
   
      val style = pointsLayer.style
      style.setString("color", colorToHexString(Color.rgb(0, 190,120)))
      style.setDouble("size", 8.0)
      style.setInteger("type", 6) // Star symbol

4. Apply modified style to the layer

   .. code-block:: kotlin
   
      pointsLayer.style = style      

SDK API References
-------------------

The SDK API can be found in :doc:`documentation <kotlin_api>`.

Demo projects
--------------

See demo projects at this :doc:`page <android_demos>`.
