.. sectionauthor:: Екатерина Петруненко <ekaterina.petrunenko@nextgis.com>
.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.com>

.. _ng_connect_overview:
    
Overview 
=========

This plugin allows QGIS user to upload and download resources to and from Web GIS or NextGIS Web (further both refer as “Web GIS”) directly from QGIS interface.

With NextGIS Connect you can:

1.	Download geodata from Web GIS to desktop GIS;
2.	Upload vector and raster layers from desktop GIS to Web GIS;
3.	Upload whole QGIS projects to Web GIS , including styles, layer hierarchy, etc;
4.	Create WFS service in one click and edit data directly in Web GIS;
5.      Create WMS service in one click;
6.	Update geodata keeping styles and attributes;
7.	Create resource groups and delete any resources;
8.      Copy the QML layer style in Web GIS to apply it to the layer in QGIS;
9.      Add new vector layer styles from QGIS to the existing style of this layer in Web GIS.





.. warning::

   **Photos** made via NextGIS Collector/Mobile apps and uploaded to Web GIS as attachments to layers **wouldn’t be available** in desktop NextGIS QGIS after downloading these layers through NextGIS Connect plugin.

To **keep the photos** intact while modifying the style, perform the following steps:

1. Add the layer's style from Web GIS to QGIS using NextGIS Connect.
2. Modify the style.
3. Update the style using NextGIS Connect.

.. figure:: _static/ngconnect_modify_keep_photo_en.png
   :align: center
   :width: 20cm   
   
   Updating a style



.. _ng_connect_install:

Installation
=============
   
Connect plugin is a part of `NextGIS QGIS <http://nextgis.com/nextgis-qgis/>`_ distributive and ready to go right after installation of desktop app. Plugin is also available through official QGIS repository, so it can be launched in other QGIS compilations. If necessary, you can check/update the version of the module in the menu section **Modules -> Manage modules -> NextGIS Connect**.


.. _ng_connect_connection:

Сonnecting to your Web GIS
==========================

When plugin is installed its icon appears in a toolbar:

.. figure:: _static/logo.png
   :align: center

Click on the icon to open NextGIS Connect panel.

.. figure:: _static/connect_panel_en.png
   :align: center
   :width: 9cm

If no connection is set at the moment, corresponding message will be shown.

.. figure:: _static/panel-no-connections_en.png
   :align: center
   :width: 9cm
   
   
.. _ng_connect_new_connection:

Create a connection
-------------------

To create a connection you need to know the address of your Web GIS. The address for your own Web GIS can be found at https://my.nextgis.com/webgis. 

.. figure:: _static/my_nextgis.png
   :align: center

   Where to find your Web GIS address

Click on “Settings” button in NextGIS Connect panel.

.. figure:: _static/call_settings_en.png
   :align: center
   :width: 9cm

   Opening Settings menu

In pop-up window press on “New” and fill in the fields:

1.	URL – address of a target Web GIS.
2.	Name – connection id, how it will be shown in the list of connections.

If you want to perform actions that need special permission, uncheck box next to **As guest** and fill in *Login* and *Password* fields with your NextGIS ID credentials. For example, unauthorized users usually can’t create or delete resources. These actions are only available for the owner of the Web GIS and users added to its `team <https://docs.nextgis.com/docs_ngcom/source/create.html#team-management>`_.

.. figure:: _static/nextgis_connect/connection_settings_en.bmp.png
   :align: center

Press “OK”. In the drop-down list of the dialog "Settings" select the connection that becomes active **after closing** dialogue.


.. _ng_connect_main_settings:

Main Settings
-------------

.. figure:: _static/nextgis_connect/settings_en.png
   :align: center

1. Rename forbidden fields – while uploading layer itself or as a part of a project, plugin renames fields forbidden for Web GIS.

2. Open web map automatically on creation – after successful import of a project into Web GIS, web map will be created and automatically opened in browser. 

3. Add WFS layer to QGIS on WFS service creation – after creation of WFS service in Web GIS it will be automatically added to QGIS as a layer.

4. Upload rasters as Cloud Optimized GeoTIFF (COG) - if this option is selected, all rasters will be loaded as Cloud Optimized GeoTIFF (COG).

5. Enable log messages - if this option is selected, then all debug messages will be automatically displayed in the “Debug messages” panel.



.. _ng_connect_proxy:

Proxy server settings
----------------------

If your company uses its own proxy server, you need to specify it in the NextGIS QGIS settings:

Upper menu > Settings > Options > Network > Use Proxy for Web Access

.. figure:: _static/nextgis_connect/proxy_en.png
   :align: center
   :alt: Proxy server settings
   
   Proxy server settings




.. _ng_connect_data_transfer:

Data transfer
=============

NextGIS Connect module allows you to share geodata between QGIS and Web GIS in both directions.

.. _ng_connect_types:

Resource Types
-----------------

The following types of resources are available for data exchange and operation:

.. |resource_vector_point| image:: _static/nextgis_connect/vector_layer_point.png
.. |resource_vector_mpoint| image:: _static/nextgis_connect/vector_layer_mpoint.png
.. |resource_vector_line| image:: _static/nextgis_connect/vector_layer_line.png
.. |resource_vector_mline| image:: _static/nextgis_connect/vector_layer_mline.png
.. |resource_vector_polygon| image:: _static/nextgis_connect/vector_layer_polygon.png
.. |resource_vector_mpolygon| image:: _static/nextgis_connect/vector_layer_mpolygon.png
.. |resource_wfs| image:: _static/resource_wfs_symbol.png
.. |resource_wms| image:: _static/resource_wms_symbol.png
.. |resource_style| image:: _static/resource_style_symbol.png
.. |resource_webmap| image:: _static/resource_webmap_symbol.png
.. |resource_group| image:: _static/nextgis_connect/resource_group.png
.. |raster_layer| image:: _static/raster_layer.png
.. |vector_layer| image:: _static/vector_layer_symbol.png

- |vector_layer| - Vector layer (NGW Vector Layer), it can be: 
  |resource_vector_point| - Point vector layer (NGW Vector Layer); 
  |resource_vector_mpoint| - Multipoint vector layer (NGW Vector Layer); 
  |resource_vector_line| - Line vector layer (NGW Vector Layer);
  |resource_vector_line| - Multiline vector layer (NGW Vector Layer);
  |resource_vector_polygon| - Polygon vector layer (NGW Vector Layer);
  |resource_vector_mpolygon| - Multipolygon vector layer (NGW Vector Layer);
- |resource_style| - Vector layer style. QGIS style gets "(qgis)" prefix, MapServer style - "(ms)"
- |resource_wfs| - WFS Service (NGW WFS Service)
- |resource_wms| - WMS Service (NGW WMS Service)
- |resource_webmap| - Web map (NGW Web Map)
- |resource_group| - Resource group (NGW Web Map)
- |raster_layer| - Raster layer (NGW Raster Layer)







.. _ng_connect_import:

From QGIS to Web GIS 
---------------------

NextGIS Connect module allows you to import:

1. Vector data
2. Raster data
3. Basemaps - only for 'Mini' or 'Premium' plans
4. QGIS project

Algorithm for importing each data type is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#creating-and-uploading-data>`_.

.. figure:: _static/add_to_ngw_en.png
   :align: center
   :width: 9cm

- Vector layer – vector layer with its style will be imported into Web GIS. You can later add this style to a Web Map.
- Raster layer – raster layer with a default style will be created in Web GIS. Style can be added directly to Web Map.
- Upload all - All layers for which option “Import selected layer(s)” is available will be added to Web GIS, as well as all groups with retained hierarchy from QGIS Layers Panel. Also a Web Map will be created and all imported layers will be added to it retaining hierarchy and visibility of QGIS Layers Panel. While importing a project you need to specify the name of the new resource group which will be created in Web GIS. This group will hold all resources imported along with the project. When the process is complete, the Web Map will be opened automatically if corresponding option is selected in plugin settings.
- Update layer style - Web GIS will update the style of the layer, similar to the style of the selected layer in QGIS.
- Add new style to layer - Web GIS will add a new style to the layer, similar to the selected layer in QGIS.

If a layer has **multiple styles**, they will all be uploaded. Their names will be kept. If the style name is "default", the layer's name will be used instead.

Imported resources will be added to a group selected in NextGIS Connect panel. 

* If other type of resource but a group is selected, import will be performed to the closest parent group to selected resource. 

* If no resource is selected, import will be performed to the Main resource group (the root directory).


.. _ng_connect_export:

From Web GIS to QGIS
----------------------

.. figure:: _static/add_to_qgis_en.png
   :align: center
   :width: 9cm


Option is available if one of the following resources is selected in NextGIS Web resource tree:

- Vector layer (NGW Vector Layer) |vector_layer| - GeoJSON vector layer will be created in QGIS;
- WFS service (NGW WFS Service) |resource_wfs| - WFS layer will be created in QGIS;
- WMS Layer - the selected WMS layer will be added to QGIS;
- WMS Service - a WMS layer will be created in QGIS, the data source for which the selected WMS Service will be;
- WMS Connection - you can select the WMS layer from the list to add to QGIS.
- QGIS style of a vector layer |resource_style| - GeoJSON vector layer with the style identical to selected one will be created in QGIS;
- Raster layer (NGW Raster layer)  |raster_layer|  - a GeoTIFF raster layer will be created in QGIS.

.. |resource_vector| image:: _static/resource_vector.png

.. |resource_wfs| image:: _static/resource_wfs.png

For layers with **multiple styles**:

* If you select a layer with multiple styles in the Connect window, all the styles will be added, but you need to chose current style in a dialog window.
* If you select a style in the Connect window, all the styles of the layer weill be added, with the selected style chosen as current style.
* If you select a resource group containing layers with multiple styles, all the styles will be added. The style used as current will be the one with the same name as the layer or the first in alphabetical order. No dialog will be displayed.
* If you add WFS/OGCF, the style with the same name as the layer or the first in alphabetical order will be chosen.


The algorithm for Exporting data to QGIS is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#exporting-data>`_.


.. _ng_connect_cont_menu:

Context Menu
-------------

Context menu may differ depending on resource type.

.. figure:: _static/context_menu_en.png
   :align: center
   :width: 10cm

Common options:

-	Open in WebGIS – open page with selected resource in Web GIS;

-	Rename – rename resource;

-	Delete – delete resource.

-   Edit metadata - edit metadata.


Variable options – depend on resource type:

-	Add to QGIS – option is described above;

-	Create Web Map – available for resources: Vector layer, Vector layer style, Raster layer;

-	Download as QML – available only for QGIS vector layer style.

-       Copy Style (Clipboard) - only available for the QGIS resource Vector Layer Style;

-       Create WFS Service - only available for the Feature Layer resource;

-       Create OGC API - Features service - only available for Vector layer

-       Create WMS service - available only for the Feature layer resource;

-       Duplicate resource - only available for resources: Vector layer and Raster layer;

-       Overwrite selected layer - available only for the Vector layer resource.



.. _ng_connect_update_data:

Updating data and style
-----------------------

.. warning:: 
   When the **layer** is updated, all data of the target layer including attachments (photos, documents) will be cleared. If you need to save them, use WFS. If the style is updated, the attachments will not be affected.

NextGIS Connect allows you to edit data in QGIS and then return it to the Web.
Thus, the data is updated in the Web GIS.
This operation is available if a vector layer is selected in the resource tree.
Select two vector layers: in resource tree and in QGIS Layer Panel. This operation will remove all features from the layer in Web GIS and upload all features from the local layer into that layer. A similar algorithm works for styles as well.

More info about updating `data <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#updating-data>`_ and `styles <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#updating-style>`_.


.. _ng_connect_wfs_wms:

Manage WMS/WFS and OGC services
------------------------

NextGIS Connect module allows publishing vector data using standard protocols :term:`WFS`, :term:`WMS` and OGC.
To do this, in the context menu of the required layer select the appropriate operation.
More info `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#creating-wfs-and-wfs-services>`_.

.. _ng_connect_res_group:

Other operations
-------------------

This block of operations is located in the top menu of the NextGIS Connect.

Create resource group
~~~~~~~~~~~~~~~~~~~~~

New group will be created:

* In the resource group selected via NextGIS Connect panel. 
* If other type of resources but a group is selected - in the closest parent group. 
* If no resource is selected - in the main resource group.

.. figure:: _static/create_group_en.png
   :align: center
   :width: 9cm

   Creating resource group using NextGIS Connect

Refresh
~~~~~~~~~~~

The "refresh" operation will update the entire Web GIS resource tree to the current state.

.. figure:: _static/reload_en.png
   :align: center
   :width: 9cm

   Refreshing Web GIS data

Open Web Map in browser
~~~~~~~~~~~~~~~~~~~~~~~~~~

Option is available if a Web Map (|resource_webmap| NGW Web Map) is selected in NextGIS Connect resource tree. The Web Map will be opened in a new tab of default browser.

.. figure:: _static/open_webmap_en.png
   :align: center
   :width: 10cm

   Opening Web Map from NextGIS Connect


