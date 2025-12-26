#!/bin/bash

# Exit on error
set -e

APP_NAME="hit-counter-api"
TAG="latest"

echo "🚀 Starting deployment for $APP_NAME..."

# 1. Build the Docker image
echo "📦 Building Docker image..."
docker build -t $APP_NAME:$TAG .

# 2. Apply Kubernetes manifests
echo "☸️  Applying Kubernetes manifests..."
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/redis.yaml
kubectl apply -f k8s/api.yaml

echo "✅ Deployment complete!"
echo "🔍 Check status with: kubectl get pods"
echo "🌐 Access the API (if using Minikube): minikube service api-service --url"

