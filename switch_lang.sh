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
if [ -d "../docs_simplecollector" ]; then
cd ../docs_simplecollector
git checkout $1
fi
if [ -d "../docs_collector" ]; then
cd ../docs_collector
git checkout $1
fi
if [ -d "../docs_forestinspector" ]; then
cd ../docs_forestinspector
git checkout master
fi
if [ -d "../docs_formbuilder_dev" ]; then
cd ../docs_formbuilder_dev
git checkout master
fi
if [ -d "../docs_howto" ]; then
cd ../docs_howto
git checkout master
fi
if [ -d "../docs_ngbio" ]; then
cd ../docs_ngbio
git checkout master
fi
if [ -d "../docs_ngcourses" ]; then
cd ../docs_ngcourses
git checkout master
fi
if [ -d "../docs_ngweb_dev" ]; then
cd ../docs_ngweb_dev
git checkout 3
fi
if [ -d "../docs_ogportal" ]; then
cd ../docs_ogportal
git checkout master
fi
if [ -d "../ngmobile_dev" ]; then
  cd ../ngmobile_dev
    if [ -d "ios_maplib_src" ]; then
      cd ios_maplib_src
      git checkout master
      cd ..
    fi
    if [ -d "/maplib_src" ]; then
      cd maplib_src
      git checkout master
      cd ..
    fi
fi
if [ -d "../qms_srv_dev" ]; then
cd ../qms_srv_dev
git checkout master
fi
cd ../../

exit 0
