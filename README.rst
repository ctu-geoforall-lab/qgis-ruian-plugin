QGIS plugin pro práci s daty RUIÁN
==================================

Dokumentace: https://ctu-geoforall-lab.github.io/qgis-ruian-plugin/

Postup manuální instalace
-------------------------

1. Do adresáře ``~/.qgis2/python/plugins`` naklonovat tento repositář:

::
      
   cd ~/.qgis2/python/plugins
   git clone https://github.com/ctu-geoforall-lab/qgis-ruian-plugin.git ruian_plugin

2. Do adresáře pluginu naklonovat repositář s knihovnou GDAL-VFR:

::
      
   cd ruian_plugin
   git clone https://github.com/ctu-osgeorel/gdal-vfr.git gdal_vfr
