#!/bin/bash

#Convert tif to png
gdal_translate -of PNG -ot Byte -scale -outsize 50% 50% $1.tif $1png.png

#Convert tif to xyz
gdal_translate -a_nodata 0 -of XYZ $1.tif $1-big.xyz -b 1

#Delete lines with null data
sed "/\-9999$/d" $1.xyz > $1.xyz

#Delete file with null data
rm $1-big.xyz