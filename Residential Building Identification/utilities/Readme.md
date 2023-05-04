## filter.py/filter.ipynb
This file contains functionalities for filtering json files based on coordinates. This code filters the features in a GeoJSON file called [name].geojson based on whether their coordinates are contained within a set of polygons contained in another GeoJSON file called [name]-ra.geojson. [name] represent a variable with the name of a state.

  ### We get [name].geojson from: https://github.com/Microsoft/USBuildingFootprints
  ### We get [name]-ra.geojson from: https://export.hotosm.org/en/v3/exports/new/select/treetag
  
  ### Steps to collect the [name]-ra.geojson data:
  
  #### 1. In the describe section, name the file in the format: [name]-ra.geojson.
  <p align="left"> 
  
  ![image](https://user-images.githubusercontent.com/98301213/218215037-5aa401b9-f3a6-43df-9b70-2237112ef270.png) 
  
  </p>
    
  #### 2.  In the format section, select GeoJson as the export format.
  <p align="left">   
  
  ![image](https://user-images.githubusercontent.com/98301213/218215074-520b4244-4b6f-4479-a25a-eab18246c0a0.png)
    
  </p> 

  #### 3. In the data section, From Land use select recidential.
  <p align="left">
  
  ![image](https://user-images.githubusercontent.com/98301213/218215125-c65b7244-15f9-430b-bd97-2fd4e491d029.png)
    
  </p> 
  
  #### 4. Select the area to export on the map. There is a size limit on the selection so I recomend using a custom selections as shown in the piture. If you cannot select a complete state at once, try doing it by parts and merging it together afterwards. The merge.ipynb notebook may be useful on that.
  <p align="left">
  
  ![image](https://user-images.githubusercontent.com/98301213/218218832-e20a3670-4d9d-4acc-993f-2c9050233a22.png)

  </p>
  
  #### 5. Finally, click on create export.
  <p align="left">
    
  ![image](https://user-images.githubusercontent.com/98301213/218215210-e5af7159-f008-4634-8a67-3be533d39368.png)
    
  </p>
