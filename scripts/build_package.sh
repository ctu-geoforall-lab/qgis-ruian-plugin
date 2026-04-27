#!/bin/sh

GDAL_VFR_VERSION=2.2.7

rm -rf gdal_vfr
wget https://github.com/ctu-geoforall-lab/gdal-vfr/archive/v${GDAL_VFR_VERSION}.tar.gz
tar xvzf v${GDAL_VFR_VERSION}.tar.gz
mkdir gdal_vfr
mv gdal-vfr-${GDAL_VFR_VERSION}/vfr4ogr gdal-vfr-${GDAL_VFR_VERSION}/vfr4ogr.conf gdal_vfr/
rm v${GDAL_VFR_VERSION}.tar.gz gdal-vfr-${GDAL_VFR_VERSION}
echo 'Y' | pb_tool zip

exit 0
