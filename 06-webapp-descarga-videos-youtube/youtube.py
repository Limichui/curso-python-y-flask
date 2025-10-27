from flask import Flask, render_template, request   # importar Flask y otros módulos necesarios
from pytube import YouTube  # importar la biblioteca pytube para manejar YouTube
import re # importar el módulo de expresiones regulares (aunque no se usa en este código)

app = Flask(__name__)  # crear una instancia de la aplicación Flask

@app.route('/', methods=['GET','POST'])  # definir la ruta principal y los métodos permitidos
def index():    # definir la función para manejar la ruta principal
    if request.method == 'POST':  # si el método de la solicitud es POST
        url = request.form['url'].strip()  # obtener la URL del formulario y eliminar espacios en blanco
        
        if not url:
            return render_template('youtube.html', mensaje="Por favor ingrese una URL.")
        
        try:
            video = YouTube(url)  # crear una instancia de YouTube con la URL proporcionada
            title = re.sub(r'[\\/*?:"<>|]', "", video.title)  # obtener el título del video
            stream = video.streams.get_highest_resolution()  # obtener la mejor resolución disponible del video
            stream.download(output_path='videos', filename=f"{title}.mp4")  # descargar el video
            
            mensaje = f"¡Descarga completa del video!, guardado como: {title}.mp4"    # mensaje de éxito
            return render_template('youtube.html', title=title, mensaje = mensaje)  # renderizar la plantilla con los datos del video
        
        except Exception as e:
            mensaje = f"Error al procesar la URL: {str(e)}"
            return render_template('youtube.html', mensaje = mensaje)  # manejar errores y mostrar mensaje de error
    return render_template('youtube.html')  # renderizar la plantilla para solicitudes GET


if __name__ == '__main__':  # si este archivo se ejecuta directamente
    app.run(debug=True)  # ejecutar la aplicación Flask en modo de depuración