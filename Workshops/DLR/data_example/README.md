## Data

The data will be provided to the teams chosing this challenge, at the start of the hackaton. All data comes from open data sources.

### Economic

Land prices for individual parcel areas have been collected from BORIS-D (Standard land value information system for Germany), a joint project of several federal state, with the aim of providing standardized, web-based and easily accessible land values from the expert committees for land values to the general public across all federal states. 

 - Sources: [Boris-D](https://www.bodenrichtwerte-boris.de/boris-d/?lang=en); [Boris-D for NRW](https://open.nrw/dataset/ce127d47-27d1-4f49-a4dc-65cc1dac339e).
 - Variables:  In BORIS-D land prices are given per area, which can be smaller than a neighborhood; for each neighborhoods all areal land prices are averaged; the number and type of areas that were aggregated in each neighborhood is also made available, as separate variables.
	   
|  	 id| Variable 			| Description 												|  
|------|--------------------|-----------------------------------------------------------| 
|     1| Neighborhood_FID	| Neighborhood identifier 										|  
|     2| Land_Value			| Aggregated land price in euros/m<sup>2</sup>				|  
|     3| Area_Types			| The types of areas for which land prices are aggregated	|  
|     4| Area_Count			| The number of areas for which land prices are aggregated	|  
|     5| City_Name			| City name 												|  

 - Variables (address points):  In the example data folder, we provide a small example of residential land prices associated with individual address points. For those interested, it could be an exercise to aggregate this information in a different manner than averaging per neighborhood.

|  	 id| Variable 	| Description 												|  
|------|------------|-----------------------------------------------------------| 
|     1| Address_ID	| Address identifier 										|  
|     2| Address	| Complete address  										| 
|     3| Land_Value	| Residential land value in euros/m<sup>2</sup>				|  
|     4| Area_Type1	| Area classification	|  
|     5| Area_Type2	| Area classification	|  
|     6| Area_ID	| Identifier of the area for which a land price is available	|
|     7| City_Name	| City name 												|	   

### Sociodemographic

The 2011 Census is the national population and housing statistical report, a collection of 190 variables describing population, households, and residence characteristics; data from the census is available at national and municipal levels and also in grids of 1km x 1km and 100m x 100m resolutions.   

 - Source: [BKG](https://gdz.bkg.bund.de/index.php/default/inspire/sonstige-inspire-themen/geographische-gitter-fur-deutschland-in-lambert-projektion-geogitter-inspire.html).
 - Variables: Census spatial data (the INSPIRE Geographical Grid System).

|  	 id| Variable 	| Description			|  
|------|------------|-----------------------| 
|     1| Grid_Code	| Grid cell identifier	|  
|     2| City_Code	| City AGS code			|  

 - Source: [Destatis](https://www.zensus2011.de/DE/Home/Aktuelles/DemografischeGrunddaten.html?nn=559100).
 - Variables: The original variable description and the mapping between original variable names and short variable names are available [here](Zensus_Data_Description_and_Variable_Naming.7z).

|  	 id| Variable 				| Description																							|  
|------|------------------------|-------------------------------------------------------------------------------------------------------| 
|     1| Grid_Code				| Grid cell identifier																					|  
|     2| population_total_units	| Total population (or households/families/buildings) count in the grid cell							|
|     2| subgroup_units			| Sub-group population count (e.g. young/old population, new/old buildings, small/big households etc.)	| 

### Spatial

1. Administrative units
	
 - Sources: Open data portals of [Berlin](https://daten.odis-berlin.de/de/dataset/ortsteile/), [Bremen](https://geoportal.bremen.de/geoportal/#), [Dresden](https://www.geodaten.sachsen.de/downloadbereich-ortsteile-4346.html), [Frankfurt am Main](https://opendata-esri-de.opendata.arcgis.com/datasets/ca64da7abad04c0eb8717ca3ec486cae_0/explore?location=50.145640%2C8.698681%2C10.97), [Köln](https://www.offenedaten-koeln.de/dataset/stadtteile-k%C3%B6ln). 

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
 - Variables: The exact information associated with a POI varies depending if the data is accessed from a OSM file, or through OSMnx. For stored OSM data, the *other_tags* columns provides most information about each data feature, but the information needs further processing, since available as a single string of concatenated tags.
	
4. Streets and paths

 - Sources: [OSM data](https://download.geofabrik.de/europe/germany.html); [OSMnx](https://github.com/gboeing/osmnx).
 - Variables: The exact information associated with a street line varies depending if the data is accessed from a OSM file, or through OSMnx. For stored OSM data, the *other_tags* columns provides most information about each data feature, but the information needs further processing, since available as a single string of concatenated tags. The *highway* tag indicates the type of street. 
	
5. Land Cover

ESA WorldCover provides global land cover data, at 10m resolution, for 11 classes, including trees, shrubland, cropland, water bodies, and built-up surfaces. 
	
 - Source: [ESA WorldCover](https://esa-worldcover.org/en). 
 - Variables: The mapping between pixel values and land cover classes is provided in the [WorlCover Product User Manual](WorldCover_PUM_V2.0.pdf), page 15.

6. Sentinel-2 images

The Copernicus Sentinel-2 mission consists of two identical satellites in the same orbit. Each satellite carries a wide swath high-resolution multispectral imager with 13 spectral bands, with a spatial resolution of 10m. 

 - Source: [Copernicus Open Hub](https://scihub.copernicus.eu/).

 ### Other
  
We recommend the participants to explore other open source spatial datasets: Nighttime Lights Data, from the [Black Marble](https://blackmarble.gsfc.nasa.gov/) suite or other sources; Urban heat islands - The [Global Surface UHI Explorer](https://developers.google.com/earth-engine/datasets/catalog/YALE_YCEO_UHI_UHI_all_averaged_v4 ) monitors  urban heat islands intensity, which is the positive temperature difference between an urban area and its hinterland; The [Global Human Settlement Layer](https://ghsl.jrc.ec.europa.eu/p2022Release.php) offers a multi-temporal assessment of the presence of population and built settlements, since 1975; The [Urban Atlas](https://land.copernicus.eu/local/urban-atlas) offers detailed land cover and land use information over major European city areas; The [European Soil Database](https://esdac.jrc.ec.europa.eu/resource-type/datasets); The [European Pollutant Release and Transfer Register (E-PRTR)](https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-23/european-pollutant-release-and-transfer-register-e-prtr-data-base).

Several federal states provide good sources of interesting economic and sociodemographic data, with or without a spatial component, i.e. [NRW](https://open.nrw/suche?volltext=&groups=regi&page=1). [INKAR](https://www.inkar.de/) is an open database of sustainability indicators, at municipality and regional level.

For examples of combining social, economic and spatial information, participants can consult the datasets compiled at [Data for Good](https://dataforgood.facebook.com/dfg/tools).