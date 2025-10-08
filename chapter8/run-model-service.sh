#!/bin/bash
cd /app 
waitress-serve --listen=0.0.0.0:8080 catdog_server:app
