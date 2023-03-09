import os
import gc
import torch
# Pre-trained models from PyTorch -- see more at: https://pytorch.org/vision/stable/models.html
from PIL import Image
#from IPython import display
# **NOTE: uncomment line 8 to download the dataset
#from roboflow import Roboflow
from torch.nn.functional import softmax
from torchvision.models import swin_b, mobilenet_v2
from torchvision.models import Swin_B_Weights, MobileNet_V2_Weights
from torchvision.transforms.functional import to_pil_image, pil_to_tensor

# Uncomment the section below to download the dataset
# ----------------------------------------------------------------
# rf = Roboflow(api_key="t2XwTHJswUaJVebcq0RL")
# project = rf.workspace("yolov8test").project("solar_panels-piya1")
# dataset = project.version(1).download("yolov8")
# ----------------------------------------------------------------

panels = []
cnt = 0
folder_path = "./solar_panels-1/valid/images"
for filename in os.listdir(folder_path):
    if filename.endswith("jpg"): 
        if cnt < 100:
            cnt += 1
            panels.append(Image.open(folder_path + '/' +filename))
        else:
            break
print('Total images with solar panel(s): '.len(panels))

torch_panels = []
for indx, img in enumerate(panels):
    torch_panels.append(pil_to_tensor(img))

# Create an instance of the swin_transformer (base version); initialize weights to the model's default weights
sw = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT, progress=False)

# Initailze tranforms (default)
preprocess_img = MobileNet_V2_Weights.DEFAULT.transforms()

# Process images to a format that swin transformer can understand
processed_img = []
for i in torch_panels:
    processed_img.append(sw(preprocess_img(i).unsqueeze(dim=0)))

# Import classes (truth labels) from the pre-trained model
categories = MobileNet_V2_Weights.DEFAULT.meta["categories"]

# Get top 3 classification categories for each images
preds_sw = []
for i in processed_img:
    preds_sw.append([categories[idx] for idx in i.argsort()[0].numpy()][::-1][:3])

solar_cnt = 0
# Output 'Ture' or 'False' for solar panel detection
for pred in preds_sw:       # for indx, pred in enumerate(preds_sw): 
    if "solar dish" in pred:
        solar_cnt += 1           # print("Image #" + indx + ": True")  

print('Images detected with solar panel(s): ',solar_cnt)