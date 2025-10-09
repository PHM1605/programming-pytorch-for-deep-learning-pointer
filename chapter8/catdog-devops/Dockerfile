FROM python:3.11-slim

ENV CATDOG_PORT=8080

ARG MODEL_PATH
ARG MODEL_NAME

ENV CATDOG_MODEL_LOCATION=/app/${MODEL_NAME}
ENV CATDOG_HOST=0.0.0.0

RUN apt-get update && apt-get install -y --no-install-recommends libglib2.0-0 libsm6 libxext6 libxrender1 \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask waitress requests \
&& pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu \
&& mkdir -p /app 

WORKDIR /app 
COPY ./model.py /app/
COPY ./catdog_server.py /app/
COPY ${MODEL_PATH}/${MODEL_NAME} /app/
COPY ./run-model-service.sh /run-model-service.sh 
RUN chmod +x /run-model-service.sh 

EXPOSE 8080
ENTRYPOINT ["/run-model-service.sh"] 

