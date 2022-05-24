.. sectionauthor:: Ekaterina Petrunenko <ekaterina.petrunenko@nextgis.com>

Настройка метаданных
=================================

Находясь в Веб ГИС в директории NextGIS Лес, можно настроить некоторые параметры отображения самого веб-приложения NextGIS Лес. Для этого в панели справа среди доступных действий выберите "Изменить".


 .. figure:: _static/admin_meta_1.png
   :name: admin_meta_1
   :align: center
   :width: 16cm

   Выбор редактирования директории "NextGIS Лес"


На странице редактирования директории перейдите во вкладку "Метаданные". 


 .. figure:: _static/admin_meta_2.png
   :name: admin_meta_2
   :align: center
   :width: 16cm

   Редактирование вкладки "Метаданные"


Здесь для любого параметра можно изменить информацию в колонке "Значения". Описания параметров и их значения по умолчанию приведены ниже:


+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+



.. list-table:: Конфигурация метаданных
   :widths: 25 25 50 50
   :header-rows: 1

   * - Ключ
     - Тип
     - Значение по умолчанию
     - Описание
   * - app
     - text
     - ngles
     - Уникальный код приложения "NextGIS Лес"
   * - title
     - text
     - NextGIS Лес
     - Заголовок приложения
   * - qmsId
     - integer
     - 465
     - QMS сервис, который будет использоваться для карт без подложек
   * - setViewDelay
     - integer
     - 500
     - Задержка загрузки тайлов при изменении положения карты (опция оптимизации). В миллисекундах
   * - lookupTableResourceGroup
     - integer
     - 
     - ID группового ресурса Веб ГИС, в котором хранятся списки алиасов полей  
   * - components.plot.enabled
     - text
     - TRUE
     - Активировать компонент 
   * - components.plot.filterFields
     - text
     - KV,YEAR_DEV,SENDER_NAM,TYPE_RUB,FARM
     - Поля фильтра на странице карты
   * - components.nep.enabled
     - text
     - TRUE
     - Активировать компонент
   * - components.nep.filterFields
     - text
     - NEP_NAME,NEP_CAT
     - Поля фильтра на странице карты
   * - components.infra.enabled
     - text
     - TRUE
     - Активировать компонент  
   * - components.infra.filterFields
     - text
     - KV,SENDER_NAM,FARM
     - Поля фильтра на странице карты
   * - components.annex3.enabled
     - text
     - TRUE
     - Активировать компонент
   * - components.annex4.enabled
     - text
     - TRUE
     - Активировать компонент
   * - components.reports.enabled
     - text
     - TRUE
     - Активировать компонент
   * - components.fires.enabled
     - text
     - TRUE
     - Активировать компонент  
   * - components.fires.viirsResource
     - integer
     - 
     - ID ресурса, в который загружаются хотспоты VIIRS 
   * - components.fires.modisResource
     - integer
     - 
     - ID ресурса, в который загружаются хотспоты MODIS
   * - resources.firewebmap
     - text
     - 
     - ID ресурса вебкарты для карты пожаров
   * - components.plot-selec.enabled
     - text
     - FALSE
     - Активировать компонент
   * - components.overview.enabled
     - text
     - TRUE
     - Активировать компонент  
   * - components.download-and-prepare-l8-s2.enabled
     - text
     - TRUE
     - Активировать компонент 
   * - components.explication2poly.enabled
     - text
     - FALSE
     - Активировать компонент 
   * - components.poly2explication.enabled
     - text
     - FALSE
     - Активировать компонент
   * - resources.space
     - text
     - nglesspace
     - keyname ресурса
   * - resources.annex3webmap
     - text
     - nglesannex3webmap
     - keyname ресурса
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4 
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
      * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
      * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4  
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     - Row 1, column 4
     
     
     
