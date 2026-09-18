# NextGIS documentation root repository
Root repository for NextGIS user and developer documentation

Main repositories
=================

* [Get Started with your Web GIS](https://github.com/nextgis/docs_ngcom)
* [NextGIS Web](https://github.com/nextgis/docs_ngweb)
* [NextGIS QGIS](https://github.com/nextgis/docs_ngqgis)
* [NextGIS Mobile](https://github.com/nextgis/docs_ngmobile)
* [NextGIS Web for developers](https://github.com/nextgis/nextgisweb/tree/3/doc)
* [NextGIS Mobile for developers](https://github.com/nextgis/ngmobile_dev)
* [NextGIS QMS Server for developers](https://github.com/nextgis/quickmapservices_server/tree/master/doc)

To start generating documentation locally you need some packages be installed python > 2.7 and:

1. sudo pip install sphinx
2. sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
3. sudo apt-get install texlive-doc-ru texlive-lang-cyrillic texlive-fonts-extra
4. sudo pip install sphinxcontrib-httpdomain sphinx-bootstrap-theme
5. sudo apt-get install latexmk

You can install packages in virtual environment, so 1 and 4 must be executed in vetualenv:

1. source env/bin/activate
2. pip install sphinx
3. pip install sphinxcontrib-httpdomain sphinx-bootstrap-theme

You have to generate key for ssh git access. See: https://help.github.com/articles/generating-ssh-keys/

```
git clone --recursive git@github.com:nextgis/docs_ng.git
cd docs_ng
make html
make latexpdf
```

Update documentation
====================

Documentation automaticaly updates on docs.nextgis.com after git push or edits on Github:

## Build status

![build status](https://buildbot.nextgis.com/badges/docs_en.svg)

## Dev mode

To track changes frontend-ассетов:

```bash
npm run dev
```

If `.rst` pages and Sphinx are edited simultaneously, удобно в отдельном
it is convenient to run this in a separate terminal:

```bash
sphinx-autobuild source build
```

## Translations

```bash
pybabel compile --directory=source/locale --domain=messages
pybabel compile --directory=source/locale --domain=sphinx
```

## License

This documentaion is licensed under CC-BY-ND 3.0
