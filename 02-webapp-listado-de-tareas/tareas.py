from flask import Flask, render_template, request, redirect # Importar las librerías necesarias

app = Flask(__name__) # Crear una instancia de la aplicación Flask

tareas = ["Hacer Compras", "Lavar el Auto", "Estudiar Python", "Ir al Gimnasio"] # Lista inicial de tareas

@app.route('/') # Ruta principal para mostrar la lista de tareas
def lista_tareas():
    return render_template('tareas.html', tareas=tareas) # Ruta para mostrar la lista de tareas

@app.route('/agregar', methods=['POST']) #  Ruta para agregar una nueva tarea
def agregar_tarea():
    nueva_tarea = request.form.get('nueva_tarea') # Obtener la nueva tarea del formulario
    if nueva_tarea: # Verificar que la tarea no esté vacía
        tareas.append(nueva_tarea) # Agregar la nueva tarea a la lista
    return redirect('/') # Redirigir a la página principal para mostrar la lista actualizada

if __name__ == '__main__':  # Definir la función para agregar una nueva tarea
    app.run(debug=True)  # Ejecutar la aplicación en modo de depuración
