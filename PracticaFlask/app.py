from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'BDTURISMO'

conexion = MySQL(app)

@app.route('/destinos')
def list_destinos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, nombre, costo FROM destinos ORDER BY nombre"
        cursor.execute(sql)
        companies = cursor.fetchall()
        # print(companies)
        data['mensaje'] = 'Exito'
        data['destinos'] = destinos
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

@app.route('/')
def index():

    destinos = ['Cartagena', 'Medellin', 'Bogotá']
    titulo='Agencia de Turismo El Paisa'
    datosindex = {
        'titulo': titulo,
        'Subtítulo': 'Bienvenidos: ' + titulo,
        'destinos': destinos,
        'cantdestinos': len(destinos)
    }
    return render_template('index.html',data=datosindex)

@app.route('/armatuplan')
def armatuplan():
    return render_template('armatuplan.html')

def not_found(error):
    # return render_template('not_found.html'),404
    return redirect(url_for('index'))

app.register_error_handler(404, not_found)

if __name__ == "__main__":
    app.run(debug=True,port=3200)