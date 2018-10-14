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

.. code-block:: gradle

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

The SDK API can be found in :doc:`documentation <kotlin_api>`.

See demo projects at this :doc:`page <android_demos>`.
