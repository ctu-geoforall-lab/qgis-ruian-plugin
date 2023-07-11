#!/bin/sh

GDAL_VFR_VERSION=2.1.6

rm -rf gdal_vfr
wget https://github.com/ctu-geoforall-lab/gdal-vfr/archive/v${GDAL_VFR_VERSION}.tar.gz
tar xvzf v${GDAL_VFR_VERSION}.tar.gz
mv gdal-vfr-${GDAL_VFR_VERSION} gdal_vfr
rm v${GDAL_VFR_VERSION}.tar.gz
echo 'Y' | pb_tool zip

exit 0
