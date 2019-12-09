import glob
import subprocess
import os

ImageList = sorted(glob.glob('*.tiff'))

Shapefile = 'Borde_CR_Oficial_IGN_2018_wgs84.shp'

TargetRes = '0.00833333 0.00833333' # Defines the target resolution

# Create output directory
OutDir = './raster_recortados/'
if not os.path.exists(OutDir):
    os.makedirs(OutDir)

for Image in ImageList:
    print('Procesando ' + Image)

    OutImage = OutDir + Image.replace('.tiff', '_recortado.tiff') # Defines Output Image

    # Clip image
    subprocess.call('gdalwarp -of GTiff -co "COMPRESS=DEFLATE" -tr '+TargetRes+ ' -cutline ' +Shapefile+ ' -crop_to_cutline ' +Image+ ' ' +OutImage + ' -srcnodata 65535 -dstnodata 65535', shell=True)

    # Build image overviews
    subprocess.call('gdaladdo --config COMPRESS_OVERVIEW DEFLATE ' +OutImage+ ' 2 4 8 16 32 64', shell=True)

    print('Imagen procesada.' + '\n')

print('Todas las imagenes fueron procesadas.')