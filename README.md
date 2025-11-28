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

## Deployment
The application is automatically built, tested, and deployed through GitHub Actions.

### Manual Deployment
To manually deploy to your VPS:
1. Copy the [deploy.sh](file:///C:/Users/Andres/Desktop/recuperacion/deploy.sh) script to your VPS
2. Make it executable: `chmod +x deploy.sh`
3. Run the script: `./deploy.sh`

### Using Docker Compose
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