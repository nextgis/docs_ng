#!/bin/bash
#switch lang - swithc_lang.sh ru

git checkout $1

cd source/docs_formbuilder
echo "$(pwd)"
git checkout $1

cd ../docs_ngmanager
echo "$(pwd)"
git checkout $1

cd ../docs_ngmobile
echo "$(pwd)"
git checkout $1

cd ../docs_ngqgis
echo "$(pwd)"
git checkout $1

cd ../docs_ngweb
echo "$(pwd)"
git checkout $1

cd ../docs_ngcom
echo "$(pwd)"
git checkout $1

if [ -d "../docs_simplecollector" ]; then
cd ../docs_simplecollector
echo "$(pwd)"
git checkout $1
fi

if [ -d "../docs_collector" ]; then
cd ../docs_collector
echo "$(pwd)"
git checkout $1
fi

if [ -d "../docs_toolbox" ]; then
cd ../docs_toolbox
echo "$(pwd)"
git checkout $1
fi

if [ -d "../docs_forestinspector" ]; then
cd ../docs_forestinspector
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_formbuilder_dev" ]; then
cd ../docs_formbuilder_dev
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_howto" ]; then
cd ../docs_howto
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_ngbio" ]; then
cd ../docs_ngbio
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_ngcourses" ]; then
cd ../docs_ngcourses
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_ngweb_dev" ]; then
cd ../docs_ngweb_dev
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_ogportal" ]; then
cd ../docs_ogportal
echo "$(pwd)"
git checkout master
fi

if [ -d "../ngmobile_dev" ]; then
  cd ../ngmobile_dev
  echo "$(pwd)"
  if [ -d "ios_maplib_src" ]; then
    cd ios_maplib_src
    echo "$(pwd)"
    git checkout master
    cd ..
  fi
  if [ -d "maplib_src" ]; then
    cd maplib_src
    echo "$(pwd)"
    git checkout master
    cd ..
  fi
fi

if [ -d "../qms_srv_dev" ]; then
cd ../qms_srv_dev
echo "$(pwd)"
git checkout master
fi

if [ -d "../docs_ngwdocker" ]; then
cd ../docs_ngwdocker
echo "$(pwd)"
git checkout master
fi

cd ../../
echo "$(pwd)"
git checkout $1

exit 0
