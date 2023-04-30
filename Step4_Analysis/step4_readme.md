This file outlines the process of comparing the socio-demographic variables with the solar panel distribution.
We categorize the dataset into two categories:
  1. Solar Panel Distribution: This dataset is received from step4 (image segmentation) and is in the form of a .csv file with the first column listing the primary key for each block group (described further) and the second column listing the number of houses with solar panels. The third column lists the number of solar patches (one house might have more than one solar patches). 
  Primary key is of the form <5-digit county FIPS code>-<6-digit census tract number>-<1-digit block group number>
  
  3. Socio-demographic Dataset: Social Explorer stores multiple ACS (American Community Surveys)reports. We download the 5-year ACS reports from Social Explorer (https://www.socialexplorer.com/a9676d974c/explore). The dataset is downloaded by block group for Arkansas state. 
  This repository currently has the dataset for specific parameters for 23 different variables. This is stored in csv file XXX. The last column in this csv file has the solar panel distribution dataset appended.

  ## Step1: Download the dataset from Social Explorer
  ![Cover](figs/SE_step1.PNG)
  


