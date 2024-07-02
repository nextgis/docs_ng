.. _ng_connect_data_transfer:

Data transfer
==============

NextGIS Connect module allows you to share geodata between QGIS and Web GIS in both directions. See below for the specifics.

.. _ng_connect_types:

Resource types 
--------------

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
.. |basemap_symbol| image:: _static/basemap_symbol.png
.. |tms_service_symbol| image:: _static/tms_service_symbol.png
.. |postgis_layer_symbol| image:: _static/postgis_layer_symbol.png
.. |demo_project_symbol| image:: _static/demo_project_symbol.png
.. |wms_layer_symbol| image:: _static/wms_layer_symbol.png
.. |wms_connection_symbol| image:: _static/wms_connection_symbol.png

- |vector_layer| - Vector layer (NGW Vector Layer), which can be:  
  |resource_vector_point| - Point vector layer (NGW Vector Layer); 
  |resource_vector_mpoint| - Multipoint vector layer (NGW Vector Layer);  
  |resource_vector_line| - Line vector layer (NGW Vector Layer); 
  |resource_vector_line| - Multiline vector layer (NGW Vector Layer); 
  |resource_vector_polygon| - Polygon vector layer (NGW Vector Layer); 
  |resource_vector_mpolygon| - Multipolygon vector layer (NGW Vector Layer); 

- |resource_style| - Vector layer style. QGIS style gets "(qgis)" prefix, MapServer style - "(ms)"
- |resource_wfs| - WFS Service (NGW WFS Service)
- |resource_wms| - WMS Service (NGW WMS Service)
- |tms_service_symbol| - TMS Layer
- |postgis_layer_symbol| - PostGIS Layer
- |raster_layer| - Raster layer (NGW Raster Layer)
- |basemap_symbol| - Basemap
- |resource_webmap| - Web Map (NGW Web Map)
- |resource_group| - Resource group (NGW Web Map)




.. _ng_connect_import:

From QGIS to Web GIS 
-------------------------------

NextGIS Connect module allows you to import:

1. Vector data
2. Raster data
3. Basemaps - only for `'Mini' or 'Premium' plans <https://nextgis.com/pricing-base/>`_
4. Entire QGIS project


Algorithm for importing each data type is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#creating-and-uploading-data>`_.

.. figure:: _static/add_to_ngw_en.png
   :align: center
   :width: 10cm
   
   Data import menu

- Vector layer – vector layer with its style will be imported into Web GIS.  
  You can later add this style to a Web Map.
- Raster layer – raster layer with a default style will be created in Web GIS.  
  Style can be added directly to Web Map.
- Upload all - All layers for which the import option is available will be added to Web GIS, as well as all groups, retaining the hierarchy from QGIS Layers Panel.  Also a Web Map will be created and all imported layers will be added to it retaining hierarchy and visibility of QGIS Layers Panel. While importing a project you need to specify the name of the new resource group which will be created in Web GIS. This group will hold all resources imported along with the project. When the process is complete, the Web Map will be opened automatically if corresponding option is selected in plugin settings.
- Update layer style - Web GIS will update the style of the layer to match the style of the selected layer in QGIS.
- Add new style to layer - Web GIS will add to the layer a new style, similar to the selected layer in QGIS.

If a layer has **multiple styles**, they will all be uploaded. Their names will be kept. If the style name is "default", the layer's name will be used instead. 


Imported resources will be added to the group selected in NextGIS Connect panel. 

* If other type of resource but a group is selected, import will be performed to the closest parent group to selected resource.
* If no resource is selected, import will be performed to the Main resource group (the root directory).


.. warning::

    **Photos** made via NextGIS Collector/Mobile apps and uploaded to Web GIS as attachments to layers **wouldn't be available** in desktop NextGIS QGIS after downloading these layers through NextGIS Connect plugin.
   



How to keep the attachments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To **keep the photos** intact while modifying the style, perform the following steps:

1. Add the layer's style from Web GIS to QGIS using NextGIS Connect.
2. Modify the style.
3. Update the style using NextGIS Connect. 

.. figure:: _static/ngconnect_modify_keep_photo_en.png
   :align: center
   :width: 20cm   
   
   Updating a style

.. _ng_connect_export:

From Web GIS to QGIS
---------------------------------

.. figure:: _static/add_to_qgis_en.png
   :align: center
   :alt: Add to QGIS
   :width: 10cm
   
   Button for data transfer to QGIS

Option is available if one of the following resources is selected in NextGIS Web resource tree:

- Vector layer (NGW Vector Layer) |vector_layer| - GeoJSON vector layer will be created in QGIS;
- WFS service (NGW WFS Service) |resource_wfs| - WFS layer will be created in QGIS;
- WMS Layer - the selected WMS layer will be added to QGIS;
- WMS Service - a WMS layer will be created in QGIS, the data source for which the selected WMS Service will be;
- WMS Connection - you can select the WMS layer from the list to add to QGIS;
- TMS Layer |tms_service_symbol|;
- PostGIS Layeer |postgis_layer_symbol|;
- QGIS style of a vector layer |resource_style| - GeoJSON vector layer with the style identical to selected one will be created in QGIS;
- Raster layer (NGW Raster layer)  |raster_layer|  - a GeoTIFF raster layer will be created in QGIS;
- Basemap|basemap_symbol|;
- Web Map |resource_webmap| - a QGIS project will be created containing layers, styles and basemaps;
- `Demo Project <https://docs.nextgis.com/docs_ngcom/source/demoprojects.html>`_ |demo_project_symbol| - a QGIS project will be created, containing layers, styles and basemaps.


For layers with **multiple styles**:

* If you select a layer with multiple styles in the Connect window, all the styles will be added, but you need to chose current style in a dialog window.
* If you select a style in the Connect window, all the styles of the layer will be added, with the selected style chosen as current style.
* If you select a resource group containing layers with multiple styles, all the styles will be added. The style used as current will be the one with the same name as the layer or the first in alphabetical order.  No dialog will be displayed.
* If you add WFS/OGCF, the style with the same name as the layer or the first in alphabetical order will be chosen.

The algorithm for Exporting data to QGIS is described `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#exporting-data>`_.

.. _ng_connect_cont_menu:

Context Menu
----------------
Context menu may differ depending on resource type.  

.. figure:: _static/context_menu_en.png
   :align: center
   :alt: Context menu for a qgis vector style
   :width: 9cm
   
   Context menu example

Common options for all resource types:

- Open in WebGIS – open the page of the selected resource in Web GIS;

- Rename resource;

- Delete resource;

- Edit metadata.


Variable options – depend on resource type:

- Add to QGIS – option is described above;

- Create Web Map – available for resources: Vector layer, Vector layer style, Raster layer, WMS layer;

- Download as QML – available only for QGIS vector layer style;

- Copy Style (Clipboard) - only available for QGIS Vector Layer Style;

- Create WFS Service - only available for Vector layer;

- Create OGC API - Features service - only available for Vector layer;

- Create WMS service - available only for Vector layer;

- Duplicate resource - only available for resources: Vector layer and Raster layer;

- Overwrite selected layer - available only for Vector layer.


The plugin also allows you to navigate to the Web GIS data directly from the the Layers panel in QGIS. In the layer's context menu find "NextGIS Connect" and press "Open in Web GIS".


.. figure:: _static/ngc_open_from_layertree_en.png
   :align: center
   :alt: Context menu in the layer tree
   :width: 22cm

   Opening Web GIS data from QGIS layer tree


.. _ng_connect_edit_layer:

Edit layers
---------------------

Vector layers added from Web GIS can be edited immediately after import to QGIS. Only one user at a time can edit the layer directly. This allows the layer to be edited even with no Internet connection. The changes will be saved to the device and transfered to Web GIS when the connection is restored.

Layer styles are preserved during both import and export of the edited layer.

.. note::
    This functionality is only available for vector data formats used in QGIS.

1. Enter the edit mode from the layer's context menu or from the toolbar.
2. Make the changes.
3. Exit edit mode. Confirm changes in the pop-up window.
4. The layer will be automatically synchronized.

To check when the layer was last synchronized, hover over the sync symbol.

.. figure:: _static/ngc_check_sync_en.png
   :align: center
   :alt: Sync information
   :width: 16cm

   Synchronization information

Press the symbol to open the layer status window.

.. figure:: _static/ngc_layer_status_en.png
   :align: center
   :width: 10cm
   :alt: Layer status dialog

   Layer status dialog

It has the date and time of the latest synchronization and the status: synchronized or not synchronized.

You can start the process manually by pressing the **Synchronization** button.

.. important::
    While the layer is in edit mode, synchronization is not available.

If changes have been made to the layer in Web GIS since the last synchronization, further synchronization will not be possible and a message will appear. To continue working with the layer you need to reload it by resetting it to the current state it is in NGW. In the synchronization dialog in the dropdown menu select **Reset layer**. Keep in mind that if you reset the layer, all local changes that had not been synchronized will be lost. 

If the edits made in the cloud were incorrect and you need to replace them with local ones, you can use the `Data overwrite <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#ngcom-ngqgis-connect-data-overwrite>`_ function.



.. _ng_connect_update_data:

Update data or styles
--------------------------

.. warning:: 
   When the **layer** is updated, all data of the target layer including attachments (photos, documents) will be cleared. If you need to save them, use WFS. If the style is updated, the attachments will not be affected.

NextGIS Connect allows you to edit data in QGIS and then return it to the Web.
Thus, the data is updated in the Web GIS.
This operation is available if a vector layer is selected in the resource tree. 

Select two vector layers: in the resource tree of NextGIS Connect and in QGIS Layers Panel. This operation will remove all features from the layer in Web GIS and upload all features from the local layer into that layer. A similar algorithm works for styles as well.

More info about updating `data <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#updating-data>`_ and `styles <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#updating-style>`_.




.. _ng_connect_wfs_wms:

Manage data with WMS/WFS and OGC services
----------------------------------------------

NextGIS Connect plugin allows to publish vector data using standard protocols :term:`WFS`, :term:`WMS` and OGC.
To do this, in the context menu of the required layer select the appropriate operation.
More info `here <https://docs.nextgis.com/docs_ngcom/source/ngqgis_connect.html#creating-wfs-and-wfs-services>`_.

.. _ng_connect_lookup:

Lookup tables
------------------------------------------------

In Web GIS you can create `Lookup tables <https://docs.nextgis.com/docs_ngcom/source/lookup.html#ngcom-lookup-table-for-layer>`_ and link them to vector layers.

When the layer is exported from Web GIS to QGIS the values of the lookup table will be added to the layer using value map widget. After that they will be available in the desktop app in the corresponding field of the table when you enter edit mode.

.. figure:: _static/ngc_lookup_en.png
   :align: center
   :width: 20cm

   Lookup table values available during editing in QGIS

In QGIS you can use Value relation widget to add another vector layer as a lookup table or upload a CSV file. When the layer is transfered to Web GIS, a Lookup table resource will be created for it.

.. _ng_connect_res_group:

Other operations
----------------

This block of operations is located in the top menu of the NextGIS Connect.

Create resource group
~~~~~~~~~~~~~~~~~~~~~~~~

New group will be created:

* In the resource group selected via NextGIS Connect panel. 
* If other type of resources but a group is selected - in the closest parent group 
  .
* If no resource is selected - in the main resource group.

.. figure:: _static/create_group_en.png
   :align: center
   :alt: Create new group
   :width: 10cm

   Creating resource group

Refresh
~~~~~~~~~~~~~~~~~~

The "refresh" operation will update the entire Web GIS resource tree to the current state.

.. figure:: _static/reload_en.png
   :align: center
   :alt: Refresh resource tree
   :width: 10cm

   Refreshing Web GIS data

Open Web Map in browser
~~~~~~~~~~~~~~~~~~~~

Option is available if a Web Map (|resource_webmap| NGW Web Map) is selected in NextGIS Connect resource tree. 
The Web Map will be opened in a new tab of default browser.

.. figure:: _static/open_webmap_en.png
   :align: center
   :alt: Open Web Map in browser
   :width: 10cm

   Opening Web Map from NextGIS Connect

