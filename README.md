# docs_ng
Full NextGIS user documentation

To start using documentation you need some programmes be installed:

1. sudo apt-get install python-sphinx 
2. sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended 
3. sudo apt-get install texlive-doc-ru texlive-lang-cyrillic texlive-fonts-extra
4. sudo pip install sphinxcontrib-httpdomain sphinx-bootstrap-theme

Than you have to generate key for ssh git access. See: https://help.github.com/articles/generating-ssh-keys/
```
git clone --recursive git@github.com:nextgis/docs_ng.git
make html
make latexpdf
```
See wiki for future details
