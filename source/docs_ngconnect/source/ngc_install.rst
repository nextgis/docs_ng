.. _ng_connect_install:

Installation
==============

To download NextGIS Connect plugin, from the main menu open *Plugins ‣ Manage and install plugins*. Start typing the name of the plugin in the search bar, select it in the list and press **Install**.

NextGIS Connect plugin is a part of `NextGIS QGIS <http://nextgis.com/nextgis-qgis/>`_ distributive and is ready to go right after installation of desktop app.

If you need to check the version of the plugin or update it, go to *Plugins‣ Manage and install plugins ‣ NextGIS Connect*. 



.. _ng_connect_connection:

Connecting to your Web GIS
===========================

When the plugin is installed, its icon appears in the toolbar:  

.. figure:: _static/logo_connect.png
   :align: center
   :alt: NextGIS Connect icon

Click on the icon to open NextGIS Connect panel.

.. figure:: _static/connect_panel_en_2.png
   :align: center
   :alt: NextGIS Connect panel
   :width: 10cm
   
   NextGIS Connect panel

.. |button_to_qgis| image:: _static/button_to_qgis.png
   :width: 6mm

.. |button_to_wg| image:: _static/button_to_wg.png
   :width: 6mm

.. |button_newfolder| image:: _static/button_newfolder.png
   :width: 6mm

.. |button_filter| image:: _static/button_filter.png
   :width: 6mm
   :alt: funnel

.. |button_refresh| image:: _static/button_refresh.png
   :width: 6mm

.. |button_openmap| image:: _static/button_openmap.png
   :width: 6mm
   :alt: map with magnifying glass

.. |button_settings| image:: _static/button_settings.png
   :width: 6mm
   :alt: blue gear

.. |button_help| image:: _static/button_help.png
   :width: 6mm
   :alt: question mark

Buttons on the panel:

* |button_to_qgis| `Add to QGIS <https://docs.nextgis.com/docs_ngconnect/source/ngc_data_transfer.html#qgis>`_

* |button_to_wg| `Add to Web GIS <https://docs.nextgis.com/docs_ngconnect/source/ngc_data_transfer.html#ng-connect-export>`_

* |button_newfolder| `Create resource group <https://docs.nextgis.com/docs_ngconnect/source/ngc_data_transfer.html#ng-connect-res-group>`_

* |button_filter| `Search and filter resources <https://docs.nextgis.com/docs_ngconnect/source/filter.html>`_

* |button_refresh| `Refresh resource tree <https://docs.nextgis.com/docs_ngconnect/source/ngc_data_transfer.html#connect-refresh>`_

* |button_openmap| `Open Web Map in browser <https://docs.nextgis.com/docs_ngconnect/source/ngc_data_transfer.html#connect-open-webmap>`_

* |button_settings| `Plugin settings <https://docs.nextgis.com/docs_ngconnect/source/ngc_settings.html>`_

* |button_help| Help - opens this manual
 


If no connection is set at the moment, the following message will be shown:

.. figure:: _static/panel-no-connections_en.png
   :align: center
   :alt: Message if there is no connection
   :width: 10cm
   
   NextGIS Connect panel if there is no connection

If the previously used version of NextGIS Connect didn't support QGIS authentication, after the update you will need to convert all existing connections and authentication data. You can do it in the NextGIS Connect panel or in the plugin settings.

.. figure:: _static/connect_update_convert_en.png
   :align: center
   :name: connect_update_convert_pic
   :alt: NextGIS Connect panel after update
   :width: 10cm

   Message announcing the need to convert connections

.. figure:: _static/ngc_upd_convert_menu_en.png
   :align: center
   :name: ngc_upd_convert_menu_pic
   :alt: NextGIS Connect settings after update
   :width: 22cm

   Message announcing the need to convert connections in NextGIS Connect settings


.. _ng_connect_new_connection:

Create a connection
--------------------

To create a connection you need to know the address of your Web GIS.
The address for your own Web GIS can be found at
https://my.nextgis.com/webgis

.. figure:: _static/my_nextgis.png
   :align: center
   :alt: Web GIS address
   :width: 20cm
   
   Web GIS address

Click on **Settings** button in NextGIS Connect panel.

.. figure:: _static/call_settings_en.png
   :align: center
   :alt: Open settings dialog
   :width: 10cm

   Opening Settings menu

In the pop-up window press **New** and fill in the fields: 

1.	URL – address of the target Web GIS.
2.	Name – connection id, how it will be shown in the list of connections.

.. figure:: _static/create_connection_en.png
   :align: center
   :width: 24cm
   :name: create_connection_pic
   :alt: Adding new connection
   
   Adding new connection

Next, in the *Authentication* section, add a new configuration or select a previously created one (the list items consist of configuration name, user name and authentication type).

The default setting, "No Authentication" can be used if you don't need to perform actions that a Guest has no permissions for.
For instance, only the Web GIS owner and the `team members <https://docs.nextgis.com/docs_ngcom/source/create.html#team-management>`_ can create and delete resources.

To **add a new configuration**, press the button with a green plus.

The "Authentication" dialog will pop up.

.. figure:: _static/auth_config_create_en_2.png
   :align: center
   :width: 10cm
   :name: auth_config_create_pic
   :alt: Adding authentication configuration
   
   Adding authentication configuration

1. Enter *Username* and *Password* of your NextGIS ID;
2. Press **Save**.

Make sure that the correct configuration is selected. To check if the credentials are correct, press **Test Connection**. 

If guest or user chosen for authentication does not have access at least to the Main resource group of the Web GIS, an error message will appear. Select a different authentication configuration or contact the administrator of the Web GIS to get access permission.

Next press **Save** in the connection creating dialog (:numref:`create_connection_pic`). 

Click **OK**. 

The connection selected in the "Connections" dropdown menu of the Settings dialog will become active **after** the dialog is closed.


Keycloak authentication in NextGIS QGIS
----------------------------------------

Desktop app NextGIS QGIS, NextGIS Web, and NextGIS Connect which serves as a link between them handle geoinformation systems that use Keycloak authorization. 

This option is relevant for corporate users who have a Web GIS deployed `on-premise <https://nextgis.com/pricing/>`_.
