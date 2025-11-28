from flask import Flask, render_template, request
import os
import socket
import sys

def get_system_info():
    return {
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'python_version': sys.version,
    }

app = Flask(__name__)

@app.route('/')
def home():
    system_info = get_system_info()
    # Leer versión del archivo VERSION
    try:
        with open('VERSION', 'r') as f:
            version_info = f.read().strip()
    except:
        version_info = 'Versión 4.0'
    return f"""
    <html>
        <head>
            <title>Flask App - Andres Prueba</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }}
                .container {{ background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #2c3e50; }}
                .info {{ background-color: #ecf0f1; padding: 15px; border-radius: 5px; margin: 10px 0; }}
                .version {{ color: #e74c3c; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Hola desde Flask con Traefik y CI/CD automático</h1>
                <p class="version">{version_info}</p>
                <div class="info">
                    <h3>📊 Información del Sistema:</h3>
                    <p><strong>Hostname:</strong> {system_info['hostname']}</p>
                    <p><strong>IP:</strong> {system_info['ip']}</p>
                    <p><strong>Python:</strong> {system_info['python_version']}</p>
                </div>
                <p>✅ Aplicación desplegada correctamente con GitHub Actions y Docker Swarm</p>
                <hr>
                <p><a href="/saludo/Andres">👉 Haz clic aquí para probar la ruta de saludo</a></p>
            </div>
        </body>
    </html>
    """

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"""
    <html>
        <head>
            <title>Saludo - {nombre}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #2c3e50; color: white; }}
                .container {{ background-color: #34495e; padding: 20px; border-radius: 10px; }}
                h2 {{ color: #ecf0f1; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>👋 Hola {nombre}!</h2>
                <p>Bienvenido a <strong>andres.byronrm.com</strong></p>
                <p>✅ Esta ruta confirma que el despliegue fue exitoso</p>
                <a href="/" style="color: #3498db;">← Volver al inicio</a>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "service": "andres-flask-app", "version": "4.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)