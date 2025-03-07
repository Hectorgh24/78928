from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola_mundo():
    return 'Hola Hector' + mensaje_alternativo() 
def mensaje_alternativo():
    return 'la mañanera'
@app.route('/json')
def algo():
    return '[nombre: "Hector", edad: 22]'
@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><nombre>Hector</nombre><edad>22</edad>'
if __name__ == '__main__': #para que lo ejecute como  principal
    app.run(host = '0.0.0.0', debug = True)
