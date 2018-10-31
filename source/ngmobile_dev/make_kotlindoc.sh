#!/bin/bash
#generate kdoc

cd ./maplib_src/
git checkout v3
cd ..
echo "Build maplib kdoc"
kotlinsphinx --overwrite ./maplib_src/maplib/src/main/kotlin/com/nextgis ./kotlin_maplib/

exit 0
