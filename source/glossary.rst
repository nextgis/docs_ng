.. _glossary:

Glossary
=========

.. glossary::
   :sorted:
            
   data
      Information represented in a way it can be processed with automatic tools with possible participation of an operator. [GOST 15971-90, article 1]
            
   information system
      1. System for storage, processing, search, distribution, 
      transfer and representation of information. [GOST 7.0-99, arcticle 3.1.30]
      2. A set of information contained in databases and tools and technologies for information processing 
      . [Federal law  "About information, 
      information technnologies and information security" 27 July 2006 N 149-FL]
   
   geographical information system
      Information system that operates with geographical data (geodata). 
      [GOST R 52438-2005 "Geographical information systems. Terms and definitions"]
   
   geodata
   geospatial data
   spatial data
      Data aboult spatial features and sets of features.
      
   geographical feature
   spatial feature
   geofeature
      Digital model for material or abstract feature of real or  
      virtual world with assigned identifier, coordinates and attributes.
      
   information support for geographic information system
      A set of knowledge about information resources, information 
      services, classificators, rules for digital description, data formats and  
      documentation, that is presented to the user or a developer of geographical information 
      system for it's creation, maintenance and usage.

   coordinate system
      A way for decription of point location relative to selected axes.

   GeoJSON
     Open standard for representation of simple geographical features 
     with their non-spatial attributes using a JavaScript Object notation.
     
   GPS
      Global positioning system
      
   GLONASS
   Global navigation satellite system
      Soviet/Russian satellite navigation system initially developed 
      for Ministry of defence of USSR. One of the two currently functioning systems 
      for global satellite navigation (Chinese satellite navigation system 
      BeiDou currently functions as regional).
   
   Android
      Operating system for smartphones, tablet computers, e-books, digital players, smart watches, game consoles, Google glasses, TVs and other devices. It plans to support vehicles. It is based on a Java virtual machine by Google. Initially developed by Android Inc. which was aquired by Google. Subsequently Google initiated the creation of :abbr:`Open Handset Alliance (OHA)`, which is now engaged in the support and further development of the platform. Android allowes to create Java applications that use libraries developed by Google to control the device. Android Native Development Kit allows to port (but not to degug) libraries and components written in C and other languages.
      
   TMS
   Tile map service
     `OSGeo <http://www.osgeo.org/>`_ standard that describes an access to representation of  
     geodata through the Internet/Intranet without an access to geodata itself. 
     
   PostGIS
     Extension for relational DBMS PostgreSQL for storage 
     of geodata in a database. PostGIS has a support for spatial 
     indexes R-Tree/GiST and geodata processing functions.
     
   ESRI Shape
   Shapefile
     Popular format for geodata files. Is developed and  
     supported by Esri company for interoperability between products of 
     Esri and other software.     
     
   GeoTIFF
     Open geodata format for raster data representation in a TIFF format with  
     matadata about georeferencing. Uses TIFF 6.0 specification, and 
     adds some types of geotags that defines a type 
     of cartographic projection, geographical coordinate system, geoid,  
     datum and all other information required for precise 
     spatial orientation of satellite image.
     
   WMS
   Web Map Service 
     A standard protocol for serving of georeferenced images through the Internet 
     that are generated on server on a basis of data from a gis database. 
     Standard was developed and initially published by international organization  
     `OGC <http://www.opengeospatial.org/>`_ (Open Geospatial Consortium 
     ) in 1999.
   
   WFS
   Web Feature Service 
     A web service that represents data in a vector GML format. 
     Client gets both attributes and geometry. Thare are standard extensions:
     
     * Transactional (WFS-T) - allows clients to send to WFS 
       server new and updated data;
     * Gazetteer (WFS-G) - a draft of a standard that adds a search and a query 
       of items by dictionary of geographical names. Initially developed by USGS;
     * Temporal - a draft of a standard that adds a temporal measurement;
     * Versioning (WFS-V, WFSV) - allows to work with different versions of data 
       (particular development of GeoServer project, not standardized by OGC). 


   Open Source
     Software with open source code. Source code of such 
     software is available for view, study and update. This allows 
     a user to participate in a process of development of open source software, 
     to use a code for creation of new software and debugging — 
     through borrowing of source code if that is allowed by license compatibility,  
     or to study of used algorithms, data structures, 
     technologies, methods and interfaces (as source code could essentially 
     complete documentation or be a kind of documentation if there is no one).

   URL
   Uniform Resource Locator
      A Uniform resource locator (description of location). Previously called Universal Resource Locator (URL). 
      URL is a standartized way to record a resource address in the Internet.
        
   QGIS
     A user-friendly geographical information system 
     with open source code, distributed under GNU General Public License. QGIS 
     is a project of Open Source Geospatial Foundation. It works on Linux, 
     Unix, Mac OSX, Windows and Android, supports for various vector, 
     raster formats, databases and has a variety of functions.
   
   Mapnik  
     Open source map renderer. Written on C++ and Python. 
     Uses a AGG library and has a function of smoothing of features with 
     high acuracy. It can read from ESRI formats, PostGIS, 
     TIFF, .osm files, and also supports for any GDAL or OGR 
     formats. 
     
   MapServer
     Server geographical information system with open source that is launched 
     through CGI interface.
   
   Software
     1. All or part of the programs, procedures, rules, and associated documentation of an information processing system [ISO/IEC 2382-1:1993].
     2. Computer programs, procedures and potentially associated documentation related to functioning of computer system [IEEE Std 829—2008].
     3. A program or a set of programs used to control a computer 
        [IEEE Std 829—2008].
     4. The collection of programs of information processing system and documentation required for the operation of these programs [GOST 19781-90].  

   Extent
     Coordinates of map borders usually written with 4 numbers. Extent identifies the place shown on the map and its scale. 
        
   Open data
     Open data is data that can be freely used, re-used and redistributed by anyone - subject only, at most, to the requirement to attribute and sharealike. Most important requirements are: 
     
     * Availability and Access: the data must be available as a whole and at no more than a reasonable reproduction cost, preferably by downloading over the internet. The data must also be available in a convenient and modifiable form.
     * Re-use and Redistribution: the data must be provided under terms that permit re-use and redistribution including the intermixing with other datasets.
     * Universal Participation: everyone must be able to use, re-use and redistribute - there should be no discrimination against fields of endeavour or against persons or groups. 
      For example, ‘non-commercial’ restrictions that would prevent ‘commercial’ use, or restrictions of use for certain purposes (e.g. only in education), are not allowed. 
     See more at http://government.ru/open_data/, http://opendatahandbook.org/guide/en/what-is-open-data/
       
   CSV
     A format for storage of tabular data in plain text.  The file contains a set of rows where columns are separated with commas or semicolons. The format is used for data exchange between programs if they can not read more complex formats. CSV could be used to store geodata: columns may store coordinates for points or geometry description in WKT or WKB formats.
     Example: 37.2200309,55.8320522,2001755270,Anikeevka,halt
       
   API
     A set of protocols, tools and procedures that an application (software or web service) provides for the use by external software. Web services API is typically a description of possible HTTP requests.
     
   QML
     A main language for description of map styles for the NextGIS QGIS software. Vector and raster styles are edited in QGIS and saved to a file with qml extension. Internal representations is xml. Map styles in qml format are supported by NextGIS Web. 
