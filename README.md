# NextGIS documentation root repository
Root repository for NextGIS user and developer documentation

Main repositories
=================

* [NextGIS Web](https://github.com/nextgis/docs_ngweb)
* [Get Started with your Web GIS](https://github.com/nextgis/docs_ngcom)
* [NextGIS QGIS](https://github.com/nextgis/docs_ngqgis)
* [NextGIS Mobile](https://github.com/nextgis/docs_ngmobile)
* [NextGIS Manager](https://github.com/nextgis/docs_ngmanager)
* [NextGIS Formbuilder](https://github.com/nextgis/docs_formbuilder)
* [NextGIS Bio](https://github.com/nextgis/docs_ngbio)
* [NextGIS Opengeodata Portal](https://github.com/nextgis/docs_ogportal)
* [NextGIS Forest Inspector](https://github.com/nextgis/docs_forestinspector)
* [NextGIS Web for developers](https://github.com/nextgis/nextgisweb/tree/3/doc)
* [NextGIS Mobile for developers](https://github.com/nextgis/ngmobile_dev)
* [NextGIS QMS Server for developers](https://github.com/nextgis/quickmapservices_server/tree/master/doc)

To start generating documentation locally you need some packages be installed python > 2.7 and:

1. sudo pip install sphinx
2. sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended 
3. sudo apt-get install texlive-doc-ru texlive-lang-cyrillic texlive-fonts-extra
4. sudo pip install sphinxcontrib-httpdomain sphinx-bootstrap-theme

Еще можно устанавливать в виртуальное окружение, тогда 1 и 4 пункты надо выполнять в нем:

1. source env/bin/activate
2. pip install sphinx
3. pip install sphinxcontrib-httpdomain sphinx-bootstrap-theme

You have to generate key for ssh git access. See: https://help.github.com/articles/generating-ssh-keys/
```
git clone --recursive git@github.com:nextgis/docs_ng.git
make html
make latexpdf
```
See [wiki for future details](https://github.com/nextgis/docs_ng/wiki/%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8)

Обновление документации
=======================

Обновление документации на docs.nextgis.ru после правки конкретной странице на Github:

* Склонировать или обновить этот репозиторий ([как правильно](https://github.com/nextgis/docs_ng/wiki/%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8#%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8-%D0%BF%D1%80%D0%B8-%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B5-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81-github))
* Дождаться что сработает buildbot (проверка раз в 30 мин)

Build status
============

![build status](http://176.9.38.120/buildbot/png?builder=docs_en)

License
-------------
This documentaion is licensed under CC-BY-SA 3.0
