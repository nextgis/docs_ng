.. sectionauthor:: Dmitry Baryshnikov <dmitry.baryshnikov@nextgis.com>
.. NextGIS Mobile iOS SDK

NextGIS iOS SDK
================

Intro
----------

NextGIS iOS SDK is set of libraries for support work with geodata in mobile application for iPhone and iPad. The SDK includes:

* `nextgis_datastore <https://github.com/nextgis/nextgis_datastore>`_ library
* `ios_maplib <https://github.com/nextgis/ios_maplib>`_ library

The **nextgis_datastore** library is written on ``С++11`` and based on `GDAL <http://gdal.org/>`_. The library supports the following functionality:

* create, modify and delety geodata (raster and vector)
* edit vector geodata (modify geometry and attributes)
* geodata managment (copy, move, various format import/export etc.)
* geodata rendering as maps using `OpenGL/OpenGL ES`
* utility functions (network requests, oAuth2, json)
* ``nextgis.com``/``NextGIS Web`` integration (under development now)

The library has ``С API`` and bindings to other programming languages using ``swig``. 

The **ios_maplib** library is written on ``Swift`` and acts as easy wrapper around C API nextgis_datastore.

Install
----------

To use SDK :program:`Xcode 8` or higher required. Also the ``Carthage`` utility required.  Carthage is intended to be the simplest way to add frameworks to your Cocoa application. To install Carthage follow instruction at `Cathage site <https://github.com/Carthage/Carthage/>`_. 

In your project folder create ``Cartfile`` with folloing text:

.. code-block:: bash

   github "nextgis/ios_maplib"

In terminal execute command:

.. code-block:: bash

   carthage update --platform "iOS"

The command will download and install all necessary components.

Add to project
----------------------

If you plan to show current location, you need add to Info.plist following pair fr key-value with ``String`` type:

.. code-block:: bash
   
   Privacy - Location When In Use Usage Description | String | Shows your location on the map
   
In your app target’s ``General settings`` tab in ``Linked Frameworks and Libraries`` section, drag and drop``ngstore.framework`` and ``ngmaplib.framework`` from ``Carthage/Build/iOS`` folder on disk.

.. figure:: _static/linked_frameworks_xcode.png
   :name: ngmobdev_linked_frameworks_xcode
   :align: center
   :width: 15cm

   **General settings** tab **Linked Frameworks and Libraries** section.

Next you need to setup copy the ``ngstore.framework`` and ``ngmaplib.framework`` to building directory. In ``Build Phases`` tab click the + icon and in context menu select ``New Run Script Phase``. In  
``Run Script`` section add following text to the script area below the ``Shell``:

.. code-block:: bash

   /usr/local/bin/carthage copy-frameworks

Next in ``Input Files`` field add following lines:

.. code-block:: bash

   $(SRCROOT)/Carthage/Build/iOS/ngstore.framework
   $(SRCROOT)/Carthage/Build/iOS/ngmaplib.framework
   
.. figure:: _static/build_run_script_xcode.png
   :name: ngmobdev_build_run_script_xcode
   :align: center
   :width: 15cm   
   
   **Build Phases** tab.

The details see in `Carthage <https://github.com/Carthage/Carthage/>`_ documentaion.

The library was build with disabled **bitcode** option, so in your project disable it too. In your app target’s select ``Build Settings`` tab and for both build types (**Debug** and **Release**) set option ``Enable bitcode NO``. 

.. figure:: _static/bitcode_disable_xcode.png
   :name: ngmobdev_bitcode_disable_xcode
   :align: center
   :width: 15cm   
   
   **Build Settings** tab.

At last step add to your View controller the ``GLK View`` and set put to custom class input field the ``MapView`` class from the ``ngmaplib`` module or some derived class.

.. figure:: _static/storyboard_xcode.png
   :name: ngmobdev_storyboard_xcode
   :align: center
   :width: 15cm  
   
   Map view form setup.

The SDK API can be found in :doc:`documentation <swift_api>`.

See demo projects at this :doc:`page <ios_demos>`.
