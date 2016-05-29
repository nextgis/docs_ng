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
      Операционная система для смартфонов, планшетных компьютеров, электронных 
      книг, цифровых проигрывателей, наручных часов, игровых приставок, нетбуков, 
      смартбуков, очков Google, телевизоров и других устройств. В будущем 
      планируется поддержка автомобилей. Основана на ядре Linux и собственной 
      реализации виртуальной машины Java от Google. Изначально разрабатывалась 
      компанией Android Inc., которую затем купила Google. Впоследствии Google 
      инициировала создание альянса :abbr:`Open Handset Alliance (OHA)`, который 
      сейчас занимается поддержкой и дальнейшим развитием платформы. Android 
      позволяет создавать Java-приложения, управляющие устройством через разработанные 
      Google библиотеки. Android Native Development Kit позволяет портировать 
      (но не отлаживать) библиотеки и компоненты приложений, написанные на Си и 
      других языках.
      
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
      Eдинообразный локатор (определитель местонахождения) ресурса. Ранее 
      назывался Universal Resource Locator  — универсальный указатель ресурса. 
      URL служит стандартизированным способом записи адреса ресурса в сети Интернет.
        
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
   
   ПО
   программное обеспечение
     1. Все или часть программ, процедур, правил и соответствующей документации системы 
        обработки информации [ISO/IEC 2382-1:1993].
     2. Компьютерные программы, процедуры и, возможно, соответствующая документация 
        и данные, относящиеся к функционированию компьютерной системы [IEEE Std 829—2008].
     3. Программа или множество программ, используемых для управления компьютером 
        [IEEE Std 829—2008].
     4. Совокупность программ системы обработки информации и программных документов, 
        необходимых для эксплуатации этих программ [ГОСТ 19781-90].  

   Охват
   Экстент
     Координаты границ карты, обычно записываются 4 цифрами. Охват обозначает место показываемое на карте, и её масштаб. 
        
   Открытые данные
     Информация, которую кто угодно может свободно использовать и распространять. Допустимы лишь требования указывать источник данных и распространять их на тех же условиях, что и исходные. Самые важные требования к ним: 
     
     * Доступность и читаемость: данные должны быть доступны целиком не дороже разумной стоимости их воспроизведения; желательно через интернет. Формат данных должен быть удобным для чтения и изменения.
     * Повторное использование и распространение: данные должны предоставляться на условиях, которые разрешают их повторное использование и распространение, в том числе - в комбинации с другими наборами данных.
     * Всеобщее участие: каждый должен иметь возможность использовать и распространять данные. Не должно быть дискриминации областей применения, людей или групп. 
       Например, ограничение «только для некоммерческого использования», которое запрещает «коммерческое» применение, или ограничение возможных областей применения (к примеру, только в образовании), недопустимы. 
     Смотрите так же http://government.ru/open_data/, http://opendatahandbook.org/guide/ru/what-is-open-data/
       
   CSV
     Формат хранения электронной таблицы в текстовом файле. Представляет собой набор строк, где столбцы разделены запятыми или точкой с запятой. Применяется для передачи информации между програмами, если они не могут читать более сложные форматы. В CSV можно хранить и географические данные: в столбцах могут быть записаны координаты точек, или же геометрия в форматах записи WKT или WKB.
     Пример cтроки: 37.2200309,55.8320522,2001755270,Аникеевка,halt
       
   API
     Набор протоколов, инструментов и процедур, которые приложение (программа, веб-сервис) предоставляет для использования внешними программными продуктами. У веб-сервисов как правило представляет собой описание возможных запросов по протоколу HTTP
     
   QML
     Язык описания картостилей, основной для программы NextGIS QGIS. Векторные и растровые стили редактируются в ней, и сохраняются в файл с расширением qml. Внутреннее представление - xml. Картостили формата qml поддерживаются в NextGIS Web. 
