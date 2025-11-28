# Recuperacion - ChatBot AI

Aplicación Flask con inteligencia artificial capaz de contestar preguntas mediante un contenedor Docker, con pruebas automatizadas y despliegue automático.

## Características

- ChatBot AI con capacidad de responder preguntas simples
- Interfaz web interactiva
- API REST para integración
- Pruebas automatizadas con pytest
- Contenerización con Docker
- Despliegue automático con GitHub Actions
- Compatible con Render.com para despliegue fácil

## Requisitos

- Python 3.12
- Docker (opcional)
- Cuenta en Render.com (para despliegue en la nube)

## Despliegue en Render

1. Crea una cuenta en [Render.com](https://render.com)
2. Haz fork de este repositorio o conéctalo directamente desde GitHub
3. En Render, selecciona "Web Service"
4. Conecta tu repositorio
5. Configura las siguientes opciones:
   - **Name**: recuperacion-chatbot
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
6. Haz clic en "Create Web Service"

La aplicación se desplegará automáticamente y estará disponible en una URL única proporcionada por Render.

## Despliegue con Docker Swarm

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
├── puglla.yml           # Configuración de Docker Swarm
├── render.yaml         # Configuración para Render.com
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

## Despliegue Manual con Docker

Para desplegar manualmente:

1. Construir la imagen:
   ```bash
   docker build -t recuperacion:latest .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 5000:5000 recuperacion:latest
   ```

3. La aplicación estará disponible en http://localhost:5000

## Despliegue Manual con Docker Swarm

1. Desplegar con Docker Swarm:
   ```bash
   docker stack deploy -c puglla.yml recuperacion
   ```

## Versionado

La imagen se etiqueta automáticamente con:
- `latest` - Última versión
- `puglla-1.0.5` - Versión específica requerida
- `puglla-<commit-hash>` - Versión por commit

## Acceso

La aplicación estará disponible en: http://byron.byronrm.com

## Desarrollo Local

Para ejecutar localmente:

```bash
pip install -r requirements.txt
python app.py
```

La aplicación estará disponible en http://localhost:5000