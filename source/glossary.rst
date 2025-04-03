.. _glossary:

Glossary
=========

.. glossary::
   :sorted:

   geographical information system
   GIS
      Information system that operates with geographical data (geodata). 

   geographical feature
   spatial feature
   geofeature
   geodata
      Digital model for material or abstract feature of real or 
      virtual world with assigned identifier, coordinates and attributes. 

   SRS
   Spacial Reference System
   CRS
   coordinate system
      A way for description of point location relative to selected axes.


   EPSG
   IOGP’s EPSG Geodetic Parameter Dataset
      Public registry of geodetic datums, spatial reference systems, Earth ellipsoids, coordinate transformations and related units of measurement, originated by a member of the European Petroleum Survey Group. Catalog is available on https://epsg.io/. Most common codes are EPSG:4326 - WGS 84, EPSG:3857 - Mercator projection.

   GPS
   Global positioning system
      One of the global navigation satellite systems that provide geolocation and time information.

   GLONASS
   Global Navigation Satellite System
      Satellite navigation system. It provides an alternative to Global Positioning System (GPS) and is the second navigational system in operation with global coverage and of comparable precision.  

   URL
   Uniform Resource Locator
      A Uniform resource locator (description of location). Previously called Universal Resource Locator (URL). URL is a standardized way to record a resource address in the Internet.

   Open Source
      Software with open source code. Source code of such software is available for view, study and update. This allows  a user to participate in a process of development of open source software, to use a code for creation of new software and debugging — through borrowing of source code if that is allowed by license compatibility, or to study of used algorithms, data structures,  technologies, methods and interfaces (as source code could essentially  complete documentation or be a kind of documentation if there is no one).

   Open data
      Open data is data that can be freely used, re-used and redistributed by anyone -  subject only, at most, to the requirement to attribute and sharealike. 

   QGIS
      A user-friendly geographical information system with open source code, distributed under GNU General Public License. QGIS is a project of Open Source Geospatial Foundation. It works on Linux, Unix, Mac OSX, Windows and Android, supports for various vector, raster formats, databases and has a variety of functions.
   
   Mapnik
      Open source map renderer. Written on C++ and Python. Uses a AGG library and has a function of smoothing of features with high acuracy. It can read from ESRI formats, PostGIS, TIFF, .osm files, and also supports for any GDAL or OGR formats. 
     
   MapServer
      Server geographical information system with open source that is launched through CGI interface.   
   
   API
      A set of protocols, tools and procedures that an application (software or web service) provides for the use by external software. Web services API is typically a description of possible HTTP requests. 
     

   CORS
   Cross-origin resource sharing
      A mechanism that allows a web page to access restricted resources from a server on a domain different than the domain that served the web page. See more in `Cross-origin resource sharing <https://en.wikipedia.org/wiki/Cross-origin_resource_sharing>`_.

   CSS
   Cascading Style Sheets
      Style sheet language used for specifying the presentation and styling of a document written in a markup language such as HTML or XML. `How to use CSS to change the look of your Web GIS <https://docs.nextgis.com/docs_ngweb/source/look.html>`_ 

   GML
   Geographic Markup Language
      XML grammar defined by the Open Geospatial Consortium (`OGC <https://www.ogc.org/standards/gml>`_) to express geographical features.   

   SDK
   software development kit
      Collection of software development tools in one installable package.

   OAuth
      (Short for open authorization) is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites but without giving them the passwords.

   SSL
   Secure Sockets Layer
      Security protocol that provides privacy, authentication, and integrity to Internet communications. 

   integer
   int
   bigint
   integral data type
      Data type that represents some range of mathematical integers. The ranges of values are: Int -  signed: between  -2147483648 and 2147483647; unsigned: between 0 and 4294967295. Bigint - signed: between -9223372036854775808 and 9223372036854775807; unsigned - between 0 and 18446744073709551615.

   HEX
      6-digit representation of the :term:`RGB` color model in the hexadecimal numeral system. The code starts with # followed by two digits representing red, two digits for green and two for blue. E.g. #f5df4d, a shade of yellow.

   HSB
   Hue, Saturation, Brightness
      A representation of RGB colors through three parameters: hue, saturation, brightness.

   RGB
      An additive color model in which the red, green, and blue primary colors of light are added together in various ways. Each color can have a value between 0 and 255. There are also :term:`HEX` color codes for HTML, CSS, SVG, and other computing applications.


   CSV
      A format for storage of tabular data in plain text.  The file contains a set of rows where columns are separated with commas or semicolons. The format is used for data exchange between programs if they can not read more complex formats. CSV could be used to store geodata: columns may store coordinates for points or geometry description in WKT or WKB formats.
     
   GeoJSON
      An open standard format designed for representing simple geographical features, along with their non-spatial attributes, based on JavaScript Object Notation.  
      The features include points, linestrings & polygons and multi-part collection of these types.      
          

   QML
      The main language for describing map styles in the NextGIS QGIS software. Vector and raster styles are edited in QGIS and saved to a file with QML extension. Internal representations is XML. Map styles in QML format are supported by NextGIS Web. 

   SLD
   Styled Layer Descriptor
      An XML schema specified by the Open Geospatial Consortium (OGC) for describing the appearance of map layers.  A typical use of SLDs is to instruct a Web Map Service (WMS) or Web Feature Service (WFS) how to render a specific layer.
   
   KML
   Keyhole Markup Language
      The file `format <https://www.ogc.org/standards/kml/>`_ used to display geographic data in an Earth browser such as Google Earth. 
      

   GeoPackage
      Open, standards-based, platform-independent, portable, self-describing, compact format for transferring geospatial information.

   PostGIS
      Extension for relational DBMS PostgreSQL for storage of geodata in a database. PostGIS has a support for spatial indexes R-Tree/GiST and geodata processing functions.

   ESRI Shape
   ESRI Shapefile
   Shapefile 
   Shape
      Popular format for geodata files developed and supported by Esri company for interoperability between products of Esri and other software.      
               
     
   GeoTIFF
      Open geodata format for raster data representation in a TIFF format with metadata about georeferencing. Uses TIFF 6.0 specification, and adds some types of geotags that defines a type of cartographic projection, geographical coordinate system, geoid, datum and all other information required for precise spatial orientation of satellite image.
     

   SVG
      Scalable Vector Graphics (SVG) is an XML-based vector image format for defining two-dimensional graphics. In GIS systems is used to store icons used as map symbols.

   XLSX
      A zipped, XML-based file format for representing spreadsheets, charts, in Office Open XML standard. Spreadsheets in this format can be used as geodata sources.

   DXF 
   AutoCAD DXF
      An open data file format developed by Autodesk to enable CAD data exchange and interoperability between AutoCAD on different computing platforms.

   MapInfo TAB
      Geospatial vector data format for geographic information systems software. It is developed and regulated by Precisely as a proprietary format. Used in MapInfo Pro.

   MapInfo MIF/MID
      Map and database exchange file format of MapInfo software product. MIF-file contains Block with the description of attributive Data-columns and Blocks that stores Geomentry Objects. MID-file is CSV-like  format to store the attributive Data. Each line in MID-file is related  with the same order Geometry Block (Geometry Object) in MIF-file. 


   WMS
   Web Map Service 
      A standard protocol for serving of georeferenced images through the Internet that are generated on server on a basis of data from a gis database. 
      The standard was developed and initially published by international organization `OGC <http://www.opengeospatial.org/>`__ (Open Geospatial Consortium) in 1999. 
     
   WFS
   Web Feature Service
   WFS-T
   WFS service
      A web service that represents data in a vector GML format. Client gets both attributes and geometry. There are standard extensions:

     * Transactional (WFS-T) - allows clients to send to WFS 
       server new and updated data;
     * Gazetteer (WFS-G) - a draft of a standard that adds a search and a query 
       of items by dictionary of geographical names. Initially developed by USGS;
     * Temporal - a draft of a standard that adds a temporal measurement;
     * Versioning (WFS-V, WFSV) - allows to work with different versions of data 
       (particular development of GeoServer project, not standardized by OGC). 

   TMS
   Tile Map Service
     `OSGeo <http://www.osgeo.org/>`__ standard that describes an access to representation of geodata through the Internet/Intranet without an access to geodata itself.   
      

   Tile 
   Tiles
      Square images displaying part of a map split by a grid, often have the size of 255 X 255 and PNG format. 
     
   OGC API Features 
   OGC API - Features
   OGC API — Features
       `OSGeo <http://www.osgeo.org/>`__ standard for publishing vector data with geometries, attributes and query filtering.

   WMTS
   Web Map Tile Service
      `OSGeo <http://www.osgeo.org/>`__ standard protocol for serving pre-rendered or run-time computed georeferenced map tiles over the Internet. 

   MVT
   Mapbox Vector Tiles
      Vector tile standard. Uses PBF container for tiles. 


   NGID
      Account on the NextGIS platform with the email address used as login.

   NGIDOP
   NextGIS ID on-premise
      Authorization and user management server for NextGIS software deployed in local networks isolated from the Internet.

   instance
      A single Web GIS with its unique URL.

   team
      A unit of user grouping in NextGIS. A Premium plan holder can share the Premium functionality with up to four other users by `adding them to the team <https://docs.nextgis.com/docs_ngcom/source/teams.html#ngcom-team-management>`_ and setting up `permissions <https://docs.nextgis.ru/docs_ngcom/source/teams.html#ngcom-auth-id-webgis>`_ for them in the Web GIS.

   LA
   label attribute
      The values of the field marked as "label attribute" are used as feature labels on the map. `How to configure <https://docs.nextgis.com/docs_ngweb/source/layers_settings.html#ngweb-admin-layers-attr>`_

   detached layer 
      Layer downloaded from Web GIS, stored locally and synchronized with the server.

   versioning
      A mechanism that tracks all changes made to the vector layer features. `Learn more <https://docs.nextgis.com/docs_ngweb/source/version.html>`_

   fid
      Field containing the unique feature ID.

   Extent 
      The coordinate of the map's boundary, usually 4 numbers. Extent identifies the area shown on the map.  
  

   resource
      A component of NextGIS Web: a layer, a map, a service etc.

   Web Map
   webmap
      Type of resource in NextGIS Web that visualizes data from various sources in a Web client.

   Vector layer
   vector_layer
      A type of geodata that stores information as a set of points, lines or polygons as well as the attribute data of the features.

   QGIS vector style 
   qgis_vector_style
      Subresource of a vector layer, necessary to display the data on a Web Map or in an app. The file extension is \*.qml. See also MapServer style. `How to create QGIS style <https://docs.nextgis.com/docs_ngweb/source/mapstyles.html#ngw-qgis-style-file>`_. 

   Resource group
   resource_group
      In NextGIS Web it's a folder/directory in the resource structure. `How to create <https://docs.nextgis.com/docs_ngweb/source/create_resource.html#ngw-resourses-group>`__

   Trackers group
   trackers_group
      In NextGIS Web it's a folder containing tracker resources. `How to create <https://docs.nextgis.ru/docs_ngcom/source/tracking.html#tracking-create>`__.

   Demo project
   demo_project
      Examples showcasing NextGIS Web functionality. `How to use Demo projects <https://docs.nextgis.com/docs_ngcom/source/demoprojects.html>`_.

   Tileset 
      File or Web GIS resource containing map data split into standardized squares. 

   Basemap
   baselayers
      Background of the map. All other layers are displayed on top of it. `How to add a basemap <https://docs.nextgis.com/docs_ngweb/source/webmaps_admin.html#ngw-map-basemaps>`_

   Collector project
   collector_project
      Type of resource in NextGIS Web, a project for data collection. Users connect to it via NextGIS Collector app to enter data in the field. `How to create <https://docs.nextgis.com/docs_ngcom/source/collector.html#collector-create-project>`__

   Raster layer
   raster_layer
      Type of resource in NextGIS Web that stores geodata as regular pixel grid. The file format is GeoTIFF. `How to create  <https://docs.nextgis.com/docs_ngweb/source/layers.html#ngw-create-raster-layer>`__

   Raster style
   raster_style
      Subresource of a raster layer necessary to display data on a Web Map.

   QGIS raster style
   qgis_raster_style
      Subresource of a raster layer necessary to display data on a Web Map or in QGIS desktop app.

   Service
   ogcfserver_service
   wmsserver_service
   wfsserver_service
      Type of resource in NextGIS Web, an interface for requesting geo-registered map images using standard protocols: OGC API – Features, WMS etc. 

   Connection
   PostGIS connection
   TMS connection
   WMS connection
   WFS connection
   postgis_connection
   tmsclient_connection
   wfsclient_connection
   wmsclient_connection
      Type of resource in NextGIS Web, a connection to a remote server using standard protocols: PostGIS, TMS, WFS, WMS.


   PostGIS layer
   postgis_layer
      Layer added using a connection to a PostGIS data base on a remote server.

   TMS layer
   tmsclient_layer
      Layer containing tiles served via TMS protocol.

   WFS Layer
   wfsclient_layer
      Layer added using WFS protocol.

   WMS layer
   wmsclient_layer
      Raster layer that displays data stored on a remote server and served via WMS protocol.

   Lookup table
   lookup_table 
      Type of resource in NextGIS Web, a list of key-value pairs that can be connected to a field of a vector layer. `How to create <https://docs.nextgis.com/docs_ngweb/source/create_other.html#ngw-create-lookup-table>`__

   MapServer style
   mapserver_style
      Subresource of a vector layer, necessary to display the data on a Web Map or in an app. See also QGIS vector style. `How to create <https://docs.nextgis.com/docs_ngweb/source/mapstyles.html#mapserver>`__

   Tracker 
      1. Type of resource in NextGIS Web that creates a connection between a tracking device and the Web GIS.
      2. Mobile app NextGIS Tracker that records tracks and sends them to Web GIS.

   Form
   formbuilder_form
      Subresource of a vector layer, a user-friendly interface for entering and editing data used in mobile apps NextGIS Mobile and NextGIS Collector. The file has \*.ngfp extension.

   File bucket
   file_bucket
      Special resource type available in Extended NextGIS on-premise. A storage for files of any kind. `How to create <https://docs.nextgis.com/docs_ngweb/source/create_other.html#ngw-create-file-bucket>`__

   SVG Marker Library
   svg_marker_library
      Type of resource in NextGIS Web that stores SVG icons used in QGIS vector styles to display data on Web Maps, if the icons are not embedded in the style. `How to create <https://docs.nextgis.com/docs_ngweb/source/mapstyles.html#ngw-create-svg-marker-lib>`__
