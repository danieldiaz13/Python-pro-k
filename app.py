from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    total_usuarios = len(usuarios)
    return render_template('index.html', usuarios=usuarios, total_usuarios=total_usuarios)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        telefono = request.form['telefono']
        if nombre and documento and telefono:
            usuario = {
                'nombre': nombre,
                'documento': documento,
                'telefono': telefono
            }
            usuarios.append(usuario)
            return redirect(url_for('index'))
        else:
            error = "Por favor, completa todos los campos."
            return render_template('register.html', error=error)
    return render_template('register.html')

@app.route('/borrar/<string:nombre>', methods=['POST'])
def borrar(nombre):
    global usuarios
    # Buscar y eliminar al usuario cuyo nombre coincida
    usuarios = [usuario for usuario in usuarios if usuario['nombre'] != nombre]
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


