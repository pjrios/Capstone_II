# Solar Panel Classification & Segmentation Pipeline
Given the residential building dataset, a binary classification task was performed to determine the presence of solar panels to reduce the complexity of the following segmentation task by using only images with solar panels as the input. The solar panel segmentation model processes the filtered images by counties to segment the section of images with solar panels.

## Environment Specifications
### Minimum Device Support
(GPU requirement here)

### Required Packages
Please refer to `requirements.txt`

## Data Preparation
The dataset for training classification and segmentation models are located in `Capstone_II/Classification + Segmentation/data`. The dataset consists of a training set and a validation set. Each set consists of a class with residential buildings identified to have solar panels and a class with residential buildings without solar panels. The training set consists of 355 samples in each class of the training set. The validation set consists of 50 samples in each class of the validation set. In total, the [name] dataset consists of 710 and 100 samples in the training set and validation set, respectively, with an approximate 90:10 training to validation split during the training of the model. The following images are samples of training images with solar panels in the training set.

![Cover][Capstone_II/Classification + Segmentation/Auxiliary/training_solar.PNG]

## Solar Panel Classification
The file `model_comparision.ipynb` under `Capstone_II/Classification + Segmentation/Auxiliary` may be used to compare the performance of eight popular classification models for the task. The models are:
- AlexNet
- VGG
- ResNet
- DenseNet
- SqueezeNet
- Inception V3
- MobileNet
- EfficientNet

The DenseNet per-trained model is the chosen as the image classification framework. Three techniques of implementations are tested during experiments: 1) train the pre-trained model from scratch, 2) adopt feature extraction, and 3) apply fine-tuning. The graph below shows the performance of the three techniques using the DenseNet model.  

![Cover][Capstone_II/Classification + Segmentation/Auxiliary/densenet_perf.PNG]

## Solar Panel Segmentation
The YOLOv8 instance segmentation framework is adopted as the architectural backbone. (more description here) The following images show sample segmentation results.

![Cover][Capstone_II/Classification + Segmentation/Auxiliary/seg_img.PNG]
