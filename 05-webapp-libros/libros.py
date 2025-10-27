from flask import Flask, render_template, request, redirect, url_for # Importar Flask y otros módulos necesarios
from flask_sqlalchemy import SQLAlchemy # Importar SQLAlchemy para la base de datos

app =Flask(__name__) # Crear una instancia de Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db' # Configurar la base de datos SQLite
db = SQLAlchemy(app) # Crear una instancia de SQLAlchemy

class Libro(db.Model): # Definir el modelo de datos para los libros
    id = db.Column(db.Integer, primary_key=True) # ID del libro
    titulo = db.Column(db.String(100), nullable=False) # Título del libro
    autor = db.Column(db.String(100), nullable=False) # Autor del libro
    
with app.app_context(): # Crear el contexto de la aplicación
    db.create_all() # Crear las tablas en la base de datos 

@app.route('/') # Ruta principal
def mostrar_libros(): # Función para mostrar la lista de libros
    libros = Libro.query.all() # Obtener todos los libros de la base de datos
    return render_template('libros.html', libros=libros) # Renderizar la plantilla con la lista de libros

@app.route('/agregar_libro', methods=['POST']) # Ruta para agregar un nuevo libro
def agregar_libro(): # Función para agregar un libro
    nuevo_titulo = request.form['titulo'] # Obtener el título del formulario
    nuevo_autor = request.form['autor'] # Obtener el autor del formulario
    
    nuevo_libro = Libro(titulo=nuevo_titulo, autor=nuevo_autor) # Crear una nueva instancia de Libro
    
    db.session.add(nuevo_libro) # Agregar el nuevo libro a la sesión
    db.session.commit() # Confirmar los cambios en la base de datos
    
    return redirect(url_for('mostrar_libros')) # Redirigir a la página principal

if __name__ == '__main__': # Verificar si el script se está ejecutando directamente
    app.run(debug=True) # Ejecutar la aplicación Flask en modo de depuración