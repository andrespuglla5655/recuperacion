from flask import Flask, render_template, request, jsonify
import os
import socket
import sys

def get_system_info():
    return {
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'python_version': sys.version,
    }

# Simple rule-based chatbot responses
def get_bot_response(question):
    question = question.lower().strip()
    
    responses = {
        "hola": "¡Hola! ¿En qué puedo ayudarte?",
        "hello": "Hello! How can I help you today?",
        "¿cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
        "how are you": "I'm doing great, thank you for asking!",
        "¿qué puedes hacer?": "Puedo responder preguntas simples. ¡Pregunta lo que quieras!",
        "what can you do": "I can answer simple questions. Ask me anything!",
        "adiós": "¡Adiós! Fue un placer ayudarte.",
        "bye": "Goodbye! It was nice helping you.",
        "nombre": "Me llamo ChatBotAI, el asistente virtual de Byron.",
        "name": "My name is ChatBotAI, Byron's virtual assistant.",
        "ayuda": "Puedes preguntarme cualquier cosa y haré mi mejor esfuerzo por ayudarte.",
        "help": "You can ask me anything and I'll do my best to help you."
    }
    
    # Check for exact matches
    for key, response in responses.items():
        if key in question:
            return response
    
    # Default responses for unrecognized questions
    default_responses = [
        "Esa es una pregunta interesante. Podrías reformularla o ser más específico.",
        "No estoy seguro de entender completamente tu pregunta. ¿Podrías explicarla de otra manera?",
        "Gracias por tu pregunta. Estoy aprendiendo y mejoraré con el tiempo.",
        "That's an interesting question. Could you rephrase it or be more specific?",
        "I'm not entirely sure I understand your question. Could you explain it differently?",
        "Thank you for your question. I'm learning and will improve over time."
    ]
    
    import random
    return random.choice(default_responses)

app = Flask(__name__)

@app.route('/')
def home():
    system_info = get_system_info()
    # Read version from VERSION file
    try:
        with open('VERSION', 'r') as f:
            version_info = f.read().strip()
    except:
        version_info = 'Versión 3.0.0'
    return f"""
    <html>
        <head>
            <title>Flask App - Byron</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }}
                .container {{ background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #2c3e50; }}
                .info {{ background-color: #ecf0f1; padding: 15px; border-radius: 5px; margin: 10px 0; }}
                .version {{ color: #e74c3c; font-weight: bold; }}
                .chat-container {{ margin-top: 20px; }}
                .chat-box {{ height: 300px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; background-color: #fff; }}
                .input-container {{ display: flex; }}
                .input-container input {{ flex: 1; padding: 10px; }}
                .input-container button {{ padding: 10px 20px; background-color: #3498db; color: white; border: none; cursor: pointer; }}
                .input-container button:hover {{ background-color: #2980b9; }}
                .message {{ margin: 10px 0; }}
                .user-message {{ text-align: right; color: #2980b9; }}
                .bot-message {{ text-align: left; color: #27ae60; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Examen byron</h1>
                <p class="version">{version_info}</p>
                <div class="info">
                    <h3>📊 Información del Sistema:</h3>
                    <p><strong>Hostname:</strong> {system_info['hostname']}</p>
                    <p><strong>IP:</strong> {system_info['ip']}</p>
                    <p><strong>Python:</strong> {system_info['python_version']}</p>
                </div>
                <p>✅ Aplicación de Byron desplegada correctamente en <strong>byron.byronrm.com</strong> con GitHub Actions y Docker Swarm</p>
                
                <div class="chat-container">
                    <h3>💬 ChatBot AI</h3>
                    <div id="chat-box" class="chat-box">
                        <div class="message bot-message">¡Hola! Soy ChatBotAI. ¿En qué puedo ayudarte hoy?</div>
                    </div>
                    <div class="input-container">
                        <input type="text" id="user-input" placeholder="Escribe tu pregunta aquí..." onkeypress="handleKeyPress(event)">
                        <button onclick="sendMessage()">Enviar</button>
                    </div>
                </div>
                
                <hr>
                <p><a href="/health">🏥 Endpoint de salud</a></p>
            </div>
            
            <script>
                function sendMessage() {{
                    const input = document.getElementById('user-input');
                    const chatBox = document.getElementById('chat-box');
                    const question = input.value.trim();
                    
                    if (question === '') return;
                    
                    // Add user message to chat
                    const userMessageDiv = document.createElement('div');
                    userMessageDiv.className = 'message user-message';
                    userMessageDiv.textContent = question;
                    chatBox.appendChild(userMessageDiv);
                    
                    // Clear input
                    input.value = '';
                    
                    // Scroll to bottom
                    chatBox.scrollTop = chatBox.scrollHeight;
                    
                    // Send request to backend
                    fetch('/ask', {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/json',
                        }},
                        body: JSON.stringify({{ question: question }})
                    }})
                    .then(response => response.json())
                    .then(data => {{
                        const botMessageDiv = document.createElement('div');
                        botMessageDiv.className = 'message bot-message';
                        botMessageDiv.textContent = data.answer;
                        chatBox.appendChild(botMessageDiv);
                        
                        // Scroll to bottom
                        chatBox.scrollTop = chatBox.scrollHeight;
                    }})
                    .catch(error => {{
                        const errorMessageDiv = document.createElement('div');
                        errorMessageDiv.className = 'message bot-message';
                        errorMessageDiv.textContent = 'Lo siento, ocurrió un error. Por favor, inténtalo de nuevo.';
                        chatBox.appendChild(errorMessageDiv);
                        
                        // Scroll to bottom
                        chatBox.scrollTop = chatBox.scrollHeight;
                    }});
                }}
                
                function handleKeyPress(event) {{
                    if (event.key === 'Enter') {{
                        sendMessage();
                    }}
                }}
            </script>
        </body>
    </html>
    """

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data.get('question', '')
        
        if not question:
            return jsonify({'answer': 'Por favor, proporciona una pregunta.'}), 400
        
        # Get bot response
        answer = get_bot_response(question)
        
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'answer': 'Lo siento, ocurrió un error al procesar tu pregunta.'}), 500

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
                <p>Bienvenido a <strong>byron.byronrm.com</strong></p>
                <p>✅ Esta ruta confirma que el despliegue de la aplicación de Byron fue exitoso</p>
                <a href="/" style="color: #3498db;">← Volver al inicio</a>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "service": "byron-flask-app", "version": "3.0.0"}

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)