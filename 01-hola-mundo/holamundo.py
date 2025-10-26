from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    contenido_html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hola Mundo desde Flask</title>
        </head>
        <body>
            <h1>Hola Mundo desde Flask!!!</h1>
        </body>
        </html>'''
    return render_template_string(contenido_html)

if __name__ == '__main__':
    app.run(debug=True)    # Renderiza el contenido HTML directamente desde una cadena