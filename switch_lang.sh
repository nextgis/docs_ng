#!/bin/bash
#switch lang - switch_lang.sh en

git checkout $1

REPOS="docs_ngcom docs_toolbox docs_data docs_geoservices docs_ngweb docs_ngqgis docs_ngmobile docs_geoserv_prem docs_toolbox_prem docs_formbuilder docs_collector docs_ngtracker docs_ngid docs_ngconnect docs_rosreestr_tools docs_ngweb_3D ngmobile_dev qms_srv_dev docs_formbuilder_dev tracker_hub_dev docs_howto docs_ngweb_dev docs_ngwdocker"

for repo in $REPOS; do
    if [ -d "../$repo" ]; then
        cd "../$repo"
        echo "Processing $(pwd)..."
        git checkout $1
    else
        echo "Skipping $repo (directory not found)"
    fi
done

cd ../../
echo "$(pwd)"
git checkout $1

exit 0
