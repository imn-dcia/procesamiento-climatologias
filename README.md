# Procesamiento de climatologías
Este repositorio contiene programas en el lenguaje [Python](https://www.python.org/) para el procesamiento de climatologías. Una climatología se define como un conjunto de medidas estadísticas que resumen series temporales de variables climáticas como precipitación, temperatura, radiación solar y velocidad del viento, entre otras.

Algunas climatologías cuyos datos están públicamente disponibles son:

* [Climate Hazards group Infrared Precipitation with Stations (CHIRPS)](https://www.chc.ucsb.edu/data/chirps)
* [Climatologies at High resolution for the Earth’s Land Surface Areas (CHELSA)](http://chelsa-climate.org/)
* [MERRAclim](https://datadryad.org/stash/dataset/doi:10.5061/dryad.s2v81)
* [WorldClim](http://www.worldclim.org/)
* [ERA5](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)

Estas climatologías pueden encontrarse en varias resoluciones espaciales (ej. 30", 0.5°, 2.5°) y temporales (ej. días, meses, años), en formatos raster como TIFF, NetCDF, BIL o PNG.

El objetivo de los programas desarrollados es generar estructuras de datos de la forma:

| localidad  | t1  | t2  | ... | tn  |suma |promedio |
|------------|-----|-----|-----|-----|-----|---------|
| ...        | ... | ... | ... | ... | ... |   ...   |
| ...        | ... | ... | ... | ... | ... |   ...   |
| ...        | ... | ... | ... | ... | ... |   ...   |

En donde:
* `localidad` corresponde a cada celda raster para la que se está reportando el valor de una variable climática. En este caso, se representa mediante la geometría correspondiente al punto central de la celda.
* `t1`, `t2`, ..., `tn` corresponden a los tiempos (ej. días, semanas, meses o años) en los que se está reportando el valor de la variable climática.
* `suma` es la suma de los valores de la variable climática para cada localidad.
* `promedio` es el promedio de los valores de la variable climática para cada localidad.

## Descripción de las climatologías
A manera de ejemplo, se describen con más detalle algunas de las climatologías mencionadas.

### CHIRPS
CHIRPS es un conjunto de datos de precipitación que abarca las latitudes entre 50°S y 50°N (para todas las longitudes), desde 1981 hasta el presente. El algoritmo de CHIRPS integra imágenes de satélite con datos de estaciones meteorológicas para generar estimados de precipitación en intervalos de tiempo diarios, de grupos de cinco días (*pentadals*), mensuales y anuales en una resolución espacial de 0.05°.

Además de la cobertura cuasi-global (50°S - 50°N), CHIRPS ofrece subconjuntos para las regiones de África, América Central y el Caribe, y el hemisferio occidental, disponibles en varios formatos (NetCDF, TIFF, BIL, PNG).

El sitio con los datos para descargar está en:
[ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0](http://bit.ly/climate-chirps)

### CHELSA
CHELSA es un conjunto de datos de clima de alta resolución (30 arco segundos) para zonas terrestres. Incluye patrones mensuales de temperaturas y precipitaciones medias desde el año 1979.

El sitio con los datos para descargar está en:
[http://chelsa-climate.org/downloads/](http://chelsa-climate.org/downloads/)

## Herramientas
Para ejecutar los programas, se recomienda instalar la distribución de Python incluida en la plataforma [Anaconda](https://www.anaconda.com/).

## Programas confeccionados
Se elaboraron dos programas:
* [Recorte de climatologías](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/recorte-climatologias.py): recorta los archivos raster de las climatologías con base en un archivo vectorial (ej. _shapefile_).
* [Procesamiento de climatologías](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/procesamiento-climatologias.ipynb): genera los archivos de salida con la estructura descrita en la sección introductoria.

## Ejemplos de resultados
Se procesaron los datos mensuales de precipitación de CHELSA para el período 1981-2010, con las siguientes agrupaciones:

### Acumulado de precipitación durante 1981
![Acumulado de precipitación durante 1981](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/img/CHELSA_1981_suma.png)
[Shapefile](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_1981.zip)
[Archivo CSV](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_1981.csv)

### Promedio de precipitación del mes de enero durante el período 1981-2010
![Promedio de precipitación del mes de enero durante el período 1981-2010](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/img/CHELSA_Enero_1981-2010_promedio.png)
[Shapefile](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_Enero_1981-2010_promedio.zip)
[Archivo CSV](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_Enero_1981-2010_promedio.csv)

### Promedio de precipitación del mes de junio durante el período 1981-2010
![Promedio de precipitación del mes de junio durante el período 1981-2010](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/img/CHELSA_Junio_1981-2010_promedio.png)
[Shapefile](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_Enero_1981-2010_promedio.zip)
[Archivo CSV](https://github.com/imn-dcia/procesamiento-climatologias/blob/master/resultados/CHELSA_Enero_1981-2010_promedio.csv)

## Bibliografía
Álvarez Francoso, J.I. (2016). Geovisualización de grandes volúmenes de datos ambientales. Diseño e implementación de un sistema para el acceso y la difusión de datos globales. (Tesis doctoral inédita). Universidad de Sevilla, Sevilla. Recuperado de https://idus.us.es/xmlui/handle/11441/45259

C. Vega, G., Pertierra, L. R., & Olalla-Tárraga, M. Á. (2017). MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data, 4(1), 170078. https://doi.org/10.1038/sdata.2017.78

Copernicus Climate Change Service (C3S) (2017): ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate. Copernicus Climate Change Service Climate Data Store (CDS), recuperado el 22 de noviembre de 2019. https://cds.climate.copernicus.eu/cdsapp#!/home

Fick, S. E., & Hijmans, R. J. (2017). WorldClim 2: New 1-km spatial resolution climate surfaces for global land areas. International Journal of Climatology, 37(12), 4302–4315. https://doi.org/10.1002/joc.5086

Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., … Michaelsen, J. (2015). The climate hazards infrared precipitation with stations—A new environmental record for monitoring extremes. Scientific Data, 2(1), 1–21. https://doi.org/10.1038/sdata.2015.66

Karger, D. N., Conrad, O., Böhner, J., Kawohl, T., Kreft, H., Soria-Auza, R. W., … Kessler, M. (2017). Climatologies at high resolution for the earth’s land surface areas. Scientific Data, 4(1), 1–20. https://doi.org/10.1038/sdata.2017.122

## Otros recursos
[Climatologías marítimas (video de la Agencia Espacial de Meteorología)](https://www.youtube.com/watch?v=KNdtahbiEd0)

[¿Cómo descargar información automatizada raster de CHIRPS haciendo uso de R? - SIG (video de Fabio Castro)](https://www.youtube.com/watch?v=V1jbSAmM940&fbclid=IwAR1dTVLgQvNSpBn_Zer8EPPIfXHoNn_Y71RfgypN5lVfF1ziSLoL3mm2iKg)

[Datos de climas: práctica en R (video de Ángela Cuervo)](https://www.youtube.com/watch?v=YZAq2yLZPF4&feature=youtu.be)

[Download and Convert CHIRPS Gridded Satellite Rainfall Data into Time Series using Python (video de GeoDelta Labs)](https://www.youtube.com/watch?v=_uaVrSeLFmA)

[Fuentes de datos de variables geoespaciales para modelos de nichos ecológicos (lista recopilada por Ángela Cuervo)](https://docs.google.com/spreadsheets/d/1SODlVcPjk2ItHokY0c5XsLegsDIy10OocHJvipHYWvg/edit?usp=sharing)

[Variables climáticas: WorldClim vs AOGCMs (video de Sara Varela)](https://www.youtube.com/watch?v=fMFrVBB0f8Y&feature=youtu.be)
