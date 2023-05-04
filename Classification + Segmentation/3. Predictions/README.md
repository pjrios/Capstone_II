# Solar Panel Classification & Segmentation Pipeline
This step employs the trained DenseNet model to perform solar panel classification with the collected residential building dataset. Following, the images identified to have solar panels are fed into the trained YOLOv8 segmentation model, which segments the region solar panel on each image and generates solar panel statistics such as:
- Number of houses with solar panels
- Number of solar panel patches
- Area of the identified solar panels
