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
cd ../../

exit 0
