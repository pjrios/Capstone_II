# Overview
The folder contains several notebooks for performing different tasks related to data annotation, segmentation, and classification. These tasks are organized in a sequence that starts with data annotation and progresses through segmentation and classification to ultimately enable predictions with the trained models.

<<<<<<< HEAD
### Requirements
The basis of the requirments is for our model to detect all solar panels and count them reliably. Binary classification would not suffice for reliablity, an efficient segmentation algorithm would allow us to compare the solar energy utilization by household.
Additionally, proper superposition of the land use data set vs solar panel will allow for efficient scalability.
Finally, the main focus is residential buildings. Anything outside of this category would have to be removed.
The following three paragraphs are a brief overview of what to expect in the Classification and Segmentation folder. More in-depth detail is within each folder with its respected READMEs.


=======
>>>>>>> e4ec818bceaa517910b3a7fce4b8a294d761bb4f
## Annotations
The first folder “1. Annotations” contains information to allow you to annotate binary images or other types of images. These annotations serve as the foundation for the segmentation and classification models that will be trained later.
## Training
The second folder “2. Training” is dedicated to training the classification and segmentation models. These models use the annotations generated in the previous step for training. 
## Prediction
Finally, the last folder “3. Prediction” contains notebooks to allow you to use the trained segmentation and classification models to make predictions. 





