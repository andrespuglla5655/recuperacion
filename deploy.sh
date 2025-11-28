#!/bin/bash

# Deployment script for recuperacion app

echo "Starting deployment process..."

# Pull the latest image
echo "Pulling latest Docker image..."
docker pull ghcr.io/andrespuglla5655/recuperacion:puglla

# Stop and remove existing containers
echo "Stopping existing containers..."
docker stop recuperacion_app || true
docker rm recuperacion_app || true

# Deploy using Docker Compose
echo "Deploying with Docker Compose..."
docker-compose -f docker-compose.prod.yml up -d

# Check the status
echo "Checking deployment status..."
docker-compose -f docker-compose.prod.yml ps

echo "Deployment completed successfully!"