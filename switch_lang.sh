#!/bin/bash
#switch lang - swithc_lang.sh ru

git checkout $1
cd source/docs_formbuilder
git checkout $1
cd ../docs_ngmanager
git checkout $1
cd ../docs_ngmobile
git checkout $1
cd ../docs_ngqgis
git checkout $1
cd ../docs_ngweb
git checkout $1
cd ../docs_ngcom
git checkout $1
cd ../docs_simplecollector
git checkout $1
cd ../docs_collector
git checkout $1
cd ../docs_forestinspector
git checkout master
cd ../docs_formbuilder_dev
git checkout master
cd ../docs_formbuilder_dev
git checkout master
cd ../docs_howto
git checkout master
cd ../docs_ngbio
git checkout master
cd ../docs_ngcourses
git checkout master
cd ../docs_ngweb_dev
git checkout 3
cd ../docs_ogportal
git checkout master
cd ../ngmobile_dev/ios_maplib_src
git checkout master
cd ../../ngmobile_dev/maplib_src
git checkout master
cd ../qms_srv_dev
git checkout master
cd ../../

exit 0
