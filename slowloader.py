import torch, torchvision
from torch import optim
import torch.nn as nn
from torchvision import datasets, transforms, models
import torch.utils.data
from PIL import Image 
import numpy as np 

device = "cuda" if torch.cuda.is_available() else "cpu"
model = models.resnet18(pretrained=True)
model.to(device)

#--- this is bad because we take 1 image, add noise for 1 image ---
class BadRandom(object):
  def __call__(self, img):
    img_np = np.array(img)
    random = np.random.random_sample(img_np.shape) # random (0,1) with same shape as img_np
    out_np = img_np+random
    out = Image.fromarray(out_np.astype("uint8"), "RGB")
    return out 
  def __repr__(self):
    str = f"{self.__class__.__name__}"
    return str 
train_data_path = "/media/phm1605/hddstorage1/data/test_images"
image_transforms = torchvision.transforms.Compose([
  transforms.Resize((224,224)),
  BadRandom(),
  transforms.ToTensor()
])
train_data = torchvision.datasets.ImageFolder(root=train_data_path, transform=image_transforms)
batch_size = 32
train_data_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size)
optimizer = optim.Adam(model.parameters(), lr=2e-2)
criterion = nn.CrossEntropyLoss()

def train_bad(model, optimizer, loss_fn, train_loader, val_loader, epochs=20, device="cuda"):
  model.to(device)
  for epoch in range(epochs):
    print(f"epoch {epoch}")
    model.train()
    for images, targets in train_loader:
      optimizer.zero_grad()
      images = images.to(device)
      targets = targets.to(device)
      output = model(images)
      loss = loss_fn(output, targets)
      loss.backward()
      optimizer.step()
    model.eval()
    num_correct = 0
    num_examples = 0
    for images, targets in val_loader:
      images = images.to(device)
      targets = targets.to(device)
      output = model(images)
      correct = torch.eq(torch.max(output, dim=1)[1], targets).view(-1)
      num_correct += torch.sum(correct).item()
      num_examples += correct.shape[0]
    print("Epoch {}, accuracy={:.2f}".format(epoch, num_correct/num_examples))
train(model, optimizer, criterion, train_data_loader, train_data_loader, epochs=10)
# -------------------------------------------------------------------------------------------
