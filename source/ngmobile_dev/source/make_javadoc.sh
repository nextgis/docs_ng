#!/bin/bash
#generate javadoc

cd ./maplib_src/
git checkout master
cd ..
echo "Build maplib javadoc"
javasphinx-apidoc -f -v -o ./maplib/ ./maplib_src/
echo "Build maplibui javadoc"
javasphinx-apidoc -f -v -o ./maplibui/ ./maplibui_src/

exit 0
