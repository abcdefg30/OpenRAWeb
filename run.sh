#!/bin/sh
rm -r output
pelican content -s pelicanconf.py -t ./themes/openra/
cd output
python -m pelican.server
cd ..
