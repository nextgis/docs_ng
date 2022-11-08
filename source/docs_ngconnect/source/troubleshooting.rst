.. sectionauthor:: Roman Gainullov <roman.gainullov@nextgis.com>

    
Troubleshooting
===============

If you encounter any issues while working with the plugin, please use the basic checks described below.

.. _ng_connect_ngw_issues:

Problems connecting to Web GIS (NGW)
---------------------------------------

.. _checkqgis:

Check QGIS version
~~~~~~~~~~~~~~~~~~

Update software if updates are available. Using our `NextGIS QGIS <https://nextgis.com/nextgis-qgis/>`_ follow:

* Check version: Help > About
* Check updates: Help > Check QGIS version
* Restart QGIS after update


.. _checkconnect:

Check NextGIS Connect version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To work, it is recommended to use the latest version of the plugin. You can check and update it as follows:

* Top Menu > Plugins > Manage and install plugins
* If the version is outdated, there will be a message at the top saying that there is an update for the plugin, and an update button will be available in the lower right corner of the window

There are no more updates for QGIS 2.X since NextGIS Connect 0.14.0. Minimum QGIS version is 3.X now.


.. _corp:

For corporate network
~~~~~~~~~~~~~~~~~~~~~~~

If you work in the internal corporate network, set up the settings of your proxy (Settings> Options> Network)


.. _credentials:

Credentials
~~~~~~~~~~~

Check the credentials when creating a connection to Web GIS (URL, username and password). The URL format is https://demo.nextgis.com. If you forgot your password, instructions for recovering are `here <https://docs.nextgis.com/docs_ngcom/source/faq_webgis.html#ngcom-change-passwords-webgis>`_.

.. _rasters:

Issues uploading data
----------------------

If the rasters are not uploaded, check the checkbox in the connection settings “Upload rasters as Cloud Optimized GeoTIFF” (COG).
