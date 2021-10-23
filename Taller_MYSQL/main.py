import re
from flask import Flask, render_template, url_for, request, redirect, flash
import controller

app = Flask(__name__)

@app.route("/")
@app.route("/customers")
def customers():
    customers = controller.get_customer()
    return render_template("customers.html", customers=customers)

@app.route("/invoices")
def invoices():
    invoices = controller.get_invoice()
    return render_template("invoices.html", invoices=invoices)

@app.route("/form_add_customer")
def form_add_customer():
    return render_template("insert_customer.html")

@app.route("/form_add_invoice")
def form_add_invoice():
    return render_template("insert_invoice.html")

@app.route("/edit_customer/<int:id>")
def edit_customer(id):
    customer = controller.get_customer_by_id(id)
    return render_template("edit_customer.html", customer=customer)

@app.route("/edit_invoice/<int:id>")
def edit_invoice(id):
    invoice = controller.get_invoice_by_id(id)
    return render_template("edit_invoice.html", invoice=invoice)

@app.route("/update_customer", methods=["POST"])
def update_customer():
    id = request.form["id"]
    name = request.form["name"]
    status=request.form["status"]
    mobile=request.form["mobile"]
    controller.update_customer(name, status, mobile, id)
    return redirect("/customers")

@app.route("/update_invoice", methods=["POST"])
def update_invoice():
    id=request.form["id"]
    number=request.form["number"]
    date = request.form["date"]
    price=request.form["price"]
    balance=request.form["balance"]
    controller.update_invoice(number, date, price, balance, id)
    return redirect("/invoices")

@app.route("/delete_invoice", methods=["POST"])
def delete_invoice():
    controller.delete_invoice(request.form["id"])
    return redirect("/invoices")

@app.route("/delete_customer", methods=["POST"])
def delete_customer():
    controller.delete_customer(request.form["id"])
    return redirect("/customers")

@app.route("/insert_customer", methods=["POST"])
def insert_customer():
    name=request.form["name"]
    status=request.form["status"]
    mobile=request.form["mobile"]
    controller.insert_customer(name, status, mobile)
    return redirect("/customers")

# Iniciar el servidor
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=4500, debug=True)