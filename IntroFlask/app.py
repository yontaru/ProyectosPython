from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

conexion = MySQL(app)

# endpoint o rutas

@app.route('/cars')
def list_cars():
        data = {}
        try:
                cursor = conexion.connection.cursor()
                sql = "SELECT id, marca, modelo, valor FROM car ORDER BY marca"
                cursor.execute(sql)
                companies = cursor.fetchall()
                # print(companies)
                data['mensaje'] = 'Exito'
                data['cars'] = cars
        except Exception as ex:    
                data['mensaje'] = 'Error ...'
        return jsonify(data)



@app.route('/')
def index():

    vehiculos = ['Mazda', 'Chevrolet', 'Renault','Audi']
    datosindex = {
        'titulo':'Sistema de Prueba',
        'subtitulo':'Bienvenido al sistema usuario: ',
        'vehiculos':vehiculos,
        'usuario':'usuarioprueba',
        'referencias':['2','Aveo','Logan','S power'],
        'cantvehiculos':len(vehiculos)
    }
    return render_template('index.html',data=datosindex)

@app.route('/login')
def login():
    return render_template('login.html')

def not_found(error):
    # return render_template('not_found.html'),404
    return redirect(url_for('index'))

app.register_error_handler(404, not_found)

if __name__ == "__main__":
    app.run(debug=True,port=3200)

