#!/bin/bash
#generate javadoc

echo "Build maplib javadoc"
javasphinx-apidoc -f -v -o ./maplib/ ./maplib_src/
echo "Build maplibui javadoc"
javasphinx-apidoc -f -v -o ./maplibui/ ./maplibui_src/

exit 0
