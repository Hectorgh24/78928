# app.py
from flask import Flask, render_template
from Producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for

app = Flask(__name__)
   
productos = [Producto("Coca", 25), Producto("Pepsi", 20), Producto("Fanta", 15)]


@app.route('/')
def inicio():
    return render_template('producto.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    #Recuperar el producto
    return render_template('editar.html', producto = producto, precio = precio)


@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get('nombre')
    p= request.form.get('precio')
    print(n,p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("guardado", headers={'Location': '/'}, status=302)


@app.route('/eliminar/<producto>')
def eliminar(producto):
    n= request.form.get('nombre')
    i = 0
    for e in productos:
        if e.nombre == n:
            productos.pop(i)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("eliminado", headers={'Location': '/'}, status=302)


@app.route('/agregar', methods=['POST'])
def agregar():
    nombre= request.form.get('nombre')
    precio= request.form.get('precio')
    productos.append(Producto(nombre,precio))
    print(f"{nombre} {precio}")
    #return Response("agregado", headers={'Location': '/'}, status=302)
    return redirect(url_for('inicio')) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)