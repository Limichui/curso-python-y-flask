from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  # Configuración de la clave secreta para sesiones

socketio = SocketIO(app)    # Inicializar SocketIO con la aplicación Flask

@app.route('/')
def index():
    return render_template('realtime.html')   # Renderizar la plantilla del chat

@socketio.on('mensaje')
def manejar_mensaje(data):
    nombre = data['nombre']   # Obtener el nombre del mensaje 'data'
    nuevo_mensaje = data['mensaje']  # Obtener el contenido del mensaje
    
    socketio.emit('actualizar_mensajes', {'nombre': nombre, 'mensaje': nuevo_mensaje}) # Emitir el mensaje a todos los clientes conectados
    
if __name__ == '__main__':
    socketio.run(app, debug=True)