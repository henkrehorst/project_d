# Note: before running, run install: pip install GDAL
from osgeo.osr import SpatialReference, CoordinateTransformation

# Amersfoort rd new projection system (EPSG 28992)
rd_new = SpatialReference()
rd_new.ImportFromEPSG(28992)
rd_new.SetTOWGS84(565.237, 50.0087, 465.658, -0.406857, 0.350733, -1.87035, 4.0812)

# Define wgs84 projection system (EPSG 4326)
wgs84 = SpatialReference()
wgs84.ImportFromEPSG(4326)

# Create convert
rd_to_wgs84 = CoordinateTransformation(rd_new, wgs84)

# Convert rd_new coordinate to wgs84
result = rd_to_wgs84.TransformPoint(49088, 422208)
print(result)
