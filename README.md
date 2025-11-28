# Recuperacion Project

This is a Python Flask application with Docker support and CI/CD pipeline.

## Features
- Flask web application
- Docker containerization
- GitHub Actions CI/CD pipeline
- Automated testing
- Image publishing to GHCR
- Automatic deployment to VPS

## Prerequisites
- Docker installed on target VPS
- SSH access to the VPS
- GitHub repository secrets configured:
  - VPS_HOST: IP address or hostname of your VPS
  - VPS_USERNAME: SSH username for your VPS
  - VPS_SSH_KEY: Private SSH key for authentication
  - VPS_PORT: SSH port (usually 22)

## Detailed Deployment Guide

For comprehensive deployment instructions, please refer to the [DEPLOYMENT.md](file:///C:/Users/Andres/Desktop/recuperacion/DEPLOYMENT.md) file.

## Quick Start

### VPS Setup
1. Copy [vps-setup.sh](file:///C:/Users/Andres/Desktop/recuperacion/vps-setup.sh) to your VPS and run it to install Docker and Docker Compose
2. Reboot your VPS after setup
3. Configure your DNS to point your subdomain (e.g., puglla.yourdomain.com) to your VPS IP address

## Deployment Options

### 1. GitHub Actions Deployment (Recommended)
The application is automatically built, tested, and deployed through GitHub Actions when you push to the `puglla` branch.

### 2. Docker Stack Deployment
For production deployment using Docker Swarm:
1. Copy [stack.yml](file:///C:/Users/Andres/Desktop/recuperacion/stack.yml) to your VPS
2. Initialize Docker Swarm: `docker swarm init`
3. Deploy the stack: `docker stack deploy -c stack.yml recuperacion`

### 3. Manual Deployment
To manually deploy to your VPS:
1. Copy the [deploy.sh](file:///C:/Users/Andres/Desktop/recuperacion/deploy.sh) script to your VPS
2. Make it executable: `chmod +x deploy.sh`
3. Run the script: `./deploy.sh`

### 4. Using Docker Compose
You can also use Docker Compose for deployment:
1. Copy [docker-compose.prod.yml](file:///C:/Users/Andres/Desktop/recuperacion/docker-compose.prod.yml) to your VPS
2. Run: `docker-compose -f docker-compose.prod.yml up -d`

## Development
To run locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`

To run tests:
1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `pytest -v`