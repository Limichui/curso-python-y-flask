from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('holaflask.html')

if __name__ == '__main__':
    app.run(debug=True)    # Renderiza el contenido HTML desde una plantilla externa