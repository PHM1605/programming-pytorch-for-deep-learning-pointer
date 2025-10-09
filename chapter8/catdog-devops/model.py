import os 
import torch 
from torchvision import models
import torch.nn as nn

def load_model():
  model = models.resnet50(weights=None)
  model.fc = nn.Sequential(
    nn.Linear(model.fc.in_features, 500),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(500,2)
  )
  location = os.environ["CATDOG_MODEL_LOCATION"] # 'catdog_resnet50.pth'
  state_dict = torch.load(location, map_location="cpu")
  model.load_state_dict(state_dict)
  model.eval()
  return model 

