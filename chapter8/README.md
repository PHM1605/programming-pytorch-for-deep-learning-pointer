## test /predict endpoint 
```bash
$env:CATDOG_MODEL_LOCATION = "catdog_resnet50.pth"
```
```bash
export CATDOG_MODEL_LOCATION="catdog_resnet50.pth"
```
```bash
set CATDOG_MODEL_LOCATION=catdog_resnet50.pth
```
```bash
python catdog_server.py
```
```bash
curl -X POST http://127.0.0.1:8080/predict -H "Content-Type: application/json" -d "{\"image_url\":\"https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg\"}"
```