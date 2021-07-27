.. sectionauthor:: Екатерина Петруненко <ekaterina.petrunenko@nextgis.com>
.. sectionauthor:: Роман Гайнуллов <roman.gainullov@nextgis.com>

.. _ng_connect:
    
NextGIS Connect
===============

This plugin allows QGIS user to upload and download resources to and from Web GIS or NextGIS Web (further both refer as “Web GIS”) directly from QGIS interface.

With NextGIS Connect you can:

1.	Download geodata from Web GIS to desktop GIS;
2.	Upload vector and raster layers from desktop GIS to Web GIS;
3.	Upload whole QGIS projects to Web GIS , including styles, layer hierarchy, etc;
4.	Create WFS service in one click and edit data directly in Web GIS;
5.	Update geodata keeping styles and attributes;
6.	Create resource groups and delete any resources.


.. important::
	If you plan to share large data through NextGIS Connect, you might need to configure QGIS timeouts for network requests. This setting is in the menu section **Settings** -> **Options** -> **Network** -> Timeout for network requests (ms). The recommended value is **300,000**, it can be increased if necessary.


.. warning::

   **Photos** made via NextGIS Collector/Mobile apps and uploaded to Web GIS as attachments to layers **wouldn’t be available** in desktop NextGIS QGIS after downloading these layers through NextGIS Connect plugin.
   

.. _ng_connect_install:

Installing NextGIS Connect
--------------------------
   
Connect plugin is a part of `NextGIS QGIS <http://nextgis.com/nextgis-qgis/>`_ distributive and ready to go right after installation of desktop app. Plugin is also available through official QGIS repository, so it can be launched in other QGIS compilations. If necessary, you can check/update the version of the module in the menu section **Modules -> Manage modules -> NextGIS Connect**.


.. _ng_connect_connection:

Creating and configuring a connection
-------------------------------------

When plugin is installed its icon appears in a toolbar:

.. figure:: _static/nextgis_connect/logo.png
   :align: center

Clicking on the icon calls NextGIS Connect panel.

.. figure:: _static/nextgis_connect/panel.png
   :align: center

If no connection is set at the moment, corresponding message will be shown.

.. figure:: _static/nextgis_connect/panel_no_connections.png
   :align: center
   
   
.. _ng_connect_set_connection:

Create a Connection
~~~~~~~~~~~~~~~~~~~  

To create a connection you need to know an address of a target Web GIS. For instance, if you’ve created your own Web GIS, its address can be found on https://my.nextgis.com/webgis page. 

.. figure:: _static/nextgis_connect/my_nextgis.png
   :align: center

Click on “Settings” button in NextGIS Connect panel.

.. figure:: _static/nextgis_connect/call_settings.png
   :align: center

In pop-up window press on “New” and fill in the fields:

1.	URL – address of a target Web GIS.
2.	Name – connection id, how it will be shown in the list of connections.

If you want to perform actions that need special permission, uncheck box next to **As guest** and fill in *Login* and *Password* fields. For example, unauthorized users usually can’t create or delete resources.

.. figure:: _static/nextgis_connect/connection_settings.png
   :align: center

Press “OK”. In the drop-down list of the dialog "Settings" select the connection that becomes active **after closing** dialogue.


.. _ng_connect_main_settings:

Main Settings
~~~~~~~~~~~~~

.. figure:: _static/nextgis_connect/settings.png
   :align: center

1. Rename forbidden fields – while uploading layer itself or as a part of a project, plugin renames fields forbidden for Web GIS.

2. Fix incorrect geometries – while uploading layer itself or as a part of a project, plugin transforms geometries into same type.

3. Abort project import after first layer import failure – plugin wouldn’t keep on uploading project if any layer is failed to be imported into Web GIS.

4. Open web map automatically on creation – after successful import of a project into Web GIS, web map will be created and automatically opened in browser. 

5. Add WFS layer to QGIS on WFS service creation – after creation of WFS service in Web GIS it will be automatically added to QGIS as a layer.


.. _ng_connect_types:

Resource Types
-------------------------

The following types of resources are available for data exchange and operation:

.. |resource_vector_point| image:: _static/nextgis_connect/vector_layer_point.png
.. |resource_vector_mpoint| image:: _static/nextgis_connect/vector_layer_mpoint.png
.. |resource_vector_line| image:: _static/nextgis_connect/vector_layer_line.png
.. |resource_vector_mline| image:: _static/nextgis_connect/vector_layer_mline.png
.. |resource_vector_polygon| image:: _static/nextgis_connect/vector_layer_polygon.png
.. |resource_vector_mpolygon| image:: _static/nextgis_connect/vector_layer_mpolygon.png
.. |resource_wfs| image:: _static/nextgis_connect/resource_wfs.png
.. |resource_wms| image:: _static/nextgis_connect/resource_wms.png
.. |resource_style| image:: _static/nextgis_connect/resource_style.png
.. |resource_webmap| image:: _static/nextgis_connect/resource_webmap.png
.. |resource_group| image:: _static/nextgis_connect/resource_group.png
- |resource_vector_point| - Point vector layer (NGW Vector Layer)
- |resource_vector_mpoint| - Multipoint vector layer (NGW Vector Layer)
- |resource_vector_line| - Line vector layer (NGW Vector Layer)
- |resource_vector_line| - Multiline vector layer (NGW Vector Layer)
- |resource_vector_polygon| - Polygon vector layer (NGW Vector Layer)
- |resource_vector_mpolygon| - Multipolygon vector layer (NGW Vector Layer)
- |resource_style| - Vector layer style. QGIS style gets "(qgis)" prefix, MapServer style - "(ms)"
- |resource_wfs| - WFS Service (NGW WFS Service)
- |resource_wms| - WMS Service (NGW WMS Service)
- |resource_webmap| - Web map (NGW Web Map)
- |resource_group| - Resource group (NGW Web Map)



.. _ng_connect_data_imp_exp:

Data sharing
------------

NextGIS Connect module allows you to share geodata between QGIS and Web GIS in both directions.

.. _ng_connect_import:

Importing data into Web GIS from QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NextGIS Connect module allows you to import:

1. Vector data
2. Raster data
3. Basemaps - only for 'Mini' or 'Premium' plans
4. QGIS project

Algorithm for importing each data type is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#creating-and-uploading-data>`_.

.. figure:: _static/nextgis_connect/add_to_ngw.png
   :align: center

- Vector layer – vector layer with its style will be imported into Web GIS. Style can be added directly on web map.
- Raster layer – raster layer with a default style will be created in Web GIS. Style can be added directly on web map.
- Current project - All layers for which option “Import selected layer(s)” is available will be added to Web GIS, as well as all groups with retained hierarchy from QGIS Layers Panel. Also web map will be created and all imported layers will be added to it retaining hierarchy and visibility of QGIS Layers Panel. While importing a project you need to specify the name of the new resource group which will be created in Web GIS. This group will hold all resources imported along with a project. Upon project import created web map will be opened automatically if corresponding option is selected in plugin settings.

Imported resources will be added to a group selected in NextGIS Connect panel. If other type of resources but a group is selected, import will be performed to a closest parent group to selected resource. If no resource is selected, import will be performed to the root directory.


.. _ng_connect_export:

Exporting data from Web GIS to QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: _static/nextgis_connect/add_to_qgis.png
   :align: center


Option is available if one of the following resources is selected in NextGIS Web resource tree:

- Vector layer (NGW Vector Layer) |resource_vector| - GeoJSON vector layer will be created in QGIS;
- WFS service (NGW WFS Service) |resource_wfs| - WFS layer will be created in QGIS;
- QGIS style of a vector layer |resource_style| - GeoJSON vector layer with the style identical to selected one will be created in QGIS;
- WMS Layer - the selected WMS layer will be added to QGIS;
- WMS Service - a WMS layer will be created in QGIS, the data source for which the selected WMS Service will be;
- WFS Connection - you can select the WMS layer from the list to add to QGIS.

.. |resource_vector| image:: _static/nextgis_connect/resource_vector.png

.. |resource_wfs| image:: _static/nextgis_connect/resource_wfs.png


The algorithm for Exporting data to QGIS is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#exporting-data>`_.


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

Publishing data by WMS/WFS protocols
-------------------------------------

NextGIS Connect module allows publishing vector data using standard protocols :term:`WFS` and :term:`WMS`.
To do this, in the context menu of the required layer select the appropriate operation.
More info `here <https://docs.nextgiscom/docs_ngcom/source/ngqgis_connect.html#creating-wfs-and-wfs-services>`_.


.. _ng_connect_res_group:

Other operations
----------------

This block of operations is located in the top menu of the NextGIS Connect.

New group will be created in resource group selected via NextGIS Connect panel. If other type of resources but a group is selected, group will be created in a closest parent group to selected resource. If no resource is selected, group will be created in the root directory.

.. figure:: _static/nextgis_connect/create_group.png
   :align: center


The "update" operation will update the entire Web GIS resource tree to the current state.

.. figure:: _static/nextgis_connect/reload.png
   :align: center


Option is available if web map (NGW Web Map) |resource_webmap|  is selected in NextGIS Connect resource tree. Map will be opened in a new tab of default browser.

.. |resource_webmap| image:: _static/nextgis_connect/resource_webmap.png

.. figure:: _static/nextgis_connect/open_webmap.png
   :align: center


"Delete" a resource permanently deletes the selected geodata.


Context Menu
-----------------------
Context menu may differ depending on resource type.

.. figure:: _static/nextgis_connect/context_menu.png
   :align: center

Common options:

-	Open in WebGIS – open page with selected resource in Web GIS;

-	Rename – rename resource;

-	Delete – delete resource.


Variable options – depend on resource type:

-	Add to QGIS – option is described above;

-	Create Web Map – available for resources: Vector layer, Vector layer style, Raster layer;

-	Download as QML – available only for QGIS vector layer style.

