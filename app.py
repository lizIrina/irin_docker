from flask import Flask, jsonify, request
import os
import random
import datetime

app = Flask(__name__)

# Puerto (usa 8080 si está definido, caso contrario 80)
port = int(os.environ.get("PORT", 80))

# IA simulada — texto renovado y creado para Irina
AI_MESSAGES = [
    "Hola, soy un pequeño asistente virtual creado por Irina. Estoy lista para pensar por ti.",
    "Los sistemas CI/CD de hoy funcionan mejor cuando el café no falta… pero también cuando Irina los configura bien.",
    "Procesando tu solicitud… uhmm… parece que todo funciona perfecto en este despliegue.",
    "La versión 1.0.5 está corriendo sin fallos. Buen trabajo, Irina.",
    "¿Sabías que esta IA vive dentro de un contenedor Docker? Gracias a Irina por traerme al mundo."
]

@app.route('/')
def home():
    return '''
    <h1>Proyecto de Examen CI/CD</h1>
    <p>Aplicación Flask con IA integrada — Versión 1.0.5</p>
    <p>Endpoints:</p>
    <ul>
        <li><a href="/ai">/ai</a> → Respuesta de IA</li>
        <li><a href="/health">/health</a> → Estado del servicio</li>
        <li><a href="/info">/info</a> → Información del sistema</li>
    </ul>
    '''

@app.route('/ai')
def ai_endpoint():
    """Genera una respuesta aleatoria de la IA"""
    msg = random.choice(AI_MESSAGES)
    return jsonify({
        "response": msg,
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.5",
        "author": "Irina"
    })

@app.route('/health')
def health():
    """Indica que la aplicación está funcionando"""
    return jsonify({
        "status": "running",
        "service": "Flask AI App",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.5"
    })

@app.route('/info')
def info():
    """Información del proyecto"""
    return jsonify({
        "application": "AI Flask Service - Irina",
        "version": "1.0.5",
        "framework": "Flask 3.1.x",
        "python": "3.10",
        "deployment": "Docker + CI/CD automático",
        "author": "Irina"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
