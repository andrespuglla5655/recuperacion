# Deployment Guide

This document provides detailed instructions for deploying the Recuperacion application.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [VPS Setup](#vps-setup)
3. [DNS Configuration](#dns-configuration)
4. [Deployment Methods](#deployment-methods)
   - [GitHub Actions (Recommended)](#github-actions-recommended)
   - [Docker Stack](#docker-stack)
   - [Docker Compose](#docker-compose)
   - [Manual Deployment](#manual-deployment)
5. [Monitoring and Maintenance](#monitoring-and-maintenance)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

Before deploying, ensure you have:

1. A VPS with Ubuntu 20.04 or later
2. A domain name with ability to configure DNS records
3. SSH access to your VPS
4. GitHub account with repository access

## VPS Setup

1. Copy the [vps-setup.sh](file:///C:/Users/Andres/Desktop/recuperacion/vps-setup.sh) script to your VPS:
   ```bash
   scp vps-setup.sh user@your-vps-ip:/home/user/
   ```

2. SSH into your VPS and run the setup script:
   ```bash
   chmod +x vps-setup.sh
   sudo ./vps-setup.sh
   ```

3. Reboot your VPS:
   ```bash
   sudo reboot
   ```

## DNS Configuration

1. Log in to your DNS provider's control panel
2. Create an A record pointing your subdomain (e.g., `puglla.yourdomain.com`) to your VPS IP address
3. Wait for DNS propagation (usually 5-30 minutes)

## Deployment Methods

### GitHub Actions (Recommended)

This is the preferred method as it automates the entire CI/CD pipeline.

1. Set up the following secrets in your GitHub repository:
   - `VPS_HOST`: Your VPS IP address or hostname
   - `VPS_USERNAME`: SSH username for your VPS
   - `VPS_SSH_KEY`: Private SSH key for authentication
   - `VPS_PORT`: SSH port (usually 22)

2. Push to the `puglla` branch to trigger automatic deployment:
   ```bash
   git push origin puglla
   ```

3. Monitor the deployment progress in the GitHub Actions tab

### Docker Stack

For production deployment using Docker Swarm:

1. Copy [stack.yml](file:///C:/Users/Andres/Desktop/recuperacion/stack.yml) to your VPS:
   ```bash
   scp stack.yml user@your-vps-ip:/home/user/
   ```

2. SSH into your VPS and initialize Docker Swarm:
   ```bash
   docker swarm init
   ```

3. Deploy the stack:
   ```bash
   docker stack deploy -c stack.yml recuperacion
   ```

4. Check the status:
   ```bash
   docker stack services recuperacion
   ```

### Docker Compose

1. Copy [docker-compose.prod.yml](file:///C:/Users/Andres/Desktop/recuperacion/docker-compose.prod.yml) to your VPS:
   ```bash
   scp docker-compose.prod.yml user@your-vps-ip:/home/user/
   ```

2. SSH into your VPS and deploy:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. Check the status:
   ```bash
   docker-compose -f docker-compose.prod.yml ps
   ```

### Manual Deployment

1. Copy the [deploy.sh](file:///C:/Users/Andres/Desktop/recuperacion/deploy.sh) script to your VPS:
   ```bash
   scp deploy.sh user@your-vps-ip:/home/user/
   ```

2. SSH into your VPS and make the script executable:
   ```bash
   chmod +x deploy.sh
   ```

3. Run the deployment script:
   ```bash
   ./deploy.sh
   ```

## Monitoring and Maintenance

### Check Application Status

```bash
# For Docker Compose deployment
docker-compose -f docker-compose.prod.yml ps

# For Docker Stack deployment
docker stack services recuperacion

# View logs
docker logs recuperacion_app
```

### Update Application

To update the application, simply push new changes to the `puglla` branch. The GitHub Actions workflow will automatically deploy the updates.

### Backup

Regularly backup your application data:
```bash
# If you have volumes, backup them
docker run --rm -v recuperacion_app-data:/data -v /tmp:/backup alpine tar czf /backup/backup.tar.gz -C /data .
```

## Troubleshooting

### Common Issues

1. **Application not accessible**
   - Check if the container is running: `docker ps`
   - Check container logs: `docker logs recuperacion_app`
   - Verify firewall settings: `sudo ufw status`

2. **DNS not resolving**
   - Check DNS records with: `nslookup puglla.yourdomain.com`
   - Wait for DNS propagation

3. **Deployment fails**
   - Check GitHub Actions logs in the repository's Actions tab
   - Verify VPS connectivity and SSH key permissions

4. **Docker permission denied**
   - Add your user to the docker group: `sudo usermod -aG docker $USER`
   - Log out and log back in

### Health Checks

The application includes health checks. You can manually check the health status:
```bash
curl -f http://localhost/ || echo "Application is not healthy"
```

For any other issues, check the application logs:
```bash
docker logs recuperacion_app
```