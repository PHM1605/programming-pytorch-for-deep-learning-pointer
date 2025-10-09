import os, torch 
from flask import Flask, jsonify, request 
from PIL import Image 
from io import BytesIO 
import requests
from torchvision import transforms 
from model import load_model 

model = load_model()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
labels = ["cat", "dog"]

img_transforms = transforms.Compose([
  transforms.Resize((64,64)),
  transforms.ToTensor(),
  transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
])

app = Flask(__name__)

@app.route("/")
def status():
  return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
  data = request.get_json()
  img_url = data.get("image_url")
  # download image
  response = requests.get(img_url)
  image = Image.open(BytesIO(response.content)).convert("RGB")

  img_tensor = img_transforms(image).unsqueeze(0).to(device)
  with torch.no_grad():
    output = model(img_tensor)
    predicted_class = labels[torch.argmax(output).item()]
  return jsonify({"image":img_url, "prediction":predicted_class})

if __name__ == "__main__":
  host=os.environ.get("CATDOG_HOST", "127.0.0.1")
  port = int(os.environ.get("CATDOG_PORT", 8080))
  app.run(host=host, port=port)
