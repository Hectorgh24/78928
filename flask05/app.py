# app.py
from flask import Flask, render_template
from Producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for
import sqlite3

app = Flask(__name__)
   
#productos = [Producto("Coca", 25), Producto("Pepsi", 20), Producto("Fanta", 15)]


@app.route('/')
def inicio():
    #productos = [Producto("Coca", 25), Producto("Pepsi", 20), Producto("Fanta", 15)]
    con = conexion()
    productos = con.execute('SELECT * FROM productos').fetchall()
    print(productos)
    con.close()
    return render_template('producto.html', productos = productos)

@app.route('/editar/<id>')
def editar(id):
    #Recuperar el producto
    con = conexion()
    Producto = con.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    con.close()
    return render_template('editar.html', producto = Producto)

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre= request.form.get('nombre')
    precio= request.form.get('precio')
    id = request.form.get('id')
    print(f"{nombre} {precio} {id}")
    con = conexion()
    con.execute('UPDATE productos SET nombre = ?, precio = ? WHERE id = ?', (nombre, precio, id))
    con.commit()
    con.close()
    return Response("guardado", headers={'Location': '/'}, status=302)

    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("guardado", headers={'Location': '/'}, status=302)

# Eliminar un producto
@app.route('/eliminar/<id>')
def eliminar(id):
    print(id)
    con = conexion()
    con.execute('DELETE FROM productos WHERE id = ?', (id,))
    con.commit()
    con.close()
    return Response("eliminado", headers={'Location': '/'}, status=302)



@app.route('/agregar', methods=['POST'])
def agregar():
    nombre= request.form.get('nombre')
    precio= request.form.get('precio')
    con = conexion()
    con.execute('INSERT INTO productos(nombre, precio) VALUES (?,?)', (nombre, precio))
    con.commit()
    con.close()
    return redirect(url_for('inicio'))

def conexion():
    con = sqlite3.connect('basedatos.db')
    con.row_factory = sqlite3.Row
    return con

def iniciar_db():
    con = conexion()
    #se crea la tabla en caso de que no exista
    con.execute('''
                CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
                );
    ''')
    con.commit() #salva los datos desues de la ejecucion
    con.close()

if __name__ == '__main__':
    iniciar_db()
    app.run(host='0.0.0.0', debug=True)