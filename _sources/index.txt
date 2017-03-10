Zásuvný modul QGIS pro stahování datových vrstev RÚIAN
======================================================

Cílem projektu je vytvoření zásuvného modulu QGIS, pomocí kterého je
možné automaticky stahovat data **Registru územní identifikace, adres
a nemovitostí** (`RÚIAN <http://ruian.cz>`__) dostupných v rámci
`Veřejného dálkového přístupu <http://vdp.cuzk.cz/>`__. Grafické
uživatelské rozhraní (GUI) je navrženo tak, aby uživateli nabídlo
jednoduchý výběr požadovaných dat. Plugin je implementován v
programovacím jazyku Python s podporou knihoven `GDAL
<http://gdal.org>`_, resp. projektu GDAL-VFR
(https://github.com/ctu-geoforall-lab/gdal-vfr.git) a PyQt.

Projekt navazuje na semestrální práce předmětu `Free Software GIS
<http://geo.fsv.cvut.cz/gwiki/155YFSG>`__ vyučovaného na `Fakultě
stavební ČVUT v Praze <http://www.fsv.cvut.cz>`__ z akademického roku
2014/1015 (https://github.com/ctu-yfsg/2015-c-qgis-vfr) a 2015/2016
(https://github.com/ctu-yfsg/2016-c-qgis-vfr).

Instalace
---------

Nejprve je nutné v QGISu registrovat repositář GeoForAll ČVUT v Praze: http://geo.fsv.cvut.cz/geoforall/qgis-plugins.xml

.. image:: images/ctu-geoforall-repo-add.png
   :width: 600

.. image:: images/ctu-geoforall-repo.png
   :width: 350

.. note:: V současné době je plugin distribuován jako experimentální. V
          nastavení je tedy nutné aktivovat *Zobrazit také
          experimentální zásuvné moduly*.
          
Poté vybereme *RUIAN Plugin* a nainstalujeme jej.

.. image:: images/install.png
   :width: 600
           
Po instalaci se v nástrojové liště QGIS objeví nová ikonka:

.. image:: images/icon.png
           
Návod k použití
---------------

Vybereme obec či obce, které chceme naimportovat:

.. image:: images/select.png
   :width: 600
           
.. warning:: Je vhodné zvolit menší objem dat maximálně ve velikosti
             okresu. Zásuvný modul není navržen pro stahování většího
             objemu dat.

.. tip:: Vyhledávat lze podle názvu obce, obce s rozšířenou
   působností, okresu či kraje.
   
   .. figure:: images/select-type.png
      :width: 600

V dalším kroku zvolíme formát a cestu k výstupní souboru:

.. figure:: images/select-output.png
   :width: 600

.. note:: V současné době zásuvný modul podporuje pouze dva výstupní
          formáty:

          * `SQLite <http://gdal.org/drv_sqlite.html>`__
          * `OGC GeoPackage <http://gdal.org/drv_geopackage.html>`__

          Podpora pro další formáty, např. Esri Shapefile je ve vývoji.
          
Data můžeme v QGISu rovnou zobrazit:

.. image:: images/ruian-add.png
   :width: 400

Příklad vizualizace stažených dat:

.. image:: images/visualization.png
   :width: 1000
   
Autoři
******

* Jan Klíma
* Lukáš Středa
* Šimon Gajzler

`Laboratoř GeoForAll <http://geomatics.fsv.cvut.cz/research/geoforall/>`__ České vysoké učení technické v Praze

Supervisor: Martin Landa

Licence
^^^^^^^

Zdrojový kód (https://github.com/ctu-geoforall-lab/qgis-ruian-plugin)
je licencován pod GNU GPL 2 a vyšší.

Hlášení chyb
^^^^^^^^^^^^

Případné chyby hlašte na https://github.com/ctu-geoforall-lab/qgis-ruian-plugin/issues
