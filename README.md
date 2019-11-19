# Generación de series temporales de datos climáticos
Este repositorio contiene programas en el lenguaje [Python](https://www.python.org/) para la generación de series temporales de datos climáticos a partir de fuentes como:

* [Climate Hazards group Infrared Precipitation with Stations (CHIRPS)](https://www.chc.ucsb.edu/data/chirps)
* [Climatologies at High resolution for the Earth’s Land Surface Areas (CHELSA)](http://chelsa-climate.org/)
* [MERRAclim](https://datadryad.org/stash/dataset/doi:10.5061/dryad.s2v81)
* [WorldClim](http://www.worldclim.org/)

Estas fuentes contienen conjuntos de datos climáticos como precipitación, temperatura y radiación, disponibles en varias resoluciones espaciales (ej. 30", 0.5°, 2.5°) y temporales (ej. días, meses, años), y en formatos como TIFF, NetCDF, BIL o PNG.

El objetivo es generar estructuras de datos de la forma:

| id_localidad | t1  | t2  | ... | tn  |
|--------------|-----|-----|-----|-----|
| ...          | ... | ... | ... | ... |
| ...          | ... | ... | ... | ... |
| ...          | ... | ... | ... | ... |


## Descripción de los datos
### CHIRPS
CHIRPS es un conjunto de datos de precipitación que abarca las latitudes entre 50°S y 50°N (para todas las longitudes), desde 1981 hasta el presente. El algoritmo de CHIRPS integra imágenes de satélite con datos de estaciones meteorológicas para generar estimados de precipitación en intervalos de tiempo diarios, de grupos de cinco días (*pentadals*), mensuales y anuales en una resolución espacial de 0.05°.

Además de la cobertura cuasi-global (50°S - 50°N), CHIRPS ofrece subconjuntos para las regiones de África, América Central y el Caribe, y el hemisferio occidental, disponibles en varios formatos (NetCDF, TIFF, BIL, PNG).

El sitio con los datos para descargar está en:
[ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0](http://bit.ly/climate-chirps)

## Herramientas
Para ejecutar los programas, se recomienda instalar la distribución de Python incluida en la plataforma [Anaconda](https://www.anaconda.com/).

## Bibliografía
C. Vega, G., Pertierra, L. R., & Olalla-Tárraga, M. Á. (2017). MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data, 4(1), 170078. https://doi.org/10.1038/sdata.2017.78

Fick, S. E., & Hijmans, R. J. (2017). WorldClim 2: New 1-km spatial resolution climate surfaces for global land areas. International Journal of Climatology, 37(12), 4302–4315. https://doi.org/10.1002/joc.5086

Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., … Michaelsen, J. (2015). The climate hazards infrared precipitation with stations—A new environmental record for monitoring extremes. Scientific Data, 2(1), 1–21. https://doi.org/10.1038/sdata.2015.66

Karger, D. N., Conrad, O., Böhner, J., Kawohl, T., Kreft, H., Soria-Auza, R. W., … Kessler, M. (2017). Climatologies at high resolution for the earth’s land surface areas. Scientific Data, 4(1), 1–20. https://doi.org/10.1038/sdata.2017.122

## Otros recursos
[¿Cómo descargar información automatizada raster de CHIRPS haciendo uso de R? - SIG (video de Fabio Castro)](https://www.youtube.com/watch?v=V1jbSAmM940&fbclid=IwAR1dTVLgQvNSpBn_Zer8EPPIfXHoNn_Y71RfgypN5lVfF1ziSLoL3mm2iKg)

[Datos de climas: práctica en R (video de Ángela Cuervo)](https://www.youtube.com/watch?v=YZAq2yLZPF4&feature=youtu.be)

[Download and Convert CHIRPS Gridded Satellite Rainfall Data into Time Series using Python (video de GeoDelta Labs)](https://www.youtube.com/watch?v=_uaVrSeLFmA)

[Fuentes de datos de variables geoespaciales para modelos de nichos ecológicos (lista recopilada por Ángela Cuervo)](https://docs.google.com/spreadsheets/d/1SODlVcPjk2ItHokY0c5XsLegsDIy10OocHJvipHYWvg/edit?usp=sharing)

[Variables climáticas: WorldClim vs AOGCMs (video de Sara Varela)](https://www.youtube.com/watch?v=fMFrVBB0f8Y&feature=youtu.be)
