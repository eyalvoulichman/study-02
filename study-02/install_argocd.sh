#!/bin/bash

# Exit on error
set -e

echo "🔄 Switching context to docker-desktop..."
kubectl config use-context docker-desktop

echo "🏗️ Creating argocd namespace..."
kubectl create namespace argocd || echo "Namespace argocd already exists"

echo "🚀 Installing Argo CD..."
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

echo "⏳ Waiting for Argo CD components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/argocd-server -n argocd

echo "✅ Argo CD installed successfully!"
echo "---------------------------------------------------"
echo "🔐 To get the initial admin password:"
echo "kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo"
echo ""
echo "🌐 To access the UI, run this in a separate terminal:"
echo "kubectl port-forward svc/argocd-server -n argocd 8080:443"
echo "Then visit: https://localhost:8080 (Username: admin)"
echo "---------------------------------------------------"

