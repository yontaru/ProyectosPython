from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key='sdf5&&'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        rol = request.form['rol']
        session['email'] = email
        session['password'] = password
        session['rol'] = rol
        return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    if session['email'] == 'xx@gmail.com' and session['password'] == '11' and session['rol'] == 'admin':
        return render_template('cart.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "main":
    app.run(debug=True, port=2300)