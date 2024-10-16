.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.ru>

.. _docs_geoserv_prem_settings:

Settings
============

.. _geoserv_prem_set_profile:

Profile
--------

**Profile** section contains user information. It is devided into two tabs: *My profile* and *My API keys*.

**My profile** tab has the following settings:

* Login
* Password (can be modified after you log in for the first time)
* Username
* E-mail


.. figure:: _static/geosop_gr_profile1_en.png
   :name: geosop_gr_profile1
   :align: center
   :width: 20cm

   My profile section in NextGIS GeoServices on-premise

**My API keys** are used for integration with other NextGIS services and external applications.
For instance, you'll need an API key to work
In this section Administrator can create and delete API keys.

While creating an API key, Administrator can set an expiration date for it.
Other API key settings include extent boundary, scale limits and origins.

.. figure:: _static/geosop_gr_profile2_en.png
   :name: geosop_gr_profile2
   :align: center
   :width: 20cm

   My API keys section in NextGIS GeoServices on-premise

.. figure:: _static/geosop_gr_profile3_en.png
   :name: geosop_gr_profile3
   :align: center
   :width: 14cm

   Creating a new API key

.. _geoserv_prem_set_users:

Users and user groups
------------------------------------

Available settings depend on user access rights.

Administrator has full access and can create users, user groups, add users to the groups, delete and modify users and groups.

.. figure:: _static/geosop_gr_users1_en.png
   :name: geosop_gr_users1
   :align: center
   :width: 20cm

   Creating and deleting user in NextGIS GeoServices on-premise

To create a new user press **Add** and fill the following fields:

* Login
* Password
* Username
* E-mail
* Group to which the new user will be added (optional)

.. figure:: _static/geosop_gr_users2_en.png
   :name: geosop_gr_users2
   :align: center
   :width: 16cm

   Creating new user in NextGIS GeoServices on-premise

.. figure:: _static/geosop_gr_users3_en.png
   :name: geosop_gr_users3
   :align: center
   :width: 20cm

   List of user groups in NextGIS GeoServices on-premise

To create a User group, in the list of groups press **Add**. Enter the name for the group. You can select users to be included in the group from a dropdown menu.

.. figure:: _static/geosop_gr_users4_en.png
   :name: geosop_gr_users4
   :align: center
   :width: 16cm

   Creating user group in NextGIS GeoServices on-premise


.. _geoserv_prem_set_basemap:

Basemap
--------------

In this section you can upload data and set boundaries for the default basemap tile service.

Input:

* Basemap file
* Boundaries

For **Basemap file** you can upload a PBF file or choose an area from the dropdown list.

.. figure:: _static/geosop_base_mapfile_en.png
   :name: geosop_base1
   :align: center
   :width: 16cm

   Two ways of selecting basemap: from list and from file

You can set the **Boundary** for the service area in several ways:

* draw it on the map in the interface;
* upload a (multi)polygon vector file in GeoJSON format.

If you select an area from the list, its boundaries will be set automatically.

.. important::
   If the boundary is not set, the next data base update will include data of the entire globe, not just the previously uploaded PBF. This would take much more storage space on your device.

.. figure:: _static/geosop_base_boundary_en.png
   :name: geosop_base2
   :align: center
   :width: 16cm

   Ways to set up boundary for basemap

You can modify the boundary or delete it (**Reset map** button) and start from scratch.

When all files are uploaded and the boundaries are set, press **Submit new basemap data** on the top of the page. The process of creating tile service will begin.

.. figure:: _static/geosop_base_submit_en.png
   :name: geosop_base4
   :align: center
   :width: 16cm

   Submit new Basemap data

If you use custom PBF, upload progress is displayed on the same tab and in the Log tab. After the process is completed successfully, the progress bar becomes green and a tick appears at the end.

.. figure:: _static/geosop_base_progress_en.png
   :name: geosop_base3
   :align: center
   :width: 16cm

   Uploading custom file

.. figure:: _static/geosop_base_complete_en.png
   :name: geosop_base3
   :align: center
   :width: 16cm

   Upload of custom file complete

In the Log the process will be marked by a green dot.

.. figure:: _static/geosop_base_log_en.png
   :name: geosop_base5
   :align: center
   :width: 16cm

   Upload progress status in the Log tab

Default basemap that you configured can be found in the Services section in the Public group. Use the link for the tile service XYZ to add it to external software such as NextGIS Web or QGIS. 

.. figure:: _static/geosop_base_XYZ_en.png
   :name: geosop_base6
   :align: center
   :width: 20cm

   Link to be used in external apps


.. _geoserv_prem_set_log:

Log
-------

The log registers data processing history and other actions performed by the app. 
Log entries include status, process source, beginning and end times, task ID and messages.

.. figure:: _static/geosop_journal1_en.png
   :name: geosop_journal1
   :align: center
   :width: 20cm

   Log tab in NextGIS GeoServices on-premise

.. figure:: _static/geosop_journal_messages_en.png
   :name: geosop_journal2
   :align: center
   :width: 20cm

   Messages for a process in the log


About
-----------

This section has information on the current versions of the components.

.. figure:: _static/geosop_about_en.png
   :name: geosop_about
   :align: center
   :width: 20cm

   Component version info in NextGIS GeoServices on-premise
 
