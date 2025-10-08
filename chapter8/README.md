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

## Steps to start service
```bash
docker build --build-arg MODEL_PATH=./weights --build-arg MODEL_NAME=catdog_resnet50.pth -t catdog-service .
```
```bash
docker run -p 8080:8080 catdog-service
```

## run with environment
```bash
docker run catdog-service --env CATDOG_MODEL_LOCATION=<URL>
```

## Setup k3s deployment (free, instead of gcloud)
```bash
docker login
docker build -t phm1605/catdog-service:v1 --build-arg MODEL_PATH=weights --build-arg MODEL_NAME=catdog_resnet50.pth .
docker push phm1605/catdog-service:v1
sudo kubectl run catdog-service --image=phm1605/catdog-service:v1 --port=8080
sudo kubectl create deployment catdog-service --image=phm1605/catdog-service:v1 --port=8080
sudo kubectl delete pod catdog-service
sudo kubectl expose deployment catdog-service --type=NodePort --port 80 --target-port=8080
sudo kubectl get svc
curl -X POST http://127.0.0.1:31562/predict -H "Content-Type: application/json" -d '{"image_url":"https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg"}'
```

## Scaling k3s services
```bash
sudo kubectl scale deployment catdog-service --replicas=3
```

## Update and clean up k3s
```bash
docker build -t phm1605/catdog-service:v2 --build-arg MODEL_PATH=weights --build-arg MODEL_NAME=catdog_resnet50.pth .
docker push phm1605/catdog-service:v2
```
Tell cluster to use the new image for deployment
```bash
sudo kubectl set image deployment/catdog-service catdog-service=phm1605/catdog-service:v2
```
Cleanup
```bash
sudo kubectl delete svc catdog-service
```