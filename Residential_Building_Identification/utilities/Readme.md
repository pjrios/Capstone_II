## filter.py
This file contains functionalities for filtering json files based on coordinates. This code filters the features in a GeoJSON file called [name].geojson based on whether their coordinates are contained within a set of polygons contained in another GeoJSON file called [name]-ra.geojson. [name] represent a variable with the name of a state.

  ### We get [name].geojson from: https://github.com/Microsoft/USBuildingFootprints
  ### We get [name]-ra.geojson from: https://export.hotosm.org/en/v3/exports/new/select/treetag
