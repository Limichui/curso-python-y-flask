from flask import Flask, render_template, request
import yt_dlp   # importar la biblioteca yt_dlp para manejar YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])    # definir la ruta principal y los métodos permitidos
def index():
    if request.method == 'POST': # si el método de la solicitud es POST
        # Obtener la URL del formulario
        url = request.form['url']   # obtener la URL del formulario

        try:
            # Opciones de descarga
            ydl_opts = {
                'outtmpl': '%(title)s.%(ext)s',  # nombre archivo = título del video
                'format': 'best'                 # mejor calidad disponible
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl: # crear una instancia de YoutubeDL con las opciones
                info = ydl.extract_info(url, download=True) # extraer información y descargar el video
                filename = ydl.prepare_filename(info)   # obtener el nombre del archivo descargado

            mensaje = f"¡Descarga completa! Video guardado como {filename}" # mensaje de éxito
            return render_template('youtube.html', mensaje=mensaje) # renderizar la plantilla con el mensaje

        except Exception as e:
            mensaje = f"Error: {e}" # mensaje de error
            return render_template('youtube.html', mensaje=mensaje) # manejar errores y mostrar mensaje de error

    return render_template('youtube.html')  # renderizar la plantilla para solicitudes GET

if __name__ == '__main__':
    app.run(debug=True)