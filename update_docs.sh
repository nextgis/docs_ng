#!/bin/bash
#update documentation

git submodule foreach git pull && git pull
git add .
git commit -am 'Update submodules'
git push --recurse-submodules=on-demand

exit 0