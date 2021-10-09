from flask import Flask, render_template, url_for, request, redirect, flash
import user_controller

app = Flask(__name__)

#Definición de rutas

#ruta inicio
@app.route("/")
@app.route("/users")
def users():
    users = user_controller.get_user()
    return render_template("users.html", users=users)

#Ruta insertar user
@app.route("/form_add_user")
def form_add_user():
    return render_template("insert_user.html")


#Ruta editar user
@app.route("/edit_user/<int:id>")
def edit_user(id):
    user = user_controller.get_user_by_id(id)
    return render_template("edit_user.html", user=user)

@app.route("/update_user", methods=["POST"])
def update_user():
    id = request.form["id"]
    name = request.form["name"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    passwd = request.form["passwd"]
    user_controller.update_user(name, email, telefono, passwd, id)
    return redirect ("/users")

@app.route("/delete_user", methods=["POST"])
def delete_user():
    user = user_controller.delete_user(request.form["id"])
    return redirect("/users")

# Iniciar el servidor
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=4500, debug=True)
