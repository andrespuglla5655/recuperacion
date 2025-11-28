# Recuperacion - ChatBot AI

Aplicación Flask con inteligencia artificial capaz de contestar preguntas mediante un contenedor Docker, con pruebas automatizadas y despliegue automático.

## Características

- ChatBot AI con capacidad de responder preguntas simples
- Interfaz web interactiva
- API REST para integración
- Pruebas automatizadas con pytest
- Contenerización con Docker
- Despliegue automático con GitHub Actions
- Integración con Traefik para enrutamiento
- Monitoreo de salud del servicio

## Requisitos

- Docker
- Docker Swarm (para despliegue en producción)
- Acceso a un VPS con Traefik configurado

## Despliegue

El despliegue se realiza automáticamente mediante GitHub Actions cuando se hace push a la rama `main`.

### Variables de Entorno Requeridas

Para el despliegue automático, se deben configurar las siguientes variables secretas en el repositorio:

- `VPS_HOST`: Dirección IP o hostname del VPS
- `VPS_USER`: Usuario SSH para el VPS
- `VPS_SSH_KEY`: Clave privada SSH
- `VPS_SSH_PORT`: Puerto SSH (por defecto 22)

## Estructura del Proyecto

```
.
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias de Python
├── Dockerfile          # Configuración de Docker
├── stack.yml           # Configuración de Docker Swarm
├── VERSION             # Archivo de versión
├── tests/              # Pruebas automatizadas
│   ├── __init__.py
│   └── test_app.py
└── .github/workflows/  # Workflows de GitHub Actions
    └── andrespuglla.yml
```

## Endpoints

- `GET /` - Página principal con interfaz de chat
- `POST /ask` - API para hacer preguntas al chatbot
- `GET /saludo/<nombre>` - Saludo personalizado
- `GET /health` - Estado de salud del servicio

## Pruebas

Para ejecutar las pruebas localmente:

```bash
pip install -r requirements.txt
pytest -v
```

## Despliegue Manual

Para desplegar manualmente:

1. Construir la imagen:
   ```bash
   docker build -t recuperacion:latest .
   ```

2. Desplegar con Docker Swarm:
   ```bash
   docker stack deploy -c stack.yml recuperacion
   ```

## Versionado

La imagen se etiqueta automáticamente con:
- `latest` - Última versión
- `puglla-1.0.5` - Versión específica requerida
- `puglla-<commit-hash>` - Versión por commit

## Acceso

La aplicación estará disponible en: http://puglla.byronrm.com

## Desarrollo

Para ejecutar localmente:

```bash
pip install -r requirements.txt
python app.py
```

La aplicación estará disponible en http://localhost:5000