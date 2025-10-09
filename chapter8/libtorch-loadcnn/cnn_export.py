import torch 
import torch.nn as nn 

class CNNNet(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(3, 16, 3, 1)
    self.conv2 = nn.Conv2d(16, 32, 3, 1)
    self.fc1 = nn.Linear(32*220*220, 2)
  
  def forward(self, x):
    x = torch.relu(self.conv1(x))
    x = torch.relu(self.conv2(x))
    x = torch.flatten(x, 1)
    x = self.fc1(x)
    return x 
  
if __name__ == "__main__":
  cnn_model = CNNNet()
  cnn_model.eval()
  example_input = torch.rand([1,3,224,224])
  traced = torch.jit.trace(cnn_model, example_input)
  traced.save("cnnnet.pt")
  print("Saved cnnnet.pt")
