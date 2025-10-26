from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)   # Configuración secreta para sesiones

mensajes = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST': 
        nombre = request.form.get('nombre')  # Obtener el nombre del formulario
        nuevo_mensaje = request.form.get('nuevo_mensaje')  # Obtener el mensaje del formulario
        if nuevo_mensaje:
            mensaje_formateado = f"{nombre}: {nuevo_mensaje}" # Formatear el mensaje con el nombre
            mensajes.append(mensaje_formateado) # Agregar el mensaje a la lista
            session['nombre'] = nombre  # Guardar el nombre en la sesión
            
    return render_template('chat.html', mensajes=mensajes, nombre=session.get('nombre'))    # Renderizar la plantilla con los mensajes y el nombre

if __name__ == '__main__':
    app.run(debug=True)