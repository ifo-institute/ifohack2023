## An interesting open source/open data workshop run by
- Oana Garbasevschi
- Manuel Köberl

### The challenge

It is estimated that in 2020 45% of Germans lived in owned residences, marking the second lowest share of homeowners of all OECD countries.  At the same time, old-age poverty is predicted to be on the rise in Germany due to increasing housing costs, and will affect particularly vulnerable populations like tenants, homeowners with mortgages, single-person households and people with migration background. Population with migration background or low incomes are also more likely to suffer the consequences of environmental hazards and pollution. At the other end of the spectrum, accumulation of wealth is one of the less well-perceived drivers of inequalities in the country, with one of the most important forms of wealth for most households being wealth in real estate. This spatial ifoHack challenge aims to investigate the relationship between land prices and spatial factors that characterize living environments, in large and diverse cities in Germany, like Berlin, Bremen, Dresden, Frankfurt am Main and Köln. By exploring information extracted from satellite images and other relevant spatial datasets, we aim to guide participants into exploring non-conventional data sources, to answer relevant economic questions related to housing markets and spatial inequalities. Are land prices positively associated with a greater availability of spatial determinants of well-being, such as green and open spaces, or walkable and bicycle paths? Is proximity to amenities, educational, leisure or work opportunities a factor that drives higher land prices? Is there a spatial segregation effect in terms of land prices and specific population subgroups? These are only some of the questions we aim to explore together at the ifoHack. By getting to know the right spatial data and methods, formulating new ideas that fit your specific research interests will be only one short step away.
 
### Data

#### Economic (land prices)

BORIS-D (Standard land value information system for Germany) is a joint project of several federal state, with the aim of providing standardized, web-based and easily accessible land values from the expert committees for land values to the general public across all federal states. 

 - Sources [Boris-D](https://www.bodenrichtwerte-boris.de/boris-d/?lang=en); [Boris-D for NRW](https://open.nrw/dataset/ce127d47-27d1-4f49-a4dc-65cc1dac339e).
 - Variable description:  In BORIS-D land prices are given per area, which can be smaller than districts; for each district all areal land prices are averaged; the number and type of areas that were aggregated in each districts is also made available, as separate variables.
	   
|  	 id| Variable 			| Description 												|  
|------|--------------------|-----------------------------------------------------------| 
|     1| Neighborhood_FID	| District identifier 										|  
|     2| Land_Value			| Aggregated land value in euros/m<sup>2</sup>				|  
|     3| Area_Types			| The types of areas for which land prices are aggregated	|  
|     4| Area_Count			| The number of areas for which land prices are aggregated	|  
|     5| City_Name			| City name 												|  

 - Variable description (address points):  

|  	 id| Variable 	| Description 												|  
|------|------------|-----------------------------------------------------------| 
|     1| Address_ID	| Address identifier 										|  
|     2| Address	| Address identifier 										| 
|     3| Land_Value	| Aggregated land value in euros/m<sup>2</sup>				|  
|     4| Area_Type1	| The types of areas for which land prices are aggregated	|  
|     5| Area_Type2	| The number of areas for which land prices are aggregated	|  
|     6| Area_ID	| The number of areas for which land prices are aggregated	|
|     7| City_Name	| City name 												|	   

#### Sociodemographic

The 2011 Census is the national population and housing statistical report, a collection of 190 variables describing population, households, and residence characteristics; data from the census is available at national and municipal levels and also in grids of 1km x 1km and 100m x 100m resolutions.   

 - Source [Destatis](https://www.zensus2011.de/DE/Home/Aktuelles/DemografischeGrunddaten.html?nn=559100)
 - Variables description: Census spatial information.

|  	 id| Variable 	| Description			|  
|------|------------|-----------------------| 
|     1| Grid_Code	| Grid cell identifier	|  
|     2| City_Code	| City AGS code			|  

 - Variables description: Census socio-demographic information.

|  	 id| Variable 				| Description																							|  
|------|------------------------|-------------------------------------------------------------------------------------------------------| 
|     1| Grid_Code				| Grid cell identifier																					|  
|     2| population_total_units	| Total population (or households/families/buildings) count in the grid cell							|
|     2| subgroup_units			| Sub-group population count (e.g. young/old population, new/old buildings, small/big households etc.	| 

#### Spatial

1. Administrative units
	
 - Sources: Open data portals of [Berlin](https://daten.odis-berlin.de/de/dataset/ortsteile/), [Bremen](https://geoportal.bremen.de/geoportal/#), [Dresden](https://www.geodaten.sachsen.de/downloadbereich-ortsteile-4346.html), [Frankfurt am Main](https://opendata-esri-de.opendata.arcgis.com/datasets/ca64da7abad04c0eb8717ca3ec486cae_0/explore?location=50.145640%2C8.698681%2C10.97), [Köln](https://www.offenedaten-koeln.de/dataset/stadtteile-k%C3%B6ln).
 - Variables 

|  	 id| Variable 			| Description				|  
|------|--------------------|---------------------------| 
|     1| Neighborhood_FID	| Neighborhood identifier	|  
|     2| Neighborhood_Code	| Neighborhood AGS code		|  
|     3| Neighborhood_Name	| Neighborhood name			|  
|     4| District_Code		| District AGS code			|  
|     5| District_Name		| District name				| 
|     5| City_Code			| City AGS code				|
|     5| City_Name			| City name					| 

2. Buildings
	
EUBUCCO is a scientific database of individual building footprints for more than 200 million buildings across the 27 European Union countries and Switzerland, together with three main attributes – building type, height and construction year. 
	
 - Source: [EUBUCCO project](https://eubucco.com/); [EUBUCCO GitHub](https://github.com/ai4up/eubucco).
 - Variables 
	   
|  	 id| Variable 			| Description 						| Note 								|
|------|--------------------|-----------------------------------|-----------------------------------|
|     1| Build_ID			| Building identifier				| Unique shape identifier 			|
|     2| Building_TypeGen	| Building type (general)			| "residential", "non-residential"	|
|     3| Building_Type		| Building type 					| "house", "library" 				|
|     4| Building_Height	| Building height 					| Available case-per-case 			|
|     5| Building_Age		| Building age 						| Available case-per-case 			|
|     6| Neighborhood_FID	| District identifier 				| The same in all district files	|
|     7| Neighborhood_Name	| District name 					|									|
|     8| City_Name			| City name 						|									|
		
3. Points of interest (POI)
	
 - Sources: [OSM data](https://download.geofabrik.de/europe/germany.html); [OSMnx](https://github.com/gboeing/osmnx).
	
4. Streets and paths

 - Sources: [OSM data](https://download.geofabrik.de/europe/germany.html); [OSMnx](https://github.com/gboeing/osmnx).
	
5. Land Cover

ESA WorldCover provides global land cover data, at 10m resolution, for 11 classes, including trees, shrubland, cropland, water bodies, and built-up surfaces. 
	
 - Source: [ESA WorldCover](https://esa-worldcover.org/en). 
  
6. Urban heat islands
	
The Global Surface UHI Explorer monitors  urban heat islands intensity, which is the positive temperature difference between an urban area and its hinterland. 
	
 - Source: https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_UHI_all_averaged_v4 
	


#### Other
 
Sustainability indicatory, multi-temporal database of indicators, INKAR; Open data portal of NRW.  

### Tools

#### QGIS
#### Python 

1. Vector data processing 

For examples of applying segregation methods, see [Segregation](https://github.com/pysal/segregation).
 
2. Raster data processing
	
3. Visualisation
 
For plotting interactively results and maps, we provide examples using [Bokeh](https://bokeh.org/). In the notebook tutorials, examples using [folium](https://github.com/python-visualization/folium) are also available. 

### Tutorials

Examples of the use of the most common Python libraries can be found in the Jupyter notebook [Vector Geodata - Quickstart](notebooks/Vector_Geodata_Quickstart.ipynb).

The Python and R geospatial community is both active and driven to publish open data, methods and learning materials. For further information on methods of geospatial anaylsis, participants can consult the following tutorials:
- [Geographic Data Science Book](https://geographicdata.science/book/intro.html)	   