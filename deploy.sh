#!/bin/bash

# Deployment script for recuperacion app

echo "Starting deployment process..."

# Pull the latest image
echo "Pulling latest Docker image..."
docker pull ghcr.io/andrespuglla5655/recuperacion:puglla

# Stop and remove existing container
echo "Stopping existing container..."
docker stop recuperacion_app || true
docker rm recuperacion_app || true

# Start new container
echo "Starting new container..."
docker run -d --name recuperacion_app -p 80:80 ghcr.io/andrespuglla5655/recuperacion:puglla

echo "Deployment completed successfully!"