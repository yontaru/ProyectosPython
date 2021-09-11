from flask import Flask, render_template
app = Flask(__name__)

# endpoint o rutas

@app.route('/')
def index():

    vehiculos = ['Mazda', 'Chevrolet', 'Renault','Audi']
    datosindex = {
        'titulo':'Sistema de Prueba',
        'subtitulo':'Bienvenido al sistema usuario: ',
        'vehiculos':vehiculos,
        'usuario':'usuarioprueba',
        'referencia':['2','Aveo','Logan','S power']
    }
    return render_template('index.html',data=datosindex)

if __name__ == "__main__":
    app.run(debug=True,port=3200)