# Link to the CoLab image classification file:
```sh
CoLab Notebook: https://colab.research.google.com/drive/1WB0j7tqIgsiTpH7MLx1_dIi1vlfw7thC?usp=sharing
```

# To use the local version ('model.py' & 'solar2.yml'):
```sh
1) Create a virtual environment via 'solar2.yml'
  - cd into your directory where the 'solar2.pml' is
  - Enter the command: 'conda env create -f solar2.yml'
2) Download the dataset from YOLOv8
  - Install Roboflow: 'pip install roboflow'
  - Uncomment the section of the code that downloads the data
  - (In case of package dependency errors, uncomment imports from lines 9-12. Comment line 8 out and uncomment the rest of the import once data is downloaded locally.)
** NOTE: The current code tests MobileNet. To test other pre-trained models, import the necessary pre-trained model and modify lines 38, 41, & 49. For more details about pre-trained models, please refer to https://pytorch.org/vision/main/models.html
  
```


# Pre-trained Model Performance (using 100 images):
```sh
Model             Year         Accuracy
++++++++++++++++++++++++++++++++++++++++
Swin              2021            77%
++++++++++++++++++++++++++++++++++++++++
Vision            2020            73%
Transformer
(vit_b_16)
++++++++++++++++++++++++++++++++++++++++
Vision            2020            34%
Transformer
(vit_b_32)
++++++++++++++++++++++++++++++++++++++++
MaxVit            2022            24% (?)
++++++++++++++++++++++++++++++++++++++++
Wide Resnet       2016            4% (?)
(wide_resnet50_2)
++++++++++++++++++++++++++++++++++++++++
RegNet            2020            2% (?)
(regnet_x_32gf)
++++++++++++++++++++++++++++++++++++++++
MobileNet         2017            0% (?)
++++++++++++++++++++++++++++++++++++++++
MnasNet           2019            0% (?)
```
