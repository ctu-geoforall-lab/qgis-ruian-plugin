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
