Лесис в SQLite
==============

Преобразование базы данных Лесис (ГИС TopoL-L) в формат SQLite для открытия в NextGIS QGIS.

На входе:

* Границы выделов - Слой с полигонами лесных выделов в формате ESRI Shapefile, упакованный в ZIP-архив.
* База данных Лесис - ZIP-архив с выгруженной из TopoL базой данных.

Результат работы:

* База данных SQLite cо специальной структурой атрибутов, которую можно подключать в NextGIS QGIS.

Пример поддерживаемой структуры выгрузки данных TopoL (сокращённый) ::

        │   ├── D
        │   │   ├── Connect.mdb
        │   │   ├── Gulf.mdb
        │   │   ├── Lh1.DBF
        │   │   ├── Lh1.DBT
        │   │   ├── Lh1.MDX
        │   │   ├── Lh2.DBF
        │   │   ├── Lh2.MDX
        │   │   ├── Lh3.DBF
        │   │   ├── Lh3.MDX
        │   │   ├── Lh4.DBF
        │   │   ├── Lh4.MDX
        │   │   ├── LInfo.rtf
        │   │   └── SubRF.DBF
        │   ├── Filters
        │   ├── FONTY.TXT
        │   ├── GROUPS.DBF
        │   ├── Groups_ocifrovka.dbf
        │   ├── info_L.ini
        │   ├── kv.zta
        │   ├── Les.tps
        │   ├── Linzn.txt
        │   ├── n
        │   │   ├── AdmRan.DBF
        │   │   ├── AnalVyp.dbf
        │   │   ├── Arenda.dbf
        │   │   ├── ArhForm.DBF
        │   │   ├── arnBase.DBF
        │   │   ├── arnLesse.DBF
        │   │   ├── arnLessor.dbf
        │   │   ├── arnVidPolz.DBF
        │   │   ├── BolotnRast.dbf
        │   │   ├── bonid.DBF
        │   │   ├── Bonitet.dbf
        │   │   ├── Connect.mdb
        │   │   ├── conv_DB.ini
        │   │   ├── Cz_CLP.zvf
        │   │   ├── DBDWORK.INI
        │   │   ├── digres.tps
        │   │   ├── DIGRES.ZTA
        │   │   ├── DimVys.DBF
        │   │   ├── EdIzm.DBF
        │   │   ├── Ekspoz.dbf
        │   │   ├── ErrP.DBF
        │   │   ├── ErrP.DBT
        │   │   ├── ErrP.ini
        │   │   ├── ErzSkl.DBF
        │   │   ├── estet.tps
        │   │   ├── ESTET.ZTA
        │   ├── PARAMETR.MDB
        │   ├── Plan.tps
        │   ├── SRAFY.TXT
        │   ├── STYLY.TXT
        │   ├── TopoL.bk1
        │   ├── TopoL.bk2
        │   ├── Topolflt.exp
        │   ├── TOPOLINF.EXP
        │   ├── TopoL.INI
        │   └── TrueType.INI
        ├── tree.txt
        ├── VD
        │   ├── coordsys.xml
        │   ├── Выдел.DBF
        │   ├── Выдел.SHP
        │   └── Выдел.SHX
        ├── Vd_L
        │   ├── coordsys.xml
        │   ├── Визир.DBF
        │   ├── Визир.SHP
        │   ├── Визир.SHX
        │   ├── Выдела_гр.DBF
        │   ├── Выдела_гр.SHP
        │   ├── Выдела_гр.SHX
        │   ├── Геоход_окр.DBF
        │   ├── Геоход_окр.SHP
        │   ├── Геоход_окр.SHX
        │   ├── Геох_пов_т.DBF
        │   ├── Геох_пов_т.SHP
        │   ├── Геох_пов_т.SHX
   


Запуск инструмента: https://toolbox.nextgis.com/operation/lesis2sqlite

**Попробуйте инструмент в действии, скачав наш пример:**

`Набор исходных данных <https://nextgis.ru/data/toolbox/lesis2sqlite/lesis2sqlite_inputs_ru.zip>`_ для проверки работы инструмента. Внутри архива пошаговая инструкция.

`Пример результата <https://nextgis.ru/data/toolbox/lesis2sqlite/lesis2sqlite_outputs_ru.zip>`_ работы инструмента.

